#!/usr/bin/python3
""" Copyright© 2023 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import os



def cfg_super_user_():
    global cfg_super_usr_status,cfg_super_usr_com
    cfg_super_usr_status=int()
    cfg_super_usr_com=str()
    if f_ext_cfgpt_su!="-1":
        os.system("sudo su")
        exit()
    else:
        exit()

def f_ext_cfgpt_su():
    global file,read_word,read_if
    file = open("https://github.com/LinuxUsersLinuxMint/PyTerm/blob/main/software.cfgpt", "r")
    read_word=str("cfg_super_usr_status=0")
    read_if = file.read().find(read_word)
    file.close()