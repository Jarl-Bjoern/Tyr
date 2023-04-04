#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from .Libraries import *
from ..Standard_Operations.Colors import Colors
from ..Standard_Operations.Standard import Standard

# Dictionaries
Dict_State = {
    "State": [],
    "Location": dirname(realpath(__file__)).split('Resources/Header_Files')[0]
}

# Functions
def Process_ID(Process_Name):
    for P in process_iter():
        if (Process_Name in P.name()):
            return P.pid

def Open_URL(Array_Targets, MAX_COUNT, SLEEP_SECONDS, Counter = 0):
    for URL in Array_Targets:
        browser_open(URL, new=0)
        if (URL not in Dict_State['State']):
            Dict_State['State'].append(URL)
        Counter += 1
        sleep(SLEEP_SECONDS)
        if (Counter == MAX_COUNT):
            input(Colors.ORANGE+'\n\tThe maximum number '+Colors.RED+f'{MAX_COUNT}'+Colors.ORANGE+' of open tabs has been reached!\n\n\t   You can continue with the '+Colors.CYAN+'"Return"'+Colors.ORANGE+' key.\n\nWith the key combination '+Colors.CYAN+'"CTRL" + "F4"'+Colors.ORANGE+' you can close open tabs faster'+Colors.RESET)
            Counter = 0
            Standard.Print_Header()
    print(Colors.ORANGE+"All available URLs were opened! :)"+Colors.RESET)
