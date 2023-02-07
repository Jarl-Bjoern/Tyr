#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Standard_Operations.Libraries import *
from Resources.Standard_Operations.Colors import Colors
from Resources.Standard_Operations.Standard import Standard

# Functions
def Process_ID(Process_Name):
    for P in process_iter():
        if (Process_Name in P.name()):
            return P.pid

def Open_URL(TEXT_FILE, MAX_COUNT, SLEEP_SECONDS, Counter = 0):
    with open(TEXT_FILE, 'r') as f:
        for URL in f.read().splitlines():
            if ('http' not in URL): browser_open(f'http://{URL}', new=0)
            else: browser_open(URL, new=0)
            Counter += 1
            sleep(SLEEP_SECONDS)
            if (Counter == MAX_COUNT):
                input(f'\nThe maximum number {MAX_COUNT} of open tabs has been reached\n\nYou can continue with the "Enter" key\n\nWith the key combination "CTRL" + "F4" you can close open tabs faster')
                Counter = 0
        print(Colors.ORANGE+"All available URLs were opened! :)"+Colors.RESET)
