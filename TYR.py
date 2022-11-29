#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Author
__author__ = "Rainer C. B. Herold"
__copyright__ = "Copyright 2022, Rainer C. B. Herold"
__credits__ = "Rainer C. B. Herold"
__license__ = "MIT license"
__version__ = "0.1"
__maintainer__ = "Rainer C. B. Herold"
__status__ = "Production"

# Libraries
try:
    from argparse import ArgumentParser, FileType, RawTextHelpFormatter, SUPPRESS
    from numpy import array
    from sys import argv
    from time import sleep
    import webbrowser
except ModuleNotFoundError as e: input(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'"), exit()

# Functions
def Stdout_Output(Text_Array):
    for char in Text_Array:
        stdout.write(char)
        stdout.flush()
        sleep(0.01)

def Initialien():
    class Colors:
        GREEN = '\033[32m'
        ORANGE = '\033[33m'
        BLUE = '\033[34m'
        UNDERLINE = '\033[4m'
        RESET = '\033[0m'

    if (osname == 'nt'): system('cls')
    else: system('clear')
    Header = """
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
💀\t\t\t\t\t\t\t\t💀
💀\t\t      """+Colors.UNDERLINE+"Tyr"+Colors.RESET+ """\t\t\t💀
💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.BLUE+"0.1"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t\t\t\t\t\t💀
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
"""
    Stdout_Output(Header)

# Main
if __name__ == '__main__':
    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter)
    optional = parser.add_argument_group('optional arguments')
    optional.add_argument('-t','--time', type=float, default=0.65, help='This parameter specify the seconds between the next tab\n\nDefault: 0.65 Seconds\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-mt','--max-tabs', type=int, default=100, help='This parameter specify the max open tabs\n\nDefault: 100\n\n-------------------------------------------------------------------------------------')
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help='Show this help message and exit.\n\n-------------------------------------------------------------------------------------')
    args = parser.parse_args()

    Open_URL(args.max_tabs, args.time)
#    Parameters = ""
#    for Arg_Name, Arg_Value in vars(args).items():
#        elif ((Arg_Name == "path" and Arg_Value != None) or (Arg_Name == "host_name" and Arg_Value != None)): Parameters += f"{Arg_Value} "
