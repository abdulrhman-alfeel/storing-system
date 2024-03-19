import sqlite3
from convertcod.processor import resource_path
from convertcod.userfind import responsebletUser
from datetime import datetime 
import gc
from tkinter import filedialog 
import os 


def creat_databise_new():
            global dir
            filedir = filedialog.askdirectory(initialdir=os.getcwd(),title="اختر ملف لحفظ النسخة",mustexist=True)
            dir = f"{filedir}/data_neew.db" 
            conn = sqlite3.connect(resource_path(dir))       
            table_create_TRIVERS_DAY = '''CREATE TABLE IF NOT EXISTS Travelers_DAY 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,process_ID INTEGER NULL,nameTrovel TEXT NOT NULL ,Gender TEXT NULL
            ,ageTrovel INTEGER NULL,workplace TEXT NOT NULL,
            Address TEXT NULL,ID_numberCart INTEGER NOT NULL,iDdrive_DAY TEXT NULL ,
            destination TEXT NULL,ِAttachments_Json JSON NULL,Time DATE NULL DEFAULT CURRENT_DATE,user TEXT NULL,sorting TEXT NULL)
            '''
                        # FOREIGN KEY(iDdrive_DAY) REFERENCES drive_pablic (iDdrive) ON DELETE RESTRICT ON UPDATE RESTRICT)

            table_create_THEGOODES_or_payload_DAY = '''CREATE TABLE IF NOT EXISTS Loads_today 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,type_payload TEXT NULL ,amount_payload INTEGER NULL,Sender TEXT NULL,
            ID_numberCart_SINDER INTEGER  NULL,sender_phone INTEGER NULL,Recipient TEXT NULL,phone_recipient INTEGER NULL,
            ID_numberCart_recipient INTEGER  NULL,
            name_office TEXT NULL, drive_name TEXT NULL,destination TEXT NULL,kind_oprtion TEXT NULL,user TEXT NULL,sorting TEXT NULL,Time DATE NULL DEFAULT CURRENT_DATE)
            '''

            table_create_Deportees_DAY = '''CREATE TABLE IF NOT EXISTS Deportees_DAY 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,namedeportees TEXT NOT NULL ,Gender TEXT NULL,agedeportees TEXT NULL
            ,ID_numberCart TEXT NULL,Imageurl BLOB NULL,iDdrive_DAY TEXT NOT NULL ,destination TEXT NULL,
            Time DATE NULL DEFAULT CURRENT_DATE,user TEXT NULL,sorting TEXT NULL,Fingerprint TEXT NULL)
            '''

            table_create_cash_prohibited = '''CREATE TABLE IF NOT EXISTS Prohibited_items_cash
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            name_Prohibited TEXT NOT NULL,amount TEXT NOT NULL ,trafficker TEXT NULL ,Gender_trafficker TEXT NULL,
            AGE_trafficker TEXT NULL,url_prohibited BLOB NULL,url_trafficker BLOB NULL ,ArrayCaught JSON NULL,user TEXT NULL,sorting TEXT NULL)
            '''
            # arrayCaught == nameforbidding and namedrive and iddrive  and trafficker and namerecipient and time_day_caught  
    
            table_create_wanted = '''CREATE TABLE IF NOT EXISTS wanted 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,              
            TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            name_wanted TEXT NOT NULL UNIQUE, ID_numberCart TEXT NULL ,age_wanted TEXT NULL
            ,Gender_wanted TEXT NULL,charge TEXT NULL ,Done TEXT NULL DEFAULT "هارب",Time_Arrest DATE NULL ,url_image_wanted BLOB NULL,ArrayCaught JSON NULL
            ,user TEXT NULL,sorting TEXT NULL,fingerprint TEXT NULL)
            '''
            
            table_create_Sort_LIST_difference = '''CREATE TABLE IF NOT EXISTS list_vierfy 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NULL , TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            ID_numberCart INTEGER NOT NULL , type_difference TEXT NOT NULL ,count_difference INTEGER NOT NULL,
            kind_list TEXT NULL,Arraydifference JSON NULL,user TEXT NULL)
            '''
            tabelNavigetion = '''CREATE TABLE IF NOT EXISTS movement (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                userName TEXT NOT NULL,datamovement  DATE NULL DEFAULT CURRENT_DATE,
                kindMovement TEXT NULL , stayuser TEXT NOT NULL,dataExet DATE NULL, arrayMovement JSON NULL,Time DATE NULL DEFAULT CURRENT_DATE)'''
            try:
                conn.execute(table_create_TRIVERS_DAY)
                conn.execute(table_create_THEGOODES_or_payload_DAY)
                conn.execute(table_create_cash_prohibited)
                conn.execute(table_create_wanted)
                conn.execute(table_create_Sort_LIST_difference)
                conn.execute(table_create_Deportees_DAY)
                conn.execute(tabelNavigetion)
                # private python or python specificWWW
                #private insert named credits pablic 
            except sqlite3.IntegrityError:
                print("couldn't add Python twice")
            conn.commit() 
            conn.close()


            user = responsebletUser()
            export_data_trovels(user=user['userName'])
            export_data_deportees(user=user['userName'])
            export_data_Arrest(user=user['userName'])
            export_data_prohibited(user=user['userName'])
            export_data_list_verify(user=user['userName'])
            export_data_lodes(user=user['userName'])
            export_movement(user=user['userName'])







