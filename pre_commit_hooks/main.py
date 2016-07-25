#!/usr/bin/env python

"""
Git pre-commit hook for checking code php instructions

Author:
    Luis Alberto Mayta

"""
from __future__ import print_function
import argparse
import sys

WARNING_MSG = 'File {0} line: {1} codigo: {2}'

FUNCTIONS_BLACK_LIST = (
    'eval',
    'var_dump',
    'print_r',
)


def detect_function_not_allowed(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retcode = 0

    for filename in args.filenames:
        with open(filename, 'rb') as inputfile:
            for line, value in enumerate(inputfile):
                result = [i for i in FUNCTIONS_BLACK_LIST if i in value]
                if result:
                    print(WARNING_MSG.format(
                        inputfile, line, value,
                    ))
                    retcode = 1
    return retcode


if __name__ == '__main__':
    sys.exit(detect_function_not_allowed())
