#!/usr/bin/python3
# Copyright© 2023 LinuxUsersLinuxMint
# PyTerm Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# PyTerm All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint

import os, time

def RecoveryMode(inputRecoveryDialog):
    global select_rp
    print("----- Recovery Mode -----")
    print("\n 1. Reinstall PyTerm")
    print("\n 2. Edit CFGPT (ConfigPyTerm) Setting (Not Working)")
    print("\n 3. Exit Recovery Mode")
    select_rp=str(input('{0}'. format(inputRecoveryDialog)))
    if select_rp=="1":
        PyTermInstall()
    elif select_rp=="2":
        EditCfgpt()
    elif select_rp=="3":
        RecoveryModeExit("Exit Recovery Mode: ")

def RecoveryModeExit(exitDialog):
    global select_ext
    print("----- Exit Recovery Mode -----")
    print("\n 1. Exit")
    print("\n 2. Return to Recovery Mode")
    select_ext=str(input('{0}'. format(exitDialog)))
    if select_ext=="1":
        print("Recovery mode exit...")
        time.sleep(2)
        exit()
    elif select_ext=="2":
        RecoveryMode("Enter select: ")

def EditCfgpt():
    # (Not Working)
    print("Not Working...")

def ReinstallPyTerm(inputDialog):
    global select_vr
    print("----- Reinstall PyTerm -----")
    print("\n 1. PyTerm Stable Beta")
    print("\n 2. PyTerm BETA_3")
    print("\n 3. PyTerm BETA_2_3")
    print("\n 4. PyTerm BETA_2_2")
    print("\n 5. PyTerm BETA_2_1")
    print("\n 6. PyTerm BETA_2")
    print("\n 7. PyTerm BETA_1")
    print("\n 8. PyTerm BETA")
    select_vr=str(input('{0}'. format(inputDialog)))

def PyTermInstall(select_vr):
    if select_vr=="1":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermStableBeta.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermStableBeta.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermStableBeta/setup_py.py")
    elif select_vr=="2":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta3.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta3.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta3/setup_py.py")
    elif select_vr=="3":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta2_3.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta2_3.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta2_3/setup_py.py")
    elif select_vr=="4":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta2_2.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta2_2.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta2_2/setup_py.py")
    elif select_vr=="5":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta2_1.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta2_1.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta2_1/setup_py.py")
    elif select_vr=="6":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta2.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta2.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta2/setup_py.py")
    elif select_vr=="7":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta1.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta1.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta1/setup_py.py")
    elif select_vr=="8":
        os.system("wget https://github.com/LinuxUsersLinuxMint/PyTerm/archive/refs/tags/PyTermBeta.zip")
        time.sleep(5)
        os.system("unzip PyTerm-PyTermBeta.zip")
        time.sleep(2)
        os.system("./PyTerm-PyTermBeta/setup_py.py")
    else:
        print("Invalid PyTerm Version...")