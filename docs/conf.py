# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

rtd = os.environ.get('READTHEDOCS', False)


extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon'
]

source_suffix = '.rst'
master_doc = 'index'
project = 'qfutil'
year = '2015'
author = 'kalhartt'
copyright = '{0}, {1}'.format(year, author)
version = release = '0.1.0'

if not rtd:
    import sphinx_py3doc_enhanced_theme
    html_theme = "sphinx_py3doc_enhanced_theme"
    html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]

    pygments_style = 'trac'
    templates_path = ['.']
    html_use_smartypants = True
    html_last_updated_fmt = '%b %d, %Y'
    html_split_index = True
    html_sidebars = {
        '**': ['searchbox.html', 'globaltoc.html', 'sourcelink.html'],
    }
    html_short_title = '%s-%s' % (project, version)
    html_theme_options = {
        'githuburl': 'https://github.com/MGXRace/python-qfutil/'
    }
