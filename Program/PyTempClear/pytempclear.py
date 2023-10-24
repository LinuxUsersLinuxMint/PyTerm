#!/usr/bin/python3

import os
import time
from File.filePath.filePath import *

def PyTempClear():
    os.system("cd {0}". format(ProgramFilePath))
    time.sleep(2)
    os.system()
    for i in file_path:
        os.system("rm -rf {0}". format(i)) # Geçici bir süreliğine kod böyle bırakılmıştır.
        # The code has been left like this temporarily.
        # kodu çalıştırmayınız ve çalıştırmayı denemeyiniz. (Sorumluluk LinuxUsersLinuxMint de değildir.)
        # Do not run or try to run the code. (Not the responsibility of LinuxUsersLinuxMint.)