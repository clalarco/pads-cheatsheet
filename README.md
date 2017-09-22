HOW TO GENERATE THE DOCUMENT
============================

1. Install sphinx and sphinx-intl

    pip install sphinx sphinx-intl


2. Create the documentation for PADS Maker in spanish

    make singlehtml pads_maker es

2. Create the documentation for PADS Std Plus in english

    make singlehtml pads_std_plus en


TRANSLATIONS
------------

In pads_maker or pads_std_plus directories.

1. Create pot files for pads maker or pads_std_plus:

   make gettext pads_maker


2. (existing bug in sphinx-intl) In conf.py, set pads_maker or pads_std_plus as tag,
    at "# The master toctree document." section, before 'tags.has(...':

    tags.add('pads_maker')  # or tags.add('pads_std_plus')

2. Update language po files

    sphinx-intl update -l es -p build\gettext


3. Update translations (using a text editor)


4. Create documentation

    make singlehtml pads_maker es


FILES ORGANIZATION
------------------
- source/ Source file
    common/ Documentation common for PADS Std Plus and PADS Maker
    locale/ translations
    pads_std_plus/ Configuration and specific documentation for PADS Std Plus
    pads_maker/ Configuration and specific documentation for PADS Maker

common, pads_std_plus and pads_maker folder has a _static folder with
stylesheets (css) and images used in documentation.
