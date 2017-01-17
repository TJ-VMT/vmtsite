#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'wuxishy & mabotkin'
SITENAME = 'TJ VMT'
SITEURL = 'https://tj-vmt.github.io/vmtsite'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('TJHSST', 'https://tjhsst.edu'),
         ('AoPS', 'http://aops.com'),
         ('AMC', 'http://www.maa.org/math-competitions'),
         ('ARML', 'http://arml.com'),
         ('HMMT', 'http://hmmt.co'),
         ('PUMaC', 'https://pumac.princeton.edu/'),
         ('CMIMC', 'http://www.cmimc.org/'),)

# Social widget
SOCIAL = (('facebook','https://www.facebook.com/groups/198737200195082/'),('github', 'https://github.com/TJ-VMT'),)

# site logo
#SITELOGO = 'img/vmt_logo.jpg'
#SITELOGO_SIZE = '60'
#HIDE_SITENAME = True

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['img']

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math']

THEME = "./themes/pelican-bootstrap3"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

TAGS_SAVE_AS = ''
TAG_SAVE_AS = ''

ARTICLE_EXCLUDES = ['weekly']

FAVICON = 'img/favicon.png'

BOOTSTRAP_THEME = 'readable'
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
HIDE_SIDEBAR = False
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False


