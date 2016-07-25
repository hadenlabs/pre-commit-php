#!/usr/bin/env python

"""
Git pre-commit hook for checking code php instructions

Author:
    Luis Alberto Mayta

"""

from __future__ import print_function
import argparse
import sys


VERSION = '0.0.0'


def check_file_validator(file_name):
    """Check Text files"""

    functions_black_list = (
        'eval',
        'var_dump',
        'print_r',
    )

    list_lines = []

    with open(file_name, 'r') as filename:
        for line, value in enumerate(filename):
            result = [i for i in functions_black_list if i in value]
            if result:
                list_lines.append(
                    (file_name, line, value,)
                )

    return list_lines


def main():
    """ Main functions handling configuration files etc"""
    parser = argparse.ArgumentParser(description='Process validation file.')
    parser.add_argument('file', help='file to validation')
    args = parser.parse_args()
    result = check_file_validator(file_name=args.file)
    if result:
        print('Se encontraron los siguientes Errores')
        for error in result:
            print('file: {0} line: {1} codigo: {2}'.format(error[0],
                                                           error[1],
                                                           error[2]))
        message = ('If you are sure you want to commit',
                   'those files,',
                   'use --no-verify option',)
        print(' '.join(message))
        sys.exit(1)

if __name__ == '__main__':
    main()
    sys.exit(0)

sys.exit(1)
