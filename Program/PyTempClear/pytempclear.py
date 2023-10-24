#!/usr/bin/python3

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
    time.sleep(2)
    print("[PyTerm]: PyTemp Clear Completed...") 