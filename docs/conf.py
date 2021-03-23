# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
import nanotune
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('../'))
sys.path.insert(0, os.path.abspath('../../../'))
sys.path.insert(0, os.path.abspath('../../../qcodes'))
sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = 'nanotune'
copyright = '2019, Jana Darulova'
author = 'Jana Darulova'

# auto versioning
version = '{}'.format(nanotune.__version__)
# The full version, including alpha/beta/rc tags.
# version = ''
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
    'nbsphinx',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    'sphinx-jsonschema',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo'
    # 'sphinx.ext.autodoc',
    # 'sphinx.ext.doctest',
    # 'sphinx.ext.intersphinx',
    # 'sphinx.ext.todo',
    # 'sphinx.ext.coverage',
    # 'sphinx.ext.imgmath',
    # 'sphinx.ext.ifconfig',
    # 'sphinx.ext.viewcode',
    # 'sphinx.ext.githubpages',
    # 'sphinx.ext.todo',
    # 'rinoh.frontend.sphinx'
]

napoleon_include_special_with_doc = True

# autodoc_mock_imports = ['numpy', 'jsonschema',  'ruamel_yaml',
#                          #'qcodes', 'qcodes.dataset',
#                         #  'websockets', 'h5py', 'visa', 'pyvisa', 'zmq',
#                         #  'wrapt',
#                         'scipy', 'matplotlib', 'mpl_toolkits', 'sklearn',
#                         'skimage', 'yaml', 'git', 'joblib', 'reportlab',
#                         'pandas', 'PyQt5', 'PIL']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '_templates', '_auto',
                    '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'nanotunedoc'

html_use_index = True


# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    'preamble': '',
    # Latex figure (float) alignment
    #
    'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'nanotune.tex', 'nanotune Documentation',
     'Jana Darulova', 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'nanotune', 'nanotune Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'nanotune', 'nanotune Documentation',
     author, 'nanotune', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'pandas': ('https://pandas.pydata.org/pandas-docs/stable/', None),
    'matplotlib': ('https://matplotlib.org/', None),
    'python': ('https://docs.python.org/3.6', None),
    'numpy': ('https://docs.scipy.org/doc/numpy', None),
    'py': ('https://pylib.readthedocs.io/en/stable/', None),
    'pyvisa': ('https://pyvisa.readthedocs.io/en/master/', None),
    'IPython': ('https://ipython.readthedocs.io/en/stable/', None),
    'qcodes': ('https://qcodes.github.io/Qcodes/', None),
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

utoclass_content = "both"
# classes should include both the
# class' and the __init__ method's docstring

autosummary_generate = True
autodoc_member_order = 'bysource'
autodoc_default_options = {'members': '',
                           'undoc-members': True,
                        #    'inherited-members': True,
                            'show-inheritance': True,
                            }

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
texinfo_show_urls = 'footnote'

numfig = True

# Use this kernel instead of the one stored in the notebook metadata:
nbsphinx_kernel_name = 'python3'
# always execute notebooks.
nbsphinx_execute = 'always'