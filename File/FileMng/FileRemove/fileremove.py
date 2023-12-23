#!/usr/bin/python3
""" Copyright© 2023 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

from File.filePath.filePath import *
import time

def FileRemove():
  global Remove_file_Path,Remove_File_var,yes_no
  Remove_file_Path=str(input('Program Path You Want to Delete: '))
  Remove_File_var=str(input('Program Variable You Want to Delete: '))
  yes_no=str(input('Are You Sure You Want to Delete Path {0} and Variable {1}? (Y / N): '.format(Remove_file_Path,Remove_File_var)))
  if yes_no=="N":
    exit()
  elif yes_no=="Y":
    time.sleep(2)
    del file_path["{0}". format(Remove_file_Path)]
    time.sleep(1)
    del file_path["{0}". format(Remove_File_var)]
  else:
    print("Invalid Command...!")