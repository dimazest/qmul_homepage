===========================================
The routine of Machine Learning experiments
===========================================

:date: 2013-11-23 12:00

A couple of months ago I started a Ph.D. at Queen Mary University of London.
It's too early to say what my work is exactly about, but it is somewhere in the
intersection of compositional distributional semantics and dialogs. My first
task was to implement a dialog act tagging model which is described in `Latent
Semantic Analysis for dialog act classification`__ by Riccardo Serafin and
others. Later, I applied the method on the Switchboard dialog corpus and
reported the results to my supervisors.

__ http://acl.ldc.upenn.edu/N/N03/N03-2032.pdf

The steps I performed seem to be very typical for many machine learning tasks,
so it worth to look closer to them. Here are the steps:

1. Obtain labeled data.
2. Transform it to the appropriate format, so it can be fed up to a classifier.
3. Implement the classifier.
4. Train the classifier on some data.
5. Evaluate it on another data.
6. Report and interpret the results.

I would like to share some observations I made.

Obtaining the data and storing extracted features
-------------------------------------------------

It's not that hard to obtain the data, most probably there is some well known
data set, which is used by everyone in the field. It is usually available  in
several files in the CSV format (CSV is somewhat human readable and it can be
processed by virtually every language). For more sophisticated data structures,
there might be a wrapper that provides a simplified access to the data. For
example, `swda.py`__ provides a convenient way of iterating over utterances in
Switchboard.

__ http://compprag.christopherpotts.net/swda.html

Unfortunately, there is no way of feeding random human-readable data to a
classifier and expecting a meaningful result. The data has to be transformed
into feature vectors and their labels. Usually the transformed data is stored
again in a CSV file. However, I find it's much more convenient to store in a
more sophisticated, probably binary form.

Pandas provides powerful `IO functionality`__. I would suggest to go with a
HDF5 store, because it's designed to be fast. What to store in the file depends
on the classifier and the task. I had to build a large sparse matrix, where
features are words and documents are utterances. I don't store the matrix
directly, but I store two arrays, one contains the values of the matrix,
another one contains their coordinates in the matrix. It is highly inspired by
the `sparse matrix implementation`__ in scipy::

    This can be instantiated in several ways:

        ...

        csr_matrix((data, ij), [shape=(M, N)])
        where data and ij satisfy the relationship a[ij[0, k], ij[1, k]] = data[k]

__ http://pandas.pydata.org/pandas-docs/stable/io.html
__ http://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.csr_matrix.html#scipy.sparse.csr_matrix

The library I use to solve the task dictates the input format. The code that
performs model training and classification is almost free from converting the
input data into some internal data structure.

The main advantage of HDF5 (and, probably, JSON, but I didn't try it) is
that the produced file can contain metadata. Metadata can be anything! A
dictionary of keys and values will do the work. I find it useful to store the
command this file was generated, the day it was generated, and some reporting
specific information: the number of documents and the number of features. These
are very useful for producing reports.

Clearly, the metadata could be put to the file name, but if it is done manually
it's error prone and parsing the input file name is not a pleasant task. I give
reasonable names to the files, however, the file name is automatically
generated, so I don't need to bother about good naming every time I generate
the input data.

Showing the results
-------------------

This easily getting more complex as you demand more and more from the
evaluation.

The simplest way is to show the metric you care about in the end of the run, so
in the terminal you will see something like::

    $ ml-tool -i data5k.h5 --model-parameter-k=50
    Accuracy: 0.6 (+/- 0.2)

Which gives so little context, that understanding what the experiment was about
is next to impossible. An you will have to store this somewhere (probably by
copy pasting to some file and giving a brief comment what it's about), so you
can write an email to your supervisor.

It is possible to get more evaluation metrics. I got inspired by the
`scikit-learn parameter estimation with grid search example`__.

The example gives very detailed information of the evaluation step, though it
puts together calculation of the results and the representation.

__ http://scikit-learn.org/stable/auto_examples/grid_search_digits.html#example-grid-search-digits-py

A standard way of splitting these two is to use a template engine. The values
for the template are prepared in the code, and then passed to the template to
be rendered. Now it's up to template how to represent the data. It can be an
regular text file, an HTML page.

HTML pages are great for sharing, remember, that finally I have to send the
results to my supervisors, but the text format is great for development and
debugging. Keeping two versions is an overhead I can't afford, so I decided to
use reStructuredText. `reStructuredText`_ is a human readable formating format.
With RST you can render tables, text styles, headers, links and much more. It
is possible to render rst documents as HTML pages, PDF, or even LaTeX. I used
`Jinja2`_ as the templating engine.

Inside of my template I show some metadata, so if I find a page with a printed
report in a year, I'll know what it is about.

Here is the template:

.. code-block:: rst

    Hyper parameter estimation
    ==========================

    :paper: {{ paper }}
    :accuracy: {{ accuracy.round(3) }}
    :best estimator: {{ clf.best_estimator_ }}
    {%- for key, value in store_metadata.items()  %}
    :{{  key }}: {{ value }}
    {%- endfor %}
    :command: {{ argv }}

    Grid accuracy scores on development set::

        {% for s in clf.grid_scores_ %}
        {{ s.mean_validation_score|round(3) }} (+/-{{ (s.cv_validation_scores.std() / 2.0)|round(3) }}) for {{s.parameters}}
        {%- endfor %}

    Evaluation results
    ------------------

    ==================== ========== ========== ========== ==========
                    tag  precision     recall   f1-score    support
    ==================== ========== ========== ========== ==========
    {%- for t, p, r, f, s in tprfs %}
    {%- set t = t.replace('+', '\+').replace('_', '\_').rjust(19) %}
    {%- set p = '{:0.3f}'.format(p).rjust(10) %}
    {%- set r = '{:0.3f}'.format(r).rjust(10) %}
    {%- set f = '{:0.3f}'.format(f).rjust(10) %}
    {%- set s = (s|string).rjust(10) %}
    {{ t              }} {{ p    }} {{ r    }} {{ f    }} {{ s    }}
    {%- endfor %}
    -------------------- ---------- ---------- ---------- ----------
    {%- set p_avg = '{:0.3f}'.format(p_avg).rjust(10) %}
    {%- set r_avg = '{:0.3f}'.format(r_avg).rjust(10) %}
    {%- set f_avg = '{:0.3f}'.format(f_avg).rjust(10) %}
    {%- set s_sum = (s_sum|string).rjust(10) %}
      weighted avg/total {{ p_avg}} {{ r_avg}} {{ f_avg}} {{ s_sum}}
    ==================== ========== ========== ========== ==========

    The model is trained on the full development set.
    The scores are computed on the full evaluation set.

And `here`__ is the result rendered with `restview`_. Restview killer feature
is that it render .rst files as HTML documents and servers them in an embedded
web server. If you point a browser to the rendered document and modify the
source .rst, the page will get refreshed.

__ {filename}/static/results/index.html

It is still a proof of concept, but it shows how to easily report experiment
results easily.

.. _Jinja2: http://jinja.pocoo.org/docs/
.. _reStructuredText: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. _restview: https://pypi.python.org/pypi/restview
