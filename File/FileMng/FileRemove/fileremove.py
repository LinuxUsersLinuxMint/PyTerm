#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *
import time

def FileRemove():
  global Remove_file_Path,Remove_File_var,yes_no
  Remove_file_Path=str(input('Silmek İstediğiniz Program Yolu: '))
  Remove_File_var=str(input('Silmek İstediğiniz Program Değişkeni: '))
  yes_no=str(input('{0} Yolunu Ve {1} Değişkenini Silmek İstediğinizden Emin Misiniz? (Y / N): '.format(Remove_file_Path,Remove_File_var)))
  if yes_no=="Y":
    exit()
  elif yes_no=="N":
    time.sleep(2)
    del file_path["{0}". format(Remove_file_Path)]
    del file_path["{0}". format(Remove_File_var)]
  else:
    print("Invalid Command...!")