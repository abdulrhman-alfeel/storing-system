import sqlite3
from tkinter import filedialog
from convertcod.processor import resource_path
from datetime import datetime
import os

def Backup_impot():
    filedir = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",filetypes=(("db File",".db"), ("DB File",".DB")))
    export_data_trovels(filedat=filedir)
    export_data_deportees(filedat=filedir)
    export_data_Arrest(filedat=filedir)
    export_data_prohibited(filedat=filedir)
    export_data_lodes(filedat=filedir)
    export_data_list_verify(filedat=filedir)
    os.remove(filedir)
    # os.renames



# *****************************************************************
# بيانات الحركة 
# *****************************************************************
def export_movement(filedat):
    global navigation
    navigation = {}
    # connta = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    connta =  sqlite3.connect(resource_path(filedat))
    try:
        cursor =connta.cursor()
        tabelUpdet = 'SELECT * FROM movement '
        cursor.execute(tabelUpdet)
        DATAnav = cursor.fetchall()
        # print(DATAnav)
            # print(navigation)
        if DATAnav is not None:
            for item in DATAnav:
                insert_movement(item)
    except sqlite3.IntegrityError:
        print('Error', sqlite3.IntegrityError)
    connta.close()
    gc.collect()



def insert_movement(item):
    conn = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = conn.cursor()
        tabel = """INSERT INTO movement (userName,datamovement,kindMovement, stayuser,dataExet,arrayMovement,Time) VALUES (?,?,?,'false',?,?,?) """
        data_tabel =(item[1],item[2],item[3],item[5],item[6],item[7])
        cursor.execute(tabel,data_tabel)
        conn.commit()
    except sqlite3.IntegrityError:
        print('error in insert movement')
    conn.close()





# ***********************************************************
# 1- بيانات الكوشن
# *************************************************************
def export_data_trovels(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM Travelers_DAY""")
            # Get the data
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_data_new_travelers(item)
            else:
                print(data,'error')

    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_data_new_travelers(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:

            dtat_table = '''INSERT INTO Travelers_DAY (process_ID,nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,ِAttachments_Json,Time,user,sorting) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            data = (item[1],item[2],item[3]
                    ,item[4],item[5],item[6],item[7]
                    ,item[8],item[9],item[10],item[11],
                    item[12],item[13])

            cursor.execute(dtat_table,data)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()

# ***********************************************************





# 1- بيانات المرحلين
# *************************************************************


def export_data_deportees(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            cursor.execute("""SELECT * FROM Deportees_DAY """)
            # Get the data
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_data_new_deportees(item)
            else:
               print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_data_new_deportees(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            dtat_table = '''INSERT INTO Deportees_DAY (namedeportees,Gender,agedeportees,ID_numberCart,Imageurl,iDdrive_DAY,destination,Time,user,sorting) 
                VALUES(?,?,?,?,?,?,?,?,?,?)'''
            data = (item[1],item[2],item[3]
                    ,item[4],item[5],item[6],item[7]
                    ,item[8],item[9],item[10])
            cursor.execute(dtat_table,data)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()






# 1- بيانات المضبوطين من المطلوبين
# *************************************************************


def export_data_Arrest(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            cursor.execute("""SELECT * FROM wanted """)
            # Get the data
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_EXPORT_new_Arrest(item)
            else:
                 print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_EXPORT_new_Arrest(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        with connection:
            table_u = """UPDATE wanted SET ID_numberCart=?,age_wanted=?,Gender_wanted=?,charge=?,Done=?,Time_Arrest=?,url_image_wanted=?,user=?,sorting=? WHERE trim(name_wanted)=trim(?)"""
            data_update_table = (item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[11],item[12],item[2])
            cursor.execute(table_u,data_update_table)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()








# 1- بيانات المضبوطات من الممنوعات
# *************************************************************
def export_data_prohibited(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        with connection:
            cursor.execute("""SELECT * FROM Prohibited_items_cash """)
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_EXPORT_new_PROHIBITED(item)
            else:
                 print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_EXPORT_new_PROHIBITED(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            table_u = """INSERT INTO Prohibited_items_cash (name_Prohibited,amount,trafficker
                    ,Gender_trafficker,AGE_trafficker,url_prohibited,url_trafficker,user,sorting) VALUES (?,?,?,?,?,?,?,?,?)"""
            data_update_table = (item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[10],item[11])
            cursor.execute(table_u,data_update_table)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()









# 1- بيانات المضبوطات من الممنوعات
# *************************************************************


def export_data_lodes(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            cursor.execute("""SELECT * FROM Loads_today""")
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_EXPORT_new_lodes(item)
            else:
                 print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_EXPORT_new_lodes(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        with connection:
            table_u = """INSERT INTO Loads_today (ID,type_payload,amount_payload,Sender,
            ID_numberCart_SINDER,sender_phone,Recipient,phone_recipient,ID_numberCart_recipient,
                            name_office,drive_name,destination,kind_oprtion,user,sorting) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
            
            data_update_table = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14])
            cursor.execute(table_u,data_update_table)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()





# 1- بيانات القائمة السوداء والرمادية
# *************************************************************


def export_data_list_verify(filedat):
    connection =  sqlite3.connect(resource_path(filedat))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            cursor.execute("""SELECT * FROM list_vierfy""")
            # Get the data
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                for item in data:
                    insert_EXPORT_new_list_verify(item)
            else:
                print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_EXPORT_new_list_verify(item):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        with connection:
            table_u = """INSERT INTO list_vierfy (name,TimeInsert,ID_numberCart,type_difference,count_difference,kind_list,user) VALUES (?,?,?,?,?,?,?)"""
            data_update_table = (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
            cursor.execute(table_u,data_update_table)
            connection.commit()
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
    connection.close()




