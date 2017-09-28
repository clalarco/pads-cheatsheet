
from os import chdir, getcwd
from os.path import abspath, dirname, join, isdir
from subprocess import call
from shutil import rmtree, copytree, ignore_patterns, move

import argparse


def call_sphinx(action, tool, language):
    """ Launch a sphinx action.
    """
    # Directories.
    root_dir = dirname(abspath(__file__))
    src_dir = join(root_dir, 'source')
    build_dir = join(root_dir, 'build')
    if action not in ['gettext']:
        build_dir = join(build_dir, tool, language)

    sphinx_cmd = ['python', '-m', 'sphinx',
                   '-M', action,
                   src_dir, build_dir,
                   '-D', 'language=%s' % language,
                   '-t', tool
    ]
    print(sphinx_cmd)
    call(sphinx_cmd)


def call_sphinx_intl(tool, language):
    """ Launch a sphinx action.
    """
    # Directories.
    root_dir = dirname(abspath(__file__))
    pot_dir = join(root_dir, 'build', 'gettext')

    sphinx_intl_cmd = [
        'python', '-m', 'sphinx_intl',
        '-t', tool,
        'update',
        '-l', language,
        '-p', pot_dir,
    ]
    print(sphinx_intl_cmd)

    call(sphinx_intl_cmd)


def create_doc(tool, language):
    """ Create documentation.
    """
    call_sphinx('singlehtml', tool, language)


def create_translations():
    """ It creates/updates translations.
    """
    tools = ['pads_std_plus', 'pads_maker']
    languages = ['en', 'es']

    # Create/update .pot files. 'en' as default language.
    for tool in tools:
        call_sphinx('gettext', tool, 'en')

    # Update locales.
    for tool in tools:
        for language in languages:
            call_sphinx_intl(tool, language)

def prepare_publish():
    """ It copies the .git directory into gh-pages, and
    change the branch to gh-pages.
    """
    root_dir = dirname(abspath(__file__))
    gh_dir = join(root_dir, 'gh-pages')
    git_dir = join(root_dir, '.git')

    # Copies .git directory.
    if isdir(git_dir):
        # Remove gh-pages if exists.
        if isdir(gh_dir):
            rmtree(gh_dir)

        copytree(git_dir, join(gh_dir, '.git'))

    # Change branch.
    current_dir = getcwd()
    chdir(gh_dir)
    call(['git', 'checkout', 'gh-pages'])
    chdir(current_dir)


def publish(tool, language):
    """ Copy the build results into gh-pages folder.
    It does not add, commit nor push the changes.
    """

    # Creates documentation.
    create_doc(tool, language)

    tool_dir = {'pads_maker': 'maker', 'pads_std_plus': 'std_plus'}[tool]
    index_filename = {'pads_maker': 'index-pads-maker.html', 'pads_std_plus': 'index-pads-std-plus.html'}[tool]

    # Copy the results into gh-pages
    root_dir = dirname(abspath(__file__))
    src_dir = join(root_dir, 'build', tool, language, 'singlehtml')
    dest_dir = join(root_dir, 'gh-pages', tool_dir, language)

    # Delete the old directory and copy the new content.
    if isdir(dest_dir):
        rmtree(dest_dir)

    # Copy content and rename index.html.
    copytree(src_dir, dest_dir, ignore=ignore_patterns('.buildinfo', 'objects.inv'))
    move(join(dest_dir, index_filename), join(dest_dir, 'index.html'))

    # Create .nojekyll file in gh-pages/ if it does not exist.
    open(join(root_dir, 'gh-pages', '.nojekyll'), 'a').close()


def parse_args():
    parser = argparse.ArgumentParser()

    # Actions:
    #   translations
    #   doc
    #   publish

    # tool
    #   pads_maker
    #   pads_std_plus

    # language

    parser.add_argument(
        'action', help="Action to select.",
        choices=['doc', 'translations', 'trans', 'publish', 'prepare-publish', 'publish-all'])

    parser.add_argument(
        'tool', help="Tool to build.", nargs='?', default='pads_maker',
        choices=['maker', 'pads_maker', 'std_plus', 'pads_std_plus'])

    parser.add_argument(
        'language', help="Language to build.", nargs='?', default='es')

    args = parser.parse_args()
    return args


def main():
    args = parse_args()

    # Check tool aliases.
    if args.tool == 'maker':
        args.tool = 'pads_maker'

    if args.tool == 'std_plus':
        args.tool = 'pads_std_plus'

    # Check actions.
    if args.action == 'doc':
        create_doc(args.tool, args.language)

    if args.action in ['translations', 'trans']:
        create_translations()

    if args.action in ['publish']:
        publish(args.tool, args.language)

    if args.action in ['publish-all']:
        for tool in ['pads_maker', 'pads_std_plus']:
            for language in ['es', 'en']:
                publish(tool, language)

    if args.action in ['prepare-publish']:
        prepare_publish()



if __name__ == '__main__':
    main()
