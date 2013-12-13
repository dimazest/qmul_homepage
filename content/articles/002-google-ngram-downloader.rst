=======================
Google ngram downloader
=======================

:date: 2013-11-28 10:30
:tags: tools

I'm building a word co-occurrence matrix out of `The Google Books Ngram Viewer
dataset`__. The dataset for 5 grams is so large, that I don't know if I have
enough space to store it.

__  http://storage.googleapis.com/books/ngrams/books/datasetsv2.html


To overcome the storage issue, I decided not to download the data first, and
process it later. Instead, I process the data as it's being downloaded.

`Google ngram downloader`__ is a small library that makes it easy to access the
ngram data in a streaming fashion. It iterates over the links of ngrams and
returns an iterator over the content of them.

__ https://pypi.python.org/pypi/google-ngram-downloader

Here is a piece of code that returns the first 5gram from the Google
collection.

.. code-block:: python

    >>> from google_ngram_downloader import readline_google_store
    >>>
    >>> fname, url, records = next(readline_google_store(ngram_len=5))
    >>> fname
    'googlebooks-eng-all-5gram-20120701-0.gz'
    >>> url
    'http://storage.googleapis.com/books/ngrams/books/googlebooks-eng-all-5gram-20120701-0.gz'
    >>> next(records)
    Record(ngram='0 " A most useful', year=1860, match_count=1, volume_count=1)

You are welcome to `fork the code`__!

__ https://github.com/dimazest/google-ngram-downloader

P.S. While I was looking for the package on PyPI, I figured out that there is a
`similar script`__. The ideas behind the implementations are similar, though
the code is different :)

__ http://blog.barvinograd.com/2011/12/google-n-gram-downloader/

Update: The dataset is avalable on `Amazon AWS`__.

__ http://aws.amazon.com/datasets/8172056142375670
