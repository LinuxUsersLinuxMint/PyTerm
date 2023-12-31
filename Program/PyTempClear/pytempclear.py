#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import os
import time
from File.filePath.filePath import *

def PyTempClear():
    print("[PyTerm]: PyTemp Clear...")
    time.sleep(2)
    os.system("rm -rf File/FileMng/FileAdd/__pycache__")
    os.system("rm -rf File/FileMng/FileList/__pycache__")
    os.system("rm -rf File/FileMng/FileRemove/__pycache__")
    os.system("rm -rf File/FileMng/FileRename/__pycache__")
    os.system("rm -rf File/FileMng/VarRename/__pycache__")
    os.system("rm -rf File/filePath/__pycache__")
    os.system("rm -rf InfoProject/__pycache__")
    os.system("rm -rf Program/InfoProgram/__pycache__")
    os.system("rm -rf Program/PyTempClear/__pycache__")
    os.system("rm -rf Program/Compatibleos/__pycache__")
    os.system("rm -rf Program/ConfigSoftware/ConfigSuperUser/__pycache__")
    os.system("rm -rf Program/ConfigSoftware/ConfigUpdate/__pycache__")
    os.system("rm -rf Program/Help/__pycache__")
    os.system("rm -rf Program/PyTermUpdateAssistans/__pycache__")
    os.system("rm -rf Program/RunProgram/__pycache__")
    os.system("rm -rf File/FileMng/Filedictformat/__pycache__")
    time.sleep(2)
    print("[PyTerm]: PyTemp Clear Completed...") 