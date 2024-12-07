# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sphinx_rtd_theme

# -- Project information -----------------------------------------------------

project = 'Test Assignment'
copyright = '2024, Me'
author = 'Olga Erman'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinxcontrib.contentui',
    'sphinx_copybutton',
    'docxbuilder',
    'sphinxcontrib.images',
    'sphinx_design',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '**/_includes/*',
    '_includes/*',
    #'**/template_pages.rst',
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages. See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['custom.css',]

html_js_files = ['custom.js',]

html_logo = "_static/logo.png"

#Custom sidebar templates, must be a dictionary that maps document names to template names.

html_sidebars = {
   '**': ['globaltoc.html'],
   'using/windows': ['windowssidebar.html', 'searchbox.html'],
   "administrator_guide/platform_setting/*": []
}

# A dictionary of options that influence the look and feel of the selected theme.
# These are theme-specific.

html_theme_options = {
    "navbar_start": "logo.html",
    "navbar_end": ["navbar-icon-links.html", "search-field.html"],
    "show_toc_level": 2,
}

# If true, images itself links to the original image
# if it doesn’t have ‘target’ option or scale related options:
# ‘scale’, ‘width’, ‘height’. The default is True.
# Document authors can this feature manually with giving no-scaled-link class to the image:

html_scaled_image_link = False

# The style name to use for Pygments highlighting of source code.
# If not set, either the theme’s default style or 'sphinx' is selected for HTML output.


# -- Other -------------------------------------------------

pygments_style = 'sphinx'
primary_domain = 'py'
# A string of reStructuredText that will be included at the beginning of every source file that is read.
# Place to add substitutions that should be available in every file (another being rst_epilog).

# Internationalization path.

# locale_dirs = ['locale/']
# gettext_compact = False     # optional.
# gettext_location = True
# gettext_additional_targets = ['literal-block', 'index terms', 'doctest block', 'image']
# figure_language_filename = '{path}{language}/{basename}{ext}'
# gettext_allow_fuzzy_translations = True

# Prologue - https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog

# with open('_includes/prolog.rst', 'r') as prolog:
#     rst_prolog = prolog.read()

