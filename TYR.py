#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resource.VF import *

# Main
if __name__ == '__main__':
    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-t','--time', type=float, default=0.65, help='This parameter specify the seconds between the next tab\n\nDefault: 0.65 Seconds\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-mt','--max-tabs', type=int, default=100, help='This parameter specify the max open tabs\n\nDefault: 100\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help='Show this help message and exit.\n\n-------------------------------------------------------------------------------------')
    args = parser.parse_args()

    Open_URL(args.max_tabs, args.time)