# *****************************************************************
# بيانات الحركة 
# *****************************************************************
def export_movement(user):
    global navigation
    navigation = {}
    # connta = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    connta =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor =connta.cursor()
        tabelUpdet = 'SELECT * FROM movement WHERE userName=? AND Time=? '
        cursor.execute(tabelUpdet,[user,str(datetime.now().date())])
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
    conn = sqlite3.connect(resource_path(dir))
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


def export_data_trovels(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM Travelers_DAY WHERE user=? AND Time =?""",[user,str(datetime.now().date())])
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
    connection =  sqlite3.connect(resource_path(dir))
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


def export_data_deportees(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM Deportees_DAY WHERE user=? AND Time =?""",[user,str(datetime.now().date())])
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
    connection =  sqlite3.connect(resource_path(dir))
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


def export_data_Arrest(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM wanted WHERE Done='مضبوط' AND user=? AND Time_Arrest=?""",[user,str(datetime.now().date())])
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

    connection =  sqlite3.connect(resource_path(dir))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:

            table_u = """INSERT INTO wanted (ID,name_wanted,ID_numberCart,age_wanted,Gender_wanted,charge,Done,Time_Arrest,url_image_wanted,user,sorting) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
            
            data_update_table = (item[0],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[11],item[12])
            cursor.execute(table_u,data_update_table)
            connection.commit()

    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()








# 1- بيانات المضبوطات من الممنوعات
# *************************************************************


def export_data_prohibited(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM Prohibited_items_cash WHERE user=? AND TimeInsert=?""",[user,str(datetime.now().date())])
            # Get the data
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

    connection =  sqlite3.connect(resource_path(dir))
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


def export_data_lodes(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM Loads_today WHERE user=? AND Time=?""",[user,str(datetime.now().date())])
            # Get the data
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

    connection =  sqlite3.connect(resource_path(dir))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
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


def export_data_list_verify(user):
    connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:
            # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
            #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
            cursor.execute("""SELECT * FROM list_vierfy WHERE user=? AND TimeInsert=?""",[user,str(datetime.now().date())])
            # Get the data
            data = cursor.fetchall()
            Ferquntlye= []
            if data is not None:
                # return list(data)
                for item in data:
                    insert_EXPORT_new_list_verify(item)
            else:
                 print(data,'error')
    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()




def insert_EXPORT_new_list_verify(item):

    connection =  sqlite3.connect(resource_path(dir))
    try:
        cursor = connection.cursor()
        # cursor.execute("SELECT * FROM ferquntlye ")
        with connection:

            table_u = """INSERT INTO list_vierfy (name,TimeInsert,ID_numberCart,type_difference,count_difference,kind_list,user) VALUES (?,?,?,?,?,?,?)"""
            
            data_update_table = (item[0],item[1],item[2],item[3],item[4],item[5],item[6])
            cursor.execute(table_u,data_update_table)
            connection.commit()

    except sqlite3.IntegrityError:
        print("couldn't add Python twice")
        # conn.commit() 
    connection.close()








# def export_data_Arrest(user):
#     connection =  sqlite3.connect(resource_path('assets\\backup\\dataSorte.db'))
#     try:
#         cursor = connection.cursor()
#         # cursor.execute("SELECT * FROM ferquntlye ")
#         with connection:
#             # cursor.execute("""SELECT process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,
#             #                iDdrive_DAY,destination,ِAttachments_Json ,Time, user,sorting FROM Travelers_DAY WHERE user=?""",[user])
#             cursor.execute("""SELECT name_wanted,Time_Arrest,
#             url_image_wanted,user,sorting FROM wanted WHERE Done='مضبوط' AND user=? AND Time_Arrest=?""",[user,str(datetime.now().date())])
#             # Get the data
#             data = cursor.fetchall()
#             Ferquntlye= []
#             if data is not None:
#                 # return list(data)
#                 for item in data:
#                     insert_data_new_deportees(item)
#             else:
#                  print(data,'error')
#     except sqlite3.IntegrityError:
#         print("couldn't add Python twice")
#         # conn.commit() 
#     connection.close()




# def insert_IMPORT_new_deportees(item):

#     connection =  sqlite3.connect(resource_path(dir))
#     try:
#         cursor = connection.cursor()
#         # cursor.execute("SELECT * FROM ferquntlye ")
#         with connection:

#             dtat_table = """UPDATE wanted SET Done='مضبوط', Time_Arrest=?,
#             url_image_wanted =?,user=?,sorting=? WHERE trim(name_wanted)=trim(?)"""
#             data = (item[1],item[2],item[3]
#                     ,item[4],item[0])

#             cursor.execute(dtat_table,data)
#             connection.commit()


#     except sqlite3.IntegrityError:
#         print("couldn't add Python twice")
#         # conn.commit() 
#     connection.close()