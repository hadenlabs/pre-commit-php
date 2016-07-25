from setuptools import find_packages, setup
from pre_commit_hooks import VERSION

setup(
    name='pre_commit_php',
    description='Some out-of-the-box hooks for pre-commit.',
    url='https://github.com/hadenlabs/pre-commit-php',
    version='.'.join(map(str, VERSION)),
    author='Luis Alberto Mayta',
    author_email='slovacus@gmail.com',

    platforms='linux',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],

    packages=find_packages('.', exclude=('tests*', 'testing*')),
    install_requires=[
        # quickfix to prevent pep8 conflicts
        'flake8!=2.5.3',
        'argparse',
        'autopep8>=1.1',
        'pyyaml',
        'simplejson',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'check-function-notallowed = pre_commit_hooks.main:detect_function_not_allowed',
        ],
    },
)
