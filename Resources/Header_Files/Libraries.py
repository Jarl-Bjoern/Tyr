#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Author
__author__ = "Rainer C. B. Herold"
__copyright__ = "Copyright 2022-2023, Rainer C. B. Herold"
__credits__ = "Rainer C. B. Herold"
__license__ = "MIT license"
__version__ = "0.2"
__maintainer__ = "Rainer C. B. Herold"
__status__ = "Production"

# Libraries
try:
    from os import kill, name as osname, remove, system
    from os.path import dirname, exists, join, realpath
    from psutil import process_iter
    from signal import SIGKILL
    from sys import stdout
    from time import sleep
    from webbrowser import open as browser_open
    from xml.etree.ElementTree import ParseError
    import xml.etree.ElementTree as ET
except ModuleNotFoundError as e: input(f"The module was not found\n\n{e}\n\nPlease confirm with the button 'Return'"), exit()

# Argument_Parser
from .ArgParser import Argument_Parser
args = Argument_Parser()

# Delete_Unused_Functions
del Argument_Parser
