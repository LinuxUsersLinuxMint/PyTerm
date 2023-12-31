#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

#  Warning: RunProgram.py and RunProgram() function are in beta version. Please read the necessary warnings and instructions before use.

import os, time

def beta_runprogram():
   program_opt = str(input('Will you start the program with path or program variable?'))

   if program_opt=="path" or program_opt=="PATH" or program_opt=="Path":
        beta_runprogram_path = str(input('Program path to be run (example: LxProgram/PyTerm/PyTerm): '))
        time.sleep(3)
        os.system("./{0}". format(beta_runprogram_path))
   elif program_opt=="Program_var" or program_opt=="var" or program_opt=="Program_variable":
        beta_runprogram = str(input("Program variable to be run (example: path_programname) : "))
        time.sleep(2)
        os.system("./{0}". format(beta_runprogram))
   else:
        print("Invalid RunProgram Argument...")