"""Deephyper analytics - single study documentation

usage:

::

    $ deephyper-analytics parse ppo_test/ppo_test_382DS/deephyper.log
    $ deephyper-analytics single ppo_test_2019-05-07_14.json

"""

import os
import argparse
from deephyper.core.plot.jn_loader import NbEdit

HERE = os.path.dirname(os.path.abspath(__file__))


def single_analytics(path_to_data_file):
    editor = NbEdit(os.path.join(HERE, 'stub/single_analytics.ipynb'))

    editor.edit(0, "{{path_to_data_file}}", path_to_data_file)

    editor.edit(1, "{{path_to_data_file}}", f"'{path_to_data_file}'")

    editor.write()

    editor.execute()


def add_subparser(subparsers):
    subparser_name = 'single'
    function_to_call = main

    parser_parse = subparsers.add_parser(
        subparser_name, help='Tool to generate analytics on a single NAS experiment (jupyter notebook).')
    parser_parse.add_argument(
        'path', type=str, help=f'A Json file generated with "deephyper-analytics parse".')

    return subparser_name, function_to_call


def main(path, *args, **kwargs):
    single_analytics(path_to_data_file=path)
