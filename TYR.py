#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.VF import *

# Main
if __name__ == '__main__':
    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    required = parser.add_argument_group('required arguments')
    required.add_argument('-iL','--import-list', type=str, required=True, help='This parameter specify your targetlist\n\nYour list must look like in this example:\n  - http://192.168.2.1\n  - https://192.168.2.2:8443\n  - http://tomcat-test:8080\n\n-------------------------------------------------------------------------------------')
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-t','--time', type=float, default=0.65, help='This parameter specify the seconds between the next tab\n\nDefault: 0.65 Seconds\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-mt','--max-tabs', type=int, default=100, help='This parameter specify the max open tabs\n\nDefault: 100\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help='Show this help message and exit.\n\n-------------------------------------------------------------------------------------')
    args = parser.parse_args()

    
    Initialien(), Open_URL(args.import_list ,args.max_tabs, args.time)
