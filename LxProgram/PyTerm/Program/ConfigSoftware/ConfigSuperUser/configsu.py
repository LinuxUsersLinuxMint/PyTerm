#!/usr/bin/python3

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