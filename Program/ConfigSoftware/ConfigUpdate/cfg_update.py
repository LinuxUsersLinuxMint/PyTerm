#!/usr/bin/python3

import time, os

def cfg_update_():
    global cfg_update_software_name,software_addr_type,software_addr
    cfg_update_software_name=str()
    software_addr_type=str()
    software_addr=str()
    
    cfg_update_software_name=input('Update Software Name: ')
    software_addr_type=input('Software Address type (git/WebSite(not available)): ')
    
    if software_addr_type=="git" or software_addr_type=="Git":
        software_addr=input('Software Address (https://github.com/usr_name/repo_name): ')
        time.sleep(2)
        if f_ext_cfgpt!="-1":
            print("{0} Software Update...". format(cfg_update_software_name))
            time.sleep(2)
            os.system("git clone {0}". format(software_addr))
            time.sleep(2)
            print("{0} Software Updated...". format(cfg_update_software_name))
            exit()
        else:
            exit()

def f_ext_cfgpt():
    global file,read_word,read_if
    file = open("https://github.com/LinuxUsersLinuxMint/PyTerm/blob/main/software.cfgpt", "r")
    read_word=str("cfg_update_status=0")
    read_if = file.read().find(read_word)
    file.close()