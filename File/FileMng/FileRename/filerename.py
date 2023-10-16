#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *

def FileRename():
    global Rename_File_Path,Old_file_Path,evet_hayır
    Rename_File_Path=str(input('Yeni Program Yolu: '))
    Old_file_Path=str(input('Eski Program Yolu: '))
    evet_hayır=str(input('{0} Değişkenini {1} Değişkeni İle Yeniden Adlandırma Yapmak Istediginizden Emin Misiniz? (E / H): '.format(Old_file_Path,Rename_File_Path)))
    file_path[Rename_File_Path] = file_path.pop(Old_file_Path)