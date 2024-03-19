import sqlite3
import os
from tkinter import filedialog
from datetime import datetime
from convertcod.processor import resource_path

import tempfile


url = tempfile.gettempdir()
# print(url)

# ***********************************************
# نسخه من البيانات الاساسية للادمن
def BackupData_origin():
   conn = sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
   # Open() function
   filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
   time = datetime.now().date()
   name = f"{filedir}/update_DataAdmin_{time}.db" 
   backup_New = sqlite3.connect(resource_path(name))
   conn.backup(backup_New)
   print(' Backup performed successfully!')
   print(' Data Saved as backupdatabase_dump.sql')
   conn.close() 
   backup_New.close()
   
def Backup_data_origin_import():
    filedir = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="اختر قاعدة بيانات للتحديث",filetypes=(("db File",".db"), ("DB File",".DB")))
    if len(filedir) > 0 :
        conn = sqlite3.connect(resource_path(filedir))
        # Open() function
        # filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
        backup_New = sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
        conn.backup(backup_New)
        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.sql')
        conn.close() 
        backup_New.close()
    else:
        print(filedir)



# ***************************************************************************
#  نسخة للبيانات المستخدم من الادمن
    
def BackupData_user():
   conn = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
   # Open() function
   filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
   time = datetime.now().date()
   name = f"{filedir}/update_DataAdmin_{time}.db" 
   backup_New = sqlite3.connect(resource_path(name))
   conn.backup(backup_New)
   print(' Backup performed successfully!')
   print(' Data Saved as backupdatabase_dump.sql')
   conn.close() 
   backup_New.close()
   
def Backup_data_user_import():
    filedir = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="اختر قاعدة بيانات للتحديث",filetypes=(("db File",".db"), ("DB File",".DB")))
    if len(filedir) > 0 :
        conn = sqlite3.connect(resource_path(filedir))
        # Open() function
        # filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
        backup_New = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
        conn.backup(backup_New)
        print(' Backup performed successfully!')
        print(' Data Saved as backupdatabase_dump.sql')
        conn.close() 
        backup_New.close()
    else:
        print(filedir)


