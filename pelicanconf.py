#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Dmitrijs Milajevs'
SITENAME = 'Dmitrijs Milajevs'
SITEURL = ''

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'en'
THEME = 'notmyidea'

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
    ('Github', 'https://github.com/dimazest'),
    ('Facebook', 'https://www.facebook.com/dimazest'),
)

STATIC_PATHS = (
    'images',
    'static',
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
