#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Header_Files.Variables import *

# Functions
def main(args, Array_Targets = []):
    # Target_Options
    if (args.target == None and args.import_list == None and args.add_nmap_xml_result == None):
        from Resources.Header_Files.ArgParser_Intro import Argument_Parser
        Argument_Parser("\n\n\t\t\t   The program cannot be started without targets!\n\t\t\tFor more information use the parameter -h or --help.\n"), exit()
    elif (args.target == None and (args.import_list != None or args.add_nmap_xml_result != None)):
        if (args.import_list != None):
            try:
                Array_Targets = Standard.Read_Targets(args.import_list)
            except FileNotFoundError as e:
                print(Colors.RED+f"\n\tYour targetlist can't be found!\n\n\t\t{args.import_list}"+Colors.RESET), exit()

        if (args.add_nmap_xml_result != None):
            try:
                Array_Temp_Zero = Standard.Read_Targets_XML(args.add_nmap_xml_result)
                if (len(Array_Targets) > 0):
                    for _ in Array_Temp_Zero:
                        if (_ not in Array_Targets):
                            Array_Targets.append(_)
                else:
                    Array_Targets = Array_Temp_Zero

            except FileNotFoundError as e:
                print(Colors.RED+f"\n\tYour targetlist can't be found!\n\n\t\t{args.add_nmap_xml_result}"+Colors.RESET), exit()
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
        except ModuleNotFoundError as e: input(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'"), exit()
        shuffle(Array_Targets)
        del shuffle

    # Program_Start
    Standard.Initialien()

    # Process_Kill
    PID = Process_ID("firefox")
    if (PID != None):
        input(Colors.ORANGE+"An already open Firefox instance has been located, it is advised\n\t\tto close it to avoid errors.\n\n      The instance will be closed with the "+Colors.CYAN+"'Return'"+Colors.ORANGE+" button.\n\n"+Colors.RESET)
        kill(PID, SIGKILL), sleep(1.25)

    # Remove_Old_State_File
    if (exists(join(dirname(realpath(__file__)), "scan.state"))):
        remove(join(dirname(realpath(__file__)), "scan.state"))

    # Main_Process
    Open_URL(Array_Targets, args.max_tabs, args.sleep)

# Main
if __name__ == '__main__':
    try:
        main(args)
    except KeyboardInterrupt:
        if (len(Dict_State['State']) > 0):
            Standard.Write_State_File(Dict_State['State'], Dict_State['Location'])
        exit()
