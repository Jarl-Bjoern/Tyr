#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Variables import *

# Functions
def main(args):
    Standard.Initialien()

    # Target_Options
    if (args.target == None and args.import_list == None and args.add_nmap_xml_result == None):
        from Resources.Header_Files.ArgParser_Scan_Intro import Argument_Parser
        Argument_Parser("\n\n\t\t\t   The program cannot be started without targets!\n\t\t\tFor more information use the parameter -h or --help.\n"), exit()
    elif (args.target == None and (args.import_list != None or args.add_nmap_xml_result != None)):
        if (args.import_list != None):
            try:
                Array_Targets = Standard.Read_Targets_v4(args.import_list)
            except FileNotFoundError as e:
                print(f"Your targetlist can't be found!\n\n{args.import_list}")

        if (args.add_nmap_xml_result != None):
            try:
                Array_Temp_Zero = Standard.Read_Targets_XML(args.add_nmap_xml_result)
                if (len(Array_Targets) > 0):
                    for _ in array(Array_Temp_Zero):
                        if (_ not in Array_Targets):
                            Array_Targets.append(_)
                else:
                    Array_Targets = Array_Temp_Zero

            except FileNotFoundError as e:
                Logs.Error_Message(f"Your targetlist can't be found!\n\n{args.add_nmap_xml_result}")
    else:
        if (len(args.target) > 1):
            Array_Targets = []
            for _ in args.target:
                if (',' in _):
                    Array_Targets.append(_[:-1])
                else:
                    Array_Targets.append(_)
        else:
            if (',' in args.target[0]):
                Temp_Split = args.target[0].split(',')
                for _ in Temp_Split:
                    if (_ != ''): Array_Targets.append(_)
            else: Array_Targets = [args.target[0]]
    if (args.random_order == True):
        try: from random import shuffle
        except ModuleNotFoundError as e: Module_Error(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'")
        shuffle(Array_Targets)
        del shuffle

    # Process_Kill
    PID = Process_ID("firefox")
    if (PID != None):
        input(Colors.ORANGE+"An already open Firefox instance has been located, it is advised\n\t\tto close it to avoid errors.\n\n      The instance will be closed with the "+Colors.CYAN+"'Return'"+Colors.ORANGE+" button.\n\n"+Colors.RESET)
        kill(PID, SIGKILL), sleep(1.25)

    # Main_Process
    Open_URL(Array_Targets, args.max_tabs, args.time)

# Main
if __name__ == '__main__':    
    try: main(args)
    except KeyboardInterrupt: exit()
