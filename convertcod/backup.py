import sqlite3
import os
from tkinter import filedialog
from datetime import datetime
from .processor import resource_path
from .internal_storage import insert_selectData ,get_selectData
import tempfile


url = tempfile.gettempdir()
# print(url)
def Backup():
   conn = sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
   # Open() function
   filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
   time = datetime.now().date()
   name = f"{filedir}/backup_{time}.db" 
   backup_New = sqlite3.connect(resource_path(name))
   conn.backup(backup_New)
   print(' Backup performed successfully!')
   print(' Data Saved as backupdatabase_dump.sql')
   conn.close() 
   backup_New.close()
   
def BackupView():
   filedir = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="اختر قاعدة بيانات للعرض",filetypes=(("db File",".db"), ("DB File",".DB")))
   if len(get_selectData()) > 0:
      insert_selectData(str(filedir),'update')   
   else:
      insert_selectData(str(filedir),'insert')  



def Backend():
   filedir = resource_path('assets\\backup\\dataSorte.db')
   if len(get_selectData()) > 0:
      insert_selectData(str(filedir),'update')   







# LIMAT EXPERIMENTAL USER
# SERCH dATAT MACHINE DEVICE 
def SerchActivate():
   # date =datetime.now().date()
   conect = sqlite3.connect(f'{url}\memory.db')
   try:
      cursor =conect.cursor()
      cursor.execute("SELECT * FROM  experimental")
      Fatch = cursor.fetchall()
      # print(Fatch)
      conect.close()
      return Fatch
   except :
      print('error sql memory')
      conect.close()
      return []
   
   
def SerchActivateLMIT():
   # date =datetime.now().date()
   conect = sqlite3.connect(f'{url}\memory.db')
   try:
      cursor =conect.cursor()
      cursor.execute("SELECT * FROM  experiLimted")
      Fatch = cursor.fetchall()
      # print(Fatch)
      conect.close()
      return Fatch
   except :
      print('error sql memory')
      conect.close()
      return []
   
# UPDATE LIMTED MACHINE 
def UPDATActivate():
   date =datetime.now().date()
   # print('hllow')
   conect = sqlite3.connect(f'{url}\memory.db')
   try:
      cursor =conect.cursor()
      table = "UPDATE experimental SET Taims=?"
      cursor.execute(table,[date])
      conect.commit()
      # print(Fatch)
   except :
      print('error sql memory')
   conect.close()
 
   
   
def UPDATActivateLMIT(date):
   # date =datetime.now().date()
   # print(date)
   conect = sqlite3.connect(f'{url}\memory.db')
   try:
      cursor =conect.cursor()
      table = "UPDATE experiLimted SET IDmachineLimtad=?"
      cursor.execute(table,[date])
      conect.commit()
      # print(Fatch)
   except :
      print('error sql memory')
   conect.close()


import platform

def get_device_id():
    try:
        # Get the machine identifier, e.g., serial number
      #   device_id = platform.uname()
        device_id = platform.machine()
        # Return the device ID
        return device_id
    except Exception as e:
        print(f"An error occurred: {e}")



def culctiveActivate():
   # date =datetime.now().date()
   # print(date)
   lIMT = 7
   conect = sqlite3.connect(f'{url}\memory.db')
   try:
      table = """ CREATE TABLE IF NOT EXISTS experimental (ID INTEGER PRIMARY KEY AUTOINCREMENT,IDmachine TEXT NOT NULL,Taims DATE NULL DEFAULT CURRENT_DATE)   
      """
      tableLIMTED = """ CREATE TABLE IF NOT EXISTS experiLimted (ID INTEGER PRIMARY KEY AUTOINCREMENT,IDmachineLimtad INTEGER NOT NULL)   
      """
      cursor =conect.cursor()
      cursor.execute(table)
      cursor.execute(tableLIMTED)
      device_id = get_device_id()
      if device_id:
         print(f"Device ID: {device_id}")
         tableInsert = """INSERT INTO experimental (IDmachine ) VALUES (?) """
         tableInsertlIMTED = """INSERT INTO experiLimted (IDmachineLimtad ) VALUES (?) """
         cursor.execute(tableInsert,[device_id])
         cursor.execute(tableInsertlIMTED,[lIMT])
         conect.commit()
         print('sesccfly')
      else:
         print("Failed to get the device ID.")
   except sqlite3.IntegrityError:
      print('error sql memory')
   conect.close()








# import socket

# def get_device_ip():
#     try:
#         # Get the host name of the device
#         host_name = socket.gethostname()
        
#         # Get the IP address of the device
#         device_ip = socket.gethostbyname(host_name)
        
#         # Return the device IP
#         return device_ip
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Get the device IP and print it
# device_ip = get_device_ip()
# if device_ip:
#     print(f"Device IP: {device_ip}")
# else:
#     print("Failed to get the device IP.")





# from sqlite3 import connect
# # Backup a memory database to a file
# memory_db = connect(':memory:')
# backup_db = connect('my_backup.db')
# memory_db.backup(backup_db)
# memory_db.close()
# backup_db.close()






# from cpuid import get_cpu_info

# def get_device_id():
#     try:
#         # Get the CPU info
#         cpu_info = get_cpu_info()
        
#         # Extract the device ID from the CPU info
#         device_id = cpu_info["Processor Serial Number"]
        
#         # Return the device ID
#         return device_id
#     except Exception as e:
#         print(f"An error occurred: {e}")

# # Get the device ID and print it
# device_id = get_device_id()
# if device_id:
#     print(f"Device ID: {device_id}")
# else:
#     print("Failed to get the device ID.")
# In this case, the device ID is generated based on the CPU's serial number. Keep in mind that you may need to install the cpuid library before running this code. You can do this by running the following command in your terminal:

# bash
# Download
# Copy code
# pip install py-cpuinfo