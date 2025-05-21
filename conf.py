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
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

myst_heading_anchors = 3
nb_execution_mode = 'off'

pygments_style = "friendly"  # or "sphinx", "friendly", etc.
highlight_options = {"linenos": True}
nb_render_code_kwargs = {
    "linenos": True,
}

# -- HTML output -------------------------------------------------------------

html_theme = "sphinx_book_theme"
html_theme_options = {
    "home_page_in_toc": True,
    "show_navbar_depth": 3,
    "show_toc_level": 2,
    "toc_title": "Contents",
}
html_title = "graph-tool tutorial"
html_static_path = []


import os
import datetime

html_last_updated_fmt = "%b %d, %Y"

# This tells Sphinx to get the last modified date from git, if possible
today = datetime.date.today().strftime(html_last_updated_fmt)
html_context = {
    "last_updated": today,
}