#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from File.filePath.filePath import *
import time

def VarRename():
    global Rename_var_Path,Old_var_Path,yes_no
    Rename_var_Path=str(input('New Program Variable: '))
    Old_var_Path=str(input('Old Program Variable: '))
    yes_no=str(input('Are You Sure You Want to Rename Variable {0} to Variable {1}? (Y / N): '. format(Old_var_Path,Rename_var_Path)))
    if yes_no=="Y" or yes_no=="Yes" or yes_no=="y" or yes_no=="yes":
        file_path["{0}". format(Rename_var_Path)]
        time.sleep(2)
        del file_path["{0}". format(Old_var_Path)]
    elif yes_no=="N" or yes_no=="No" or yes_no=="n" or yes_no=="no":
        exit()
    else:
        print("Invalid Command...!")