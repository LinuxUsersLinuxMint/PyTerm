#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
from File.filePath.filePath import *

def FileRemove():
  global Remove_file_Path,Remove_File_var,evet_hayır
  Remove_file_Path=str(input('Silmek İstediğiniz Program Yolu: '))
  Remove_File_var=str(input('Silmek İstediğiniz Program Değişkeni: '))
  evet_hayır=str(input('{0} Yolunu Ve {1} Değişkenini Silmek İstediğinizden Emin Misiniz? (E / H): '.format(Remove_file_Path,Remove_File_var)))
  if evet_hayır=="H":
    exit()
  elif evet_hayır=="E":
    del file_path["{0}". format(Remove_file_Path)]
    del file_path["{0}". format(Remove_File_var)]