#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "???"

import argparse
import sys


def create_parser():
    parser = argparse.ArgumentParser("Perform transformation on input text")
    parser.add_argument('-u', '--upper', action='store_true', help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action='store_true', help='convert text to lowercase')
    parser.add_argument('-t', '--title', action='store_true', help='convert text to titlecase')
    parser.add_argument('text', help="text to be manipulated")

    return parser


def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    result = ns.text
    if ns.upper:
        result = result.upper()
    if ns.lower:
        result = result.lower()
    if ns.title:
        result = result.title()
    return result


if __name__ == '__main__':
    main(sys.argv[1:])
