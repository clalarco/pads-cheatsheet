from os.path import abspath, dirname, join
import argparse

from subprocess import call

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
        choices=['doc', 'translations', 'trans', 'publish'])

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
        publish(tool, language)


if __name__ == '__main__':
    main()
