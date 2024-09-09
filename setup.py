#!/usr/bin/env python

from distutils.core import setup

LONG_DESCRIPTION = \
'''The program reads one or more input FASTA files.
For each file it computes a variety of statistics, and then
prints a summary of the statistics as output.

The goal is to provide a solid foundation for new bioinformatics command line tools,
and is an ideal starting place for new projects.'''


setup(
    name='AGI_demo',
    version='0.1.0.0',
    author='Andy Bachler',
    author_email='andy.bachler@csiro.au',
    packages=['AGI_demo'],
    package_dir={'AGI_demo': 'AGI_demo'},
    entry_points={
        'console_scripts': ['AGI_demo = AGI_demo.AGI_demo:main']
    },
    url='https://github.com/Andy-B-123/AGI_demo',
    license='LICENSE',
    description=('A prototypical bioinformatics command line tool'),
    long_description=(LONG_DESCRIPTION),
    install_requires=["biopython"],
)
