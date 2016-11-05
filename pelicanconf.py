#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False


AUTHOR = u'John Martinez'
SITENAME = u'cache_money_hoes'
SITEURL = ''


TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

MARKUP = 'md'

DEFAULT_DATE_FORMAT = '%B %d, %Y'

SUMMARY_MAX_LENGTH = 100
DEFAULT_PAGINATION = 10

PAGE_DIRS = ['pages']
ARTICLE_DIRS = ['articles']

THEME = 'nice-blog'
STATIC_PATHS = ['images']

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS= 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS

STATIC_PATHS = ['images', 'robots.txt', 'CNAME']

# DEFAULT_HEADER_BG = '/images/<insert-an-image.jpg>'
GITHUB_USERNAME = 'gobrewers14'
SHOW_ARCHIVES = True
SHOW_FEED = True

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['sitemap', 'latex']

SITEMAP = {
  'format': 'xml'
}
