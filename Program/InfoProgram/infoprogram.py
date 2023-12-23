#!/usr/bin/python3
""" Copyright© 2023 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from File.filePath.filePath import *
from InfoProject.info import *
import time

def InfoProgram():
    global select
    select=str(input('Enter the program you want to see info about: '))
    if select=="info":
        print("[PyTerm]: Program Info...")
        time.sleep(2)
        print("Program Name: {0}". format(name))
        print("Program Version: {0}". format(ver))
        print("Program Type: {0}". format(ver_type))
        print("Program About: {0}". format(about))
        print("Program Help Directory: {0}". format(hlp))
        print("Program Help Website: {0}". format(hlp_website))
        print("Program Author: {0}". format(author))
        print("Program Author Website: {0}". format(authorwebsite))
        time.sleep(2)
        print("[PyTerm]: Program Info Completed...")
    elif select=="exit":
        exit()
    else:
        print("Invalid command...!")