#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *
import time

def file_dictf():
  global file_dict_yesno
  file_dict_yesno=str(input('Are you sure you want to reset the file_path dictionary?: '))
  if file_dict_yesno=="N":
    exit()
  elif file_dict_yesno=="Y":
    time.sleep(2)
    del file_path
    time.sleep(2)
    file_path=dict({})
  else:
    print("Invalid Command...!")