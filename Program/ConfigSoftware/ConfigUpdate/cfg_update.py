#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import time, os

def cfg_update_():
    global cfg_update_software_name,software_addr_type,software_addr,cfgpt_f,web_cfgpt_f
    cfgpt_f=str("/blob/main/software.cfgpt")
    web_cfgpt_f=str("/{0}/software.cfgpt". format(cfg_update_software_name))
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
    elif software_addr_type=="web_site" or software_addr_type=="Web Site" or software_addr_type=="web site":
        software_addr==input('Software Address (https://website_name.domain/software_folder/software.cfgpt):  ')
        time.sleep(2)
        if f_ext_web_cfgpt!="-1":
            print("")

def f_ext_cfgpt():
    global file,read_word,read_if
    file = open("{0}". format(software_addr+cfgpt_f), "r")
    read_word=str("cfg_update_status=0")
    read_if = file.read().find(read_word)
    file.close()

def f_ext_web_cfgpt():
    global file_,read_word_,read_if_
    file_ = open("{0}". format(software_addr+web_cfgpt_f))
    read_word_=str("cfg_update_status=0")
    read_if_ = file.read().find(read_word_)
    file_.close()