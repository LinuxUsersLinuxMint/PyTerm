#!/usr/bin/python3
""" Copyright© 2023-2024 LinuxUsersLinuxMint
PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
PyTerm All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint """

import time, os

yes_no=str(input('Are you sure you want to install PyTerm? (Y / N / Uninstall): '))

if yes_no=="N" or yes_no=="n" or yes_no=="No" or yes_no=="no" or yes_no=="NO":
    exit()
elif yes_no=="Y" or yes_no=="y" or yes_no=="Yes" or yes_no=="yes" or yes_no=="YES":
    print("Installing PyTerm...")
    time.sleep(3)
    os.system("./install_runpyterm.sh") # PyTerm Shortcut Install
    print("[PyTerm_Setup_Environment]: PyTerm installation step 1/3...")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: setup_create_dir.sh step 1/3... (Create Folder)")
    time.sleep(3)
    os.system("./setup_create_dir.sh")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: PyTerm installation step completed...")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: PyTerm installation step 2/3...")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: setup_copy_files.sh step 2/3... (Copy Files)")
    time.sleep(3)
    os.system("./setup_copy_files.sh")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: PyTerm installation step completed...")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: PyTerm installation step 3/3...")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: setup_folder_copy.sh step 3/3... (Copy Folder)")
    time.sleep(3)
    os.system("./setup_folder_copy.sh")
    time.sleep(3)
    print("[PyTerm_Setup_Environment]: PyTerm installation step completed...")
    exit()
elif yes_no=="Uninstall" or yes_no=="uninstall" or yes_no=="U" or yes_no=="u":
    print("Uninstall PyTerm...")
    time.sleep(3)
    os.system("./uninstall_pyterm.sh")
    time.sleep(2)
    exit()
else:
    print("Invalid PSE (Python Setup Environment) Argument...")