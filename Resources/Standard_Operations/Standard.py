#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from .Colors import Colors
from ..Header_Files.Libraries import dirname, exists, ET, join, osname, realpath, sleep, stdout, system

class Standard:
    def Stdout_Output(Text_Array):
        for char in Text_Array:
            stdout.write(char)
            stdout.flush()
            sleep(0.01)

    def Print_Header():
        Header = """💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
💀\t\t\t\t\t\t\t\t💀
💀\t\t              """+Colors.UNDERLINE+"TYR"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.BLUE+"0.2"+Colors.RESET+"""\t\t\t\t💀
💀\t\t"""+Colors.CYAN+"Rainer Christian Bjoern Herold"+Colors.RESET+"""\t\t\t💀
💀\t\t\t\t\t\t\t\t💀
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
"""
        if (osname == "nt"): system('cls')
        else:                system('clear')
        print(Header)

    def Initialien():
        if (osname == 'nt'): system('cls')
        else: system('clear')
        Header = """💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
💀\t\t\t\t\t\t\t\t💀
💀\t\t              """+Colors.UNDERLINE+"TYR"+Colors.RESET+"""\t\t\t\t💀
💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.BLUE+"0.2"+Colors.RESET+"""\t\t\t\t💀
💀\t\t"""+Colors.CYAN+"Rainer Christian Bjoern Herold"+Colors.RESET+"""\t\t\t💀
💀\t\t\t\t\t\t\t\t💀
💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
"""
        Standard.Stdout_Output(Header)

    def Read_Targets_XML(file_path, Array_Out = [], Array_Template = []):
        if (exists(join(dirname(realpath(__file__)).split("Resources/Standard_Operations")[0], "scan.state"))):
            with open(join(dirname(realpath(__file__)).split("Resources/Standard_Operations")[0], "scan.state"), 'r') as f:
                Array_Template = f.read().splitlines()

        Protocol, Address, Port, Skip_Attributes = "","","",False
        for event, elem in ET.iterparse(file_path, events=("end",)):
            if (event == "end"):
                if (elem.tag == 'address'):
                    if (Skip_Attributes != True):
                        Address = elem.attrib['addr']
                elif (elem.tag == 'state'):
                    if (elem.attrib['state'] != "open"):
                        Skip_Attributes = True
                elif (elem.tag == 'service'):
                    if (Skip_Attributes != True):
                        if ('http' in elem.attrib['name'] and not 'ssl' in elem.attrib['name'] and not 'https' in elem.attrib['name']):
                            Protocol = "http"
                        elif ('https' in elem.attrib['name'] or ('http' in elem.attrib['name'] and 'ssl' in elem.attrib['name'])):
                            Protocol = "https"
                elif (elem.tag == 'port'):
                    if (Skip_Attributes != True):
                        Port = elem.attrib['portid']
                    if (Protocol != "" and Address != "" and Port != ""):
                        Full_Target = f'{Protocol}://{Address}:{Port}'
                        Protocol, Address, Port = "","",""

                        if ('https://' in Full_Target or 'http://' in Full_Target):
                            if (Full_Target not in Array_Out):
                                if (Full_Target not in Array_Template):
                                    Array_Out.append(Full_Target)

                        Full_Target = ""

                    Skip_Attributes = False

        return Array_Out

    def Read_Targets(Input_File, Array_Out = [], Array_Template = []):
        if (exists(join(dirname(realpath(__file__)).split("Resources/Standard_Operations")[0], "scan.state"))):
            with open(join(dirname(realpath(__file__)).split("Resources/Standard_Operations")[0], "scan.state"), 'r') as f:
                Array_Template = f.read().splitlines()

        with open(Input_File, 'r') as f:
            Array_Temp_Targets = f.read().splitlines()

        for i in Array_Temp_Targets:
            if (i not in Array_Out):
                if (i not in Array_Template):
                    Array_Out.append(i)

        return Array_Out

    def Write_State_File(Array_State, Location):
        with open(join(Location, 'scan.state'), 'w') as f:
            for _ in Array_State:
                f.write(f'{_}\n')
