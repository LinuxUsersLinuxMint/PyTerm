#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *

def VarRename():
    global Rename_var_Path,Old_var_Path,evet_hayır
    Rename_var_Path=str(input('Yeni Program Değişkeni: '))
    Old_var_Path=str(input('Eski Program Değişkeni: '))
    evet_hayır=str(input('{0} Değişkenini {1} Değişkeni İle Yeniden Adlandırma Yapmak Istediginizden Emin Misiniz? (E / H): '.format(Old_var_Path,Rename_var_Path)))
    file_path["{0}". format(Rename_var_Path)]
    del file_path["{0}". format(Old_var_Path)]