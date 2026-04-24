# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys


sys.path.insert(0, os.path.abspath("_ext"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = """<span style="text-align: center;
  font-weight: 700;line-height: 1;display: block;
  letter-spacing: .15em;
  font-size: .6em;">EARTH HISTORY @ UVIC<br>TEACHING</span>"""
copyright = '2024, Blake Dyer'
author = 'Blake Dyer'
release = '2024'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["crate.sphinx.csv", "sphinx.ext.mathjax"]

nb_execution_mode = "off"

# myst_enable_extensions = [
#     "amsmath",
#     "colon_fence",
#     "deflist",
#     "dollarmath",
#     "html_image",
# ]



myst_url_schemes = ("http", "https", "mailto")
templates_path = ['_templates']
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_theme_options = {
    # "github_url": "https://github.com/blakedyer/eos-courses",
    "show_prev_next": False,
    "search_bar_text": "Search",
    "navbar_start": [],
    "navbar_persistent": [],
    "article_header_start": [],
    "article_header_end": [],
    "secondary_sidebar_items": [],
    "use_download_button": False,
    "use_fullscreen_button": False,
    "logo": {
        "text": project,
    },
}
html_sidebars = {
    "**": ["navbar-logo.html", "site-hub-link.html", "search-field.html", "sbt-sidebar-nav.html"],
}
html_logo = "_static/logo.jpg"
html_favicon = 'favicon.png'
html_static_path = ['_static','eos240-public/Lectures','eos408-public/Lectures','eos423-public/Lectures']
html_css_files = ['custom.css']
html_js_files = ['live-course.js']
html_title = "Earth History @ UVIC"
html_baseurl = "https://eos-courses.readthedocs.io/en/latest/"
