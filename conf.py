# Configuration file for the Sphinx documentation builder.

project = 'Graph Tool Tutorial'
author = 'Alex Tao'
release = '0.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'myst_nb',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

root_doc = 'index'

# -- MyST configuration ------------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "linkify",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 3
nb_execution_mode = 'off'

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "show_navbar_depth": 1,
    "show_toc_level": 2,
    "toc_title": "Contents",
}
html_title = "Graph Tool Tutorial"
html_static_path = []
