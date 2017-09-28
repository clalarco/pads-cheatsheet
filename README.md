PADS CHEAT SHEET
================

This is a repository where cheat sheet is generated.

The result after publishing and push can be seen here:

Spanish: https://clalarco.github.io/pads-cheatsheet/maker/es/
English: https://clalarco.github.io/pads-cheatsheet/maker/en/


HOW TO GENERATE DOCUMENTATION
-----------------------------
0. Install python if not installed

1. Install sphinx and sphinx-intl

    ```pip install sphinx sphinx-intl```


2. Create the documentation for PADS Maker in spanish

    ```python build.py doc pads_maker es```

2. Create the documentation for PADS Std Plus in english

    ```python build.py doc pads_std_plus en```


The documentation will be stored at build/<tool>/<lang>/singlehtml


TRANSLATIONS
------------

1. Update languages::

   ```python build.py translations```


3. Update translations (.po files) en ```source\locale\<lang>\LC_MESSAGES```
    using a text editor


4. Create documentation, in ```build``` directory.

    ```python build.py doc pads_maker es```


PUBLISHING
----------

You need to clone the repo from github to make this work, 
instead just downloading the zip file.


1. If required, create gh-pages:

    ```python build.py prepare-publish```

2. Publish the tool/language or all:

    ```python build.py publish pads-maker es```

    or

    ```python build.py publish-all```

3. Change to ```gh-pages/``` directory and commit the changes into git.

4. Push your changes.


FILES ORGANIZATION
------------------
- ```source/``` Source file
    ```common/``` Documentation common for PADS Std Plus and PADS Maker
    ```locale/``` translations
    ```pads_std_plus/``` Configuration and specific documentation for PADS Std Plus
    ```pads_maker/``` Configuration and specific documentation for PADS Maker
- ```build/``` the generated documentation by Sphinx
- ```gh-pages/``` the published version of cheat sheet, accessible from https://clalarco.github.io/pads-cheatsheet/
    This directory is a copy of the repo, but pointing to git ```gh-pages``` branch.

```common```, ```pads_std_plus``` and ```pads_maker``` folder has a ```_static``` folder with
stylesheets (css) and images used in documentation.
