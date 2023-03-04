#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Standard_Operations.Colors import Colors
from Resources.Standard_Operations.Libraries import dirname, join, realpath

# Functions
def Argument_Parser(Template_Location = dirname(realpath(__file__)).replace('Resources/Header_Files', 'Templates')):
    from argparse import ArgumentParser, RawTextHelpFormatter, SUPPRESS

    Program_Description = """-------------------------------------------------------------------------------------
|  Created by Rainer Christian Bjoern Herold                                        |
|  Copyright 2022-2023. All rights reserved.                                        |
|                                                                                   |
|  Please do not use the program for illegal activities.                            |
|                                                                                   |
|  If you got any problems don't hesitate to contact me so I can try to fix them.   |
-------------------------------------------------------------------------------------
"""

    parser = ArgumentParser(add_help=False, formatter_class=RawTextHelpFormatter, description=Colors.ORANGE+Program_Description+Colors.RESET, usage=SUPPRESS)
    required = parser.add_argument_group(Colors.ORANGE+'required arguments'+Colors.RESET)
    optional = parser.add_argument_group(Colors.ORANGE+'optional arguments'+Colors.RESET)
    
    required.add_argument('-iL','--import-list', type=str, required=True, help=Colors.GREEN+'This parameter specify your targetlist\n\nYour list must look like in this example:'+Colors.RESET+'\n  - http://192.168.2.1\n  - https://192.168.2.2:8443\n  - http://tomcat-test:8080\n  - http://tomcat-test:8080/manager'+Colors.BLUE+'\n\n-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-t','--time', type=float, default=0.65, help=Colors.GREEN+'This parameter specify the seconds between the next tab\n\n'+Colors.RESET+'Default: 0.65 Seconds'+Colors.BLUE+'\n\n-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-mt','--max-tabs', type=int, default=100, help=Colors.GREEN+'This parameter specify the max open tabs\n\n'+Colors.RESET+'Default: 100'+Colors.BLUE+'\n\n-------------------------------------------------------------------------------------'+Colors.RESET)
    optional.add_argument('-h','--help', action='help', default=SUPPRESS, help=Colors.GREEN+'Show this help message and exit.'+Colors.BLUE+'\n\n-------------------------------------------------------------------------------------'+Colors.RESET)

    del ArgumentParser, RawTextHelpFormatter, SUPPRESS
    return parser.parse_args()
