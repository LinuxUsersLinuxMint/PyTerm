#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *
import time

def VarRename():
    global Rename_var_Path,Old_var_Path,yes_no
    Rename_var_Path=str(input('Yeni Program Değişkeni: '))
    Old_var_Path=str(input('Eski Program Değişkeni: '))
    yes_no=str(input('{0} Değişkenini {1} Değişkeni İle Yeniden Adlandırma Yapmak Istediginizden Emin Misiniz? (Y / N): '.format(Old_var_Path,Rename_var_Path)))
    if yes_no=="Y" or yes_no=="Yes" or yes_no=="y" or yes_no=="yes":
        time.sleep(2)
        file_path("{0}". format(Rename_var_Path))
        del file_path("{0}". format(Old_var_Path))
    elif yes_no=="N" or yes_no=="No" or yes_no=="n" or yes_no=="no":
        exit()
    else:
        print("Invalid Command...!")