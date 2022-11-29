# Libraries
from HF import *

# Variables
MAX_COUNT, SLEEP_SECONDS = 100, 0.65

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

def Search(MAX_COUNT, SLEEP_SECONDS, Counter = 0):
    with open(argv[1], 'r') as f:
        for URL in f.read().splitlines():
        		if ('http' not in URL): webbrowser.open(f'http://{URL}')
        		else: webbrowser.open(URL)
        	Counter += 1
        	sleep(SLEEP_SECONDS)
        	if (Counter == MAX_COUNT):
        		input(f'\nThere are {100} tabs opened, please close all and confirm with Return to continue')
        		Counter = 0
