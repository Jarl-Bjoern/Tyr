#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.HF import *

# Classes
class Colors:
    CYAN = '\033[36m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    RED = '\033[31m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

# Variables
Program_Description = """-------------------------------------------------------------------------------------
|  Created by Rainer Christian Bjoern Herold                                        |
|  Copyright 2022-2023. All rights reserved.                                        |
|                                                                                   |
|  Please do not use the program for illegal activities.                            |
|                                                                                   |
|  If you got any problems don't hesitate to contact me so I can try to fix them.   |
-------------------------------------------------------------------------------------
"""

# Functions
def Stdout_Output(Text_Array):
    for char in Text_Array:
        stdout.write(char)
        stdout.flush()
        sleep(0.01)

def Initialien():
    if (osname == 'nt'): system('cls')
    else: system('clear')
    Header = """💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
💀\t\t\t\t\t\t\t\t💀
💀\t\t              """+Colors.UNDERLINE+"TYR"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.CYAN+"0.1"+Colors.RESET+"""\t\t\t\t💀
💀\t\tRainer Christian Bjoern Herold\t\t\t💀
💀\t\t\t\t\t\t\t\t💀
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
"""
    Stdout_Output(Header)

def Open_URL(TEXT_FILE, MAX_COUNT, SLEEP_SECONDS, Counter = 0):
    with open(TEXT_FILE, 'r') as f:
        for URL in f.read().splitlines():
            if ('http' not in URL): browser_open(f'http://{URL}')
            else: browser_open(URL)
            Counter += 1
            sleep(SLEEP_SECONDS)
            if (Counter == MAX_COUNT):
                input(f'\nThe maximum number {MAX_COUNT} of open tabs has been reached\n\nYou can continue with the "Enter" key\n\nWith the key combination "CTRL" + "F4" you can close open tabs faster')
                Counter = 0
        print(Colors.ORANGE+"All available URLs were opened! :)"+Colors.RESET)
