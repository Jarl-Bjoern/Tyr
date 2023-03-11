#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Variables import *

# Functions
def main(args):
    Standard.Initialien()

    PID = Process_ID("firefox")
    if (PID != None):
        input(Colors.ORANGE+"An already open Firefox instance has been located, it is advised\n\t\tto close it to avoid errors.\n\n      The instance will be closed with the "+Colors.CYAN+"'Return'"+Colors.ORANGE+" button.\n\n"+Colors.RESET)
        kill(PID, SIGKILL), sleep(1.25)
    Open_URL(args.import_list, args.max_tabs, args.time)

# Main
if __name__ == '__main__':    
    try: main(args)
    except KeyboardInterrupt: exit()
