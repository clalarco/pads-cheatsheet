# -*- coding: utf-8 -*-
#
# PADS Maker Cheat Sheet build configuration file, created by
# sphinx-quickstart on Fri Jun 09 15:20:25 2017.
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
d = os.path.dirname(os.path.abspath(__file__))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
print ([t for t in tags])
if tags.has('pads_maker'):
    master_doc = 'index-pads-maker'
    # General information about the project.
    project = u'PADS Maker'
    product = u'PADS Maker'
    copyright = u'2017, Mentor Graphics'
    author = u'Mentor Graphics'

    # The version info for the project you're documenting, acts as replacement for
    # |version| and |release|, also used in various other places throughout the
    # built documents.
    #
    # The short X.Y version.
    version = u'2.0'
    # The full version, including alpha/beta/rc tags.
    release = u'2.0'

else:
    master_doc = 'index-pads-std-plus'
    # General information about the project.
    project = u'PADS Std Plus'
    product = u'PADS Std Plus'
    copyright = u'2017, Mentor Graphics'
    author = u'Mentor Graphics'

    # The version info for the project you're documenting, acts as replacement for
    # |version| and |release|, also used in various other places throughout the
    # built documents.
    #
    # The short X.Y version.
    version = u'VX.2.1'
    # The full version, including alpha/beta/rc tags.
    release = u'VX.2.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'
locale_dirs = ['locale']
gettext_compact = False

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    '_build',
    'Thumbs.db',
    'common/icons-logos.rst',
]

if tags.has('pads_maker'):
    exclude_patterns.append('index-pads-std-plus.rst')
    exclude_patterns.append('pads_std_plus')
    exclude_patterns.append('common/schematics/blocks.rst')

if tags.has('pads_std_plus'):
    exclude_patterns.append('index-pads-maker.rst')
    exclude_patterns.append('pads_maker')

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = project + " Cheat Sheet"
html_theme = 'epub'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

html_theme_options = {'relbar1': False, 'footer': False}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['common/_static', 'pads_maker/_static', 'pads_std_plus/_static']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
if tags.has('pads_maker'):
    htmlhelp_basename = 'padsmaker'

if tags.has('pads_std_plus'):
    htmlhelp_basename = 'padsstdplus'

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
    (master_doc, htmlhelp_basename + '.tex', html_title,
     u'Mentor Graphics', 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, htmlhelp_basename, html_title,
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, htmlhelp_basename, html_title,
     author, htmlhelp_basename, 'One line description of project.',
     'Miscellaneous'),
]



# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

def setup(app):
    app.add_stylesheet('css/cheatsheet.css')
