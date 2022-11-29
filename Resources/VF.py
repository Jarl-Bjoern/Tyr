#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.HF import *

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
