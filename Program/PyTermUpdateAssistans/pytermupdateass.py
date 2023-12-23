#!/usr/bin/python3
""" Copyright© 2023 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import os, time

def PyTermUpdateAssistans():
    pyterm_up_ass = str(input('Update PyTerm? (Y / N): '))
    if pyterm_up_ass=="Y" or pyterm_up_ass=="y" or pyterm_up_ass=="YES" or pyterm_up_ass=="yes" or pyterm_up_ass=="Yes":
        os.system("git clone https://github.com/LinuxUsersLinuxMint/PyTerm")
        time.sleep(5)
        os.system("./PyTerm-main/setup_py.py")
    elif pyterm_up_ass=="N" or pyterm_up_ass=="n" or pyterm_up_ass=="NO" or pyterm_up_ass=="no" or pyterm_up_ass=="No":
        exit()
    else:
        print("Invalid PyTermUpdateAssistans Argument...")