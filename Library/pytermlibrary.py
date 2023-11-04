#!/usr/bin/python

from File.filePath.filePath import *
from File.FileMng.FileAdd.fileadd import *
from File.FileMng.FileList.filelist import *
from File.FileMng.FileRemove.fileremove import *
from File.FileMng.FileRename.filerename import *
from File.FileMng.VarRename.varrename import *
from Program.InfoProgram.infoprogram import *
from Program.PyTempClear.pytempclear import *
from Program.PyTermUpdateAssistans.pytermupdateass import *
from Program.RunProgram.runprogram import *
from Program.Help.help import *
from Program.ConfigSoftware.ConfigSuperUser.configsu import *
from Program.ConfigSoftware.ConfigUpdate.cfg_update import *
from Program.Compatibleos.compatibleos import *
from File.FileMng.Filedictformat.filedictformat import *

def Software_lib_mng():
    global select_t
    select_t=str(input('Select _t: '))
    if select_t=="info":
        Info_lib()
    if select_t=="update_lib":
        pass

    def Info_lib():
        global py_term_lg
        py_term_lg=str("[PyTerm_lib_inf]:")
        print("{0} filePath [VER]: {1}". format(py_term_lg,"1.2"))
        print("{0} fileadd [VER]: {1}\n". format(py_term_lg,"1.1"))
        print("{0} filelist [VER]: {1}\n". format(py_term_lg,"0.3"))
        print("{0} fileremove [VER]: {1}\n". format(py_term_lg,"1.0"))
        print("{0} filerename [VER]: {1}\n". format(py_term_lg,"1.5"))
        print("{0} varrename [VER]: {1}\n". format(py_term_lg,"1.7"))
        print("{0} infoprogram [VER]: {1}\n". format(py_term_lg,"1.1"))
        print("{0} pytempclear [VER]: {1}\n". format(py_term_lg,"1.0"))
        print("{0} pytermupdateass [VER]: {1}\n". format(py_term_lg,"0.1"))
        print("{0} runprogram [VER]: {1}\n". format(py_term_lg,"0.3"))
        print("{0} help [VER]: {1}\n". format(py_term_lg,"1.3"))
        print("{0} configsu [VER]: {1}\n". format(py_term_lg,"1.2"))
        print("{0} cfg_update [VER]: {1}\n". format(py_term_lg,"1.0"))
        print("{0} compatibleos [VER]: {1}\n" . format(py_term_lg,"1.1"))
        print("{0} filedictformat [VER]: {1}\n". format(py_term_lg,"1.2"))