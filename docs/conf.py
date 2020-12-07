# -*- coding: utf-8 -*-
#
# Iracema documentation build configuration file, created by
# sphinx-quickstart on Fri Oct 20 04:13:51 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('..'))

from iracema import __version__


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.todo',
              'sphinx.ext.coverage', 'sphinx.ext.mathjax',
              'sphinx.ext.ifconfig', 'sphinx.ext.viewcode',
              'sphinx.ext.githubpages', 'sphinxcontrib.napoleon',
              'matplotlib.sphinxext.plot_directive', 'sphinx.ext.doctest'
              ]

# Hide source code link for plotting
plot_html_show_source_link = False
# plot_html_show_formats = False

# setup code for doctest
doctest_global_setup = """
import iracema as ir
import os
from pathlib import Path
samples_path = Path(ir.root, '..', 'audio', 'iracema-audio')
os.chdir(samples_path)
# preload one sample file
clarinet_audio = ir.Audio.load('03 - Clarinet - Fast Excerpt.wav')
clarinet_data = clarinet_audio.data
clarinet_fs = clarinet_audio.fs
"""

plot_pre_code = """
import iracema as ir
import os
from pathlib import Path
samples_path = Path(ir.root, '..', 'audio', 'iracema-audio')
os.chdir(samples_path)
clarinet_audio = ir.Audio.load('03 - Clarinet - Fast Excerpt.wav')
clarinet_data = clarinet_audio.data
clarinet_fs = clarinet_audio.fs
"""

# Add any paths that contain templates here, relative to this directory.
templates_path = [
    'templates'
]

source_suffix = '.rst'
master_doc = 'index'

# General information about the project.
project = u'Iracema'
copyright = u'2019, Tairone N. Magalhães'
author = u'Tairone N. Magalhães'

# The short X.Y version.
version = __version__
 # The full version, including alpha/beta/rc tags.
release = version

language = 'en'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = 'img/iracema-white.png'
html_show_sphinx = False

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': True,
    'logo_only': True,
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars



# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'iracemadoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'iracema.tex', u'Iracema Documentation',
     u'Tairone N. Magalhaes', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'iracema', u'Iracema Documentation',
     [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'iracema', u'Iracema Documentation',
     author, 'iracema', 'One line description of project.',
     'Miscellaneous'),
]

# -- Options for multiversioning ------------------------------------------

smv_tag_whitelist = r'^\d+\.\d+.\d+$'
smv_branch_whitelist = r'^(master|develop)$'

# -- Other options --------------------------------------------------------

autodoc_mock_imports = ["sounddevice"]
autoclass_content = 'both'
autodoc_member_order = 'bysource'

# napoleon settings
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_ivar = True
napoleon_include_init_with_doc = False

