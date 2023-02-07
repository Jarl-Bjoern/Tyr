#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Rainer Christian Bjoern Herold

# Libraries
from Resources.Standard_Operations.Colors import Colors
from Resources.Standard_Operations.Libraries import osname, stdout, system

class Standard:
  def Stdout_Output(Text_Array):
      for char in Text_Array:
          stdout.write(char)
          stdout.flush()
          sleep(0.01)

  def Initialien():
      if (osname == 'nt'): system('cls')
      else: system('clear')
      Header = """💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀
  💀\t\t\t\t\t\t\t\t💀
  💀\t\t              """+Colors.UNDERLINE+"TYR"+Colors.RESET+"""\t\t\t\t💀
  💀\t\t\t  """+Colors.ORANGE+"Version "+Colors.CYAN+"0.1"+Colors.RESET+"""\t\t\t\t💀
  💀\t\tRainer Christian Bjoern Herold\t\t\t💀
  💀\t\t\t\t\t\t\t\t💀
  💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀💀\n\n
  """
      Stdout_Output(Header)
