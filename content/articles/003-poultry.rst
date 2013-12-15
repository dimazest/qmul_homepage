========================================================
 A story behind Poultry, a Twitter Streaming API client
========================================================

:date: 2013-12-14 17:42
:tags: tools, twitter

Poultry is a `Twitter Streaming API`__ client and a tweet collection manager
that I started developing for the `Semantic Web course`__ together with Annisa
Ihsani. Later, it powered the experiments for my `master`__ thesis and the
following `paper`__. To be completely accurate, my project was partially done
during the internship at `Paylogic`__.

This post is about `poultry`__ development story mostly in pictures. Read the
`user guide`__ if you want to use it, or go to the `github page`__ if you want
to hack it.

__ https://dev.twitter.com/docs/streaming-apis/streams/public
__ http://www.rug.nl/ocasys/fwn/vak/show?code=LIX002M05&ocasysyear=2013
__ http://lct-master.org/
__ http://www2013.org/companion/p795.pdf
__ http://www.paylogic.com/en/

The early beginning
-------------------

.. figure:: {filename}/static/images/fowler_talk.jpg
    :figwidth: 90%
    :width: 100%
    :align: center
    :alt: The first public mention of Fowler/Poultry.

    The first presentation of Fowler in Prague in 2011. The power of pipe.
    Thanks Annisa for the picture!


__ https://pypi.python.org/pypi/poultry
__ http://poultry.readthedocs.org/en/latest/
__ https://github.com/dimazest/poultry


The bigger the data you are collecting, the bigger the problems you have
managing it. I understood it shortly after a bunch of bash one-liners was not
capable to deal with the sample twitter stream. Also my appetite grew, I wanted
to track many words, people, locations; ultimately, build streams based on
topics and so on.

Also, generators was a `hot topic`__ at `Europython 2011`__ and they kept
popping up in my head. I came across `A Curious Course on Coroutines and
Concurrency`__ around that time and decided to implement my Twitter client
using generators.

__ https://ep2013.europython.eu/conference/talks/beyond-python-enhanched-generators
__ https://ep2013.europython.eu/ep2011
__ http://dabeaz.com/coroutines/

The glory
---------

The following summer was fun. We watched the UEFA championship both on the TV
and a Twitter in extremely international environment. Sometimes it was more fun
to read the tweets that following the TV broadcast.


.. figure:: {filename}/static/images/euro_grunn.jpg
    :figwidth: 90%
    :width: 100%
    :alt: Wellington enjoys sports and drinks!

    Wellington enjoys sports and drinks!

At Europython 2012 I gave a lighting talk, showing small visualizations. I was
so busy with preparing it, that I barely had time to attend other talks :).

.. figure:: {filename}/static/images/euro_italy.jpg
    :figwidth: 90%
    :width: 100%
    :alt: I'm in front of the IT crowd.

    Pythonistas follow the trending words during some game. Thanks,  Daniel
    Pyrathon for the picture.

After I finished my master and got a job at Paylogic, the project didn't get
any attention. However, I got a chance to present some advanced aspects of it at
`Pygrunn`__, thanks to Berco Beute.

__ http://www.pygrunn.org/

.. figure:: {filename}/static/images/pygrunn2013_02.jpg
    :figwidth: 90%
    :width: 100%
    :alt: The most classy stage I've ever seen.

    I'm trying to be hip, before leaving to Brazil. Thanks, Òscar Vilaplana for
    the picture!

In Brazil, I presented the paper at a `workshop`__ collocated with `WWW
2013`__.

__ http://www.ramss.ws/2013/
__ http://www2013.wwwconference.org/

The future
----------

This is a short story of poultry. It was a lot of fun for me to work on this
code. Finally, I got some time to package and upload it to PYPI. Now
it is able to get its own unique story.

P.S. Initially, the package was called ``fowler``, but I decided to rename it
to ``poultry``.

P.P.S. And I would like to additionally thank Gosse Bouma (for my thesis
supervision), Karol Kuczmarski (for useful discussion), Paylogic crew (for
support), Alexandre González Rodríguez (for organizing and inviting people to
parties) and Maria Nadejde (for asking for an advice on Python and Twitter).
