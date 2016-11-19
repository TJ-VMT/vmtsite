#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'SHY'
SITENAME = 'TJ VMT'
SITEURL = 'https://wuxishy.github.io/vmtsite'

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
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['img']

PLUGIN_PATHS = ['/home/compsci/pelican-plugins']
PLUGINS = ['render_math']

THEME = "/home/compsci/pelican-themes/pelican-bootstrap3"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

BOOTSTRAP_THEME = 'readable'
SHOW_ARTICLE_AUTHOR = False
SHOW_ARTICLE_CATEGORY = False
HIDE_SIDEBAR = True
DISPLAY_CATEGORIES_ON_MENU = False
#DISPLAY_TAGS_ON_SIDEBAR = True
