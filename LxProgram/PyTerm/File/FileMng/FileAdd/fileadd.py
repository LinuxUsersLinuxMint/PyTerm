#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *
def FileAdd():
  global Add_file_Path,Add_File_var
  Add_file_Path=str(input('Program Path You Want to Add: '))
  Add_File_var=str(input('In Which Variable Should the Program You Want to Add Be Stored (path_example): '))
  file_path["{0}". format(Add_file_Path)] = ("{0}". format(Add_File_var))