#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dmitrijs Milajevs'
SITENAME = 'Dmitrijs Milajevs'
SITESUBTITLE = 'at Queen Mary University of London'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
# THEME = 'notmyidea'
THEME = 'flasky'

SECTIONS = (
    ('Home', 'index.html'),
    ('Blog', 'category/articles.html'),
    # ('Archive', 'archives.html'),
    # ('Tags', 'tags.html'),
    # ('Projects', 'pages/projects.html'),
    # ('Talks', 'pages/talks.html'),
    # ('About', 'pages/about-me.html'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

# Blogroll
LINKS = (
    ('Theory group at QMUL', 'http://theory.eecs.qmul.ac.uk/'),
    ('Cogsci group at QMUL', 'http://cogsci.eecs.qmul.ac.uk/'),
    ('The Python Club', 'https://www.facebook.com/groups/723364331026623/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/dimazest'),
    ('Facebook', 'https://www.facebook.com/dimazest'),
    ('Github', 'https://github.com/dimazest'),
    ('Bitbucket', 'https://bitbucket.org/dimazest'),
)

MAIL_USERNAME = 'd.milajevs'
MAIL_HOST = 'qmul.ac.uk'

TWITTER_USERNAME = 'dimazest'
DISQUS_SITENAME = 'dmitrijsmilajevs-qmul'
GITHUB_URL = 'https://github.com/dimazest'
GOOGLE_ANALYTICS = 'UA-1173947-7'
LINKEDIN_URL = 'http://www.linkedin.com/in/dmitrijsmilajevs'

STATIC_PATHS = (
    'images',
    'static',
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
