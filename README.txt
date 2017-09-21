HOW TO GENERATE THE DOCUMENT
============================

1. Install sphinx and sphinx-intl

    pip install sphinx sphinx-intl


2. Create the documentation

    cd pads_std_plus  # or pads_maker
    make singlehtml


TRANSLATIONS
------------

1. Create pot files

   make gettext


2. Update language po files

    sphinx-intl update -l es -p _build\gettext


3. Update translations (using a text editor)


4. Create documentation

    cd pads_std_plus  # or pads_maker
    make singlehtml


FILES ORGANIZATION
------------------

- common/ Documentation common for PADS Std Plus and PADS Maker
- locale/ translations
- pads_std_plus/ Configuration and specific documentation for PADS Std Plus
- pads_maker/ Configuration and specific documentation for PADS Maker

common, pads_std_plus and pads_maker folder has a _static folder with
stylesheets (css) and images used in documentation.
