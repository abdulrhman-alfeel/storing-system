import sqlite3
from datetime import datetime
from tkinter import messagebox
import re
from convertcod.json_stringify import json_stringify
from convertcod.json_parse import *
import os 
from convertcod.processor import resource_path
from convertcod.internal_storage import get_selectData
def nameData():
    try:
        Dirbase = get_selectData()
        if len(Dirbase) <= 0 :
            Dir= 'assets\\backup\\dataSorte.db'
            # print(Dirbase[0][1])
        else:
            Dir= str(Dirbase[0][1])
        return resource_path(Dir)
    except:
        Dirbase= 'assets\\backup\\dataSorte.db'
            # print(Dirbase[0][1])
        return resource_path(Dirbase)
    
class StationMonthSqly():
    def __init__(self):
            self.Frequntlye = []
            self.inComin_dataAll()

        #   الفرز وبياناتها 
    def insert_Pablic_station(nameSorting,sortingSit,Admin,IDsort,destination_Json,vierfiy=None):
        # print(classifyP)
        arrayNew=[]
        numSum = 0
        connection = sqlite3.connect(nameData())
        cursor = connection.cursor()
        try:
            with connection:
            # print(incomingquantity,vierfiy,vierfiyDone)
                if vierfiy is None :
                    teable_insert_qurey= '''UPDATE sorting SET nameSorting =?, sortingSit=?,Admin_sorting=?,destination_Json=? WHERE IDsort=?'''
                    data_insert_tuple = (nameSorting,sortingSit,Admin,destination_Json,IDsort)
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
                else:
                    # numberIdusb= randomnumber()
                    # if image_license is not None and image_care is not None and image_drive is not None:
                    teable_insert_qurey= '''INSERT INTO sorting (nameSorting,sortingSit,Admin_sorting,IDsort,destination_Json) VALUES(?,?,?,?,?)'''
                    
                    data_insert_tuple = (nameSorting,sortingSit,Admin,IDsort,destination_Json)
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
        except sqlite3.IntegrityError:
             print("error")    
        connection.close() 


    def inComin_dataAll():
                global station
                connection =  sqlite3.connect(nameData())
                try: 
                    cursor = connection.cursor()
                    with connection:
                        cursor.execute("SELECT * FROM sorting")
                        # Get the data
                        data = cursor.fetchall()
                        # print(data)
                        station= []
                        for i in range(len(data)):
                                    obje = {}
                                    obje['ID']= data[i][0] 
                                    obje['nameSorting']=  data[i][1]
                                    obje['sortingSit']=  data[i][2]
                                    obje['Admin_sorting']=  data[i][3]
                                    obje['TimeInsert']=  data[i][4]
                                    obje['IDsort']=  data[i][5]
                                    dataarrays = data[i][6]
                                    if dataarrays is not None and len(dataarrays) > 0:
                                        obje['Arrayjson']=  json_parse(dataarrays)
                                    else:
                                        obje['Arrayjson']= []
                                    dataarrays_disation = data[i][7]
                                    if dataarrays_disation is not None and len(dataarrays_disation) > 0:
                                        obje['destination_Json']=  json_parse(dataarrays_disation)
                                    else:
                                        obje['destination_Json']= []
                                    station.append(obje)  
                    return list(station)
                except sqlite3.IntegrityError:
                    print("couldn't add Python twice")
                    # conn.commit() 
                connection.close()

    def inComin_dataAllwitch():
            conn =  sqlite3.connect(nameData())
            try:
                cursor = conn.cursor()
                with conn:
                        cursor.execute( "SELECT ID,nameSorting,sortingSit,Admin_sorting,TimeInsert,IDsort,Arrayjson FROM sorting")
                        data = cursor.fetchall()
                        return list(data)
            except sqlite3.IntegrityError:
                    print("dont's have data")
            conn.close()


# وظائف حسابات السائقين    
    def insert_Pablic(iddrive,namedrive,ID_numberCart,kindCare,ColorCare,number_Care,Guarantee,IDsort,image_care,image_drive,image_license,type=None):
        # print(image_care)
        connection =  sqlite3.connect(nameData())
        # print(image_care)
        try:
            with connection:      
                if type is None:               
                    teable_insert_qurey= '''INSERT INTO drive_pablic (iDdrive,namedrive,ID_numberCart,kind_care,Color_care,
                    number_Care,Guarantee,IDsort,url_Image_care,url_Image_drive,url_image_license) VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
                    data_insert_tuple = (str(iddrive),str(namedrive),str(ID_numberCart),str(kindCare),str(ColorCare)
                                         ,str(number_Care),str(Guarantee),str(IDsort), sqlite3.Binary(image_care) if image_care is not None else image_care
                                         ,sqlite3.Binary(image_drive) if image_drive is not None else image_drive
                                         ,sqlite3.Binary(image_license) if image_license is not None else image_license)
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
                else:
                    teable_insert_qurey= '''UPDATE drive_pablic SET namedrive=?, ID_numberCart=?,kind_care=?,
                    Color_care=?,number_Care=?,Guarantee=?, IDsort=?, url_Image_care=?,url_Image_drive=?,url_image_license=? WHERE iDdrive=?'''
                    data_insert_tuple = (str(namedrive),str(ID_numberCart),str(kindCare),str(ColorCare),str(number_Care),str(Guarantee),str(IDsort),
                                         sqlite3.Binary(image_care) if image_care is not None else image_care
                                         ,sqlite3.Binary(image_drive) if image_drive is not None else image_drive
                                         ,sqlite3.Binary(image_license) if image_license is not None else image_license,str(iddrive))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
        except sqlite3.IntegrityError:
                print("there is a problem") 
        connection.close() 


#  جلب البيانات  الرئيسية لمستفيدين من الصرف  للعرض     
    def inComin_Pablic_drive():
                connection =  sqlite3.connect(nameData())
                try:
                    cursor = connection.cursor()
                    # cursor.execute("SELECT * FROM ferquntlye ")
                    with connection:
                        cursor.execute("SELECT iDdrive,namedrive,ID_numberCart,kind_care,Color_care,number_Care,Guarantee,IDsort,Time FROM drive_pablic")
                        # Get the data
                        data = cursor.fetchall()
                        Ferquntlye= []
                        if data is not None:
                            return list(data)
                except sqlite3.IntegrityError:
                    print("couldn't add Python twice")
                    # conn.commit() 
                connection.close()

#جلب البيانات الرئيسية للمستفيدين من الصرف بيانات الاعتمادات  
    def brings_drive_Pablic():
                connection =  sqlite3.connect(nameData())
                try:
                    cursor = connection.cursor()
                    # cursor.execute("SELECT * FROM ferquntlye ")
                    with connection:
                        cursor.execute(" SELECT * FROM drive_pablic ")
                        # Get the data
                        data = cursor.fetchall()
                        Ferquntlye= []
                        for i in range(len(data)):
                            obje = {"iDdrive":data[i][0],"namedrive":data[i][1],'ID_numberCart':data[i][2], 
                                    "kind_care":data[i][3],"Color_care": data[i][4],"number_Care":data[i][5],
                                    "Guarantee":data[i][6],"IDsort":data[i][7],"Time":data[i][8],
                                    'stating':data[i][9],"Arrayjson":data[i][10],"url_Image_care":data[i][11],"url_Image_drive":data[i][12],
                                    "url_image_license":data[i][13]}
                            
                            Ferquntlye.append(obje)
                        return list(Ferquntlye)
                except sqlite3.IntegrityError:
                    print("couldn't add Python twice")
                    # conn.commit() 
                connection.close()



#  لجمع بيانات الشهرية للحساب السواق وحذفة 
    def DeletAcontfetchArryJson(iDdrive,VIREBLISWITCH):
        conn =  sqlite3.connect(nameData())
        try:
            cursor = conn.cursor()
            print(VIREBLISWITCH)

            if VIREBLISWITCH["name1"] == 'DeletAll':
                cursor.execute('UPDATE drive_pablic SET Arraypash = ( SELECT  Arraypash  FROM (Sort_Month)  WHERE iDdrive=? ) , stating="محذوف"  WHERE iDdrive=? ',[iDdrive,iDdrive])
                cursor.execute("UPDATE Sort_Month SET stating='محذوف'  WHERE iDdrive=?",[iDdrive]) 
                messagebox.showwarning(title='Error', message='تم حذف السواق بنجاح')
            else:
                cursor.execute('UPDATE drive_pablic SET  stating="جاري"  WHERE iDdrive=? ',[iDdrive])
                cursor.execute("UPDATE Sort_Month SET stating='جاري'  WHERE iDdrive=?",[iDdrive]) 
                messagebox.showwarning(title='Error', message='تم استرداد السواق بنجاح')
            conn.commit()
            return True
        except sqlite3.IntegrityError:
            print('Error',sqlite3.IntegrityError)
        






    # بيانات المكتب
    def insert_Office(iDoffice,office_name,owner_name,ID_numberCart,employ_name,Licensig,IDsort,url_image_licens,type=None):
        connection =  sqlite3.connect(nameData())
        try:
            with connection:      
                if type is None:               
                    teable_insert_qurey= '''INSERT INTO office (iDoffice,office_name,owner_name,ID_numberCart,
                    employ_name,Licensig,IDsort,url_image_licens) VALUES(?,?,?,?,?,?,?,?)'''
                    data_insert_tuple = (str(iDoffice),str(office_name),str(owner_name),str(ID_numberCart),employ_name,str(Licensig),str(IDsort),sqlite3.Binary(url_image_licens))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
                else:
                    teable_insert_qurey= '''UPDATE office SET office_name=?, owner_name=?,ID_numberCart=?
                    ,employ_name=?,Licensig=?,IDsort=?,url_image_licens=? WHERE iDoffice=?'''
                    data_insert_tuple = (str(office_name),str(owner_name),str(ID_numberCart),employ_name,str(Licensig),str(IDsort),sqlite3.Binary(url_image_licens),str(iDoffice))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
        except sqlite3.IntegrityError:
                print("there is a problem") 
        connection.close() 
        

#جلب البيانات الرئيسية للمكاتب  
    def inCominOffice_Pablic():
                connection =  sqlite3.connect(nameData())
                try:
                    cursor = connection.cursor()
                    # cursor.execute("SELECT * FROM ferquntlye ")
                    with connection:
                        cursor.execute(" SELECT * FROM office ")
                        # Get the data
                        data = cursor.fetchall()
                        Ferquntlye= []
                        for i in range(len(data)):
                            obje = {"iDoffice":data[i][0],"office_name":data[i][1],
                                    'owner_name':data[i][2], 
                                    "ID_numberCart":data[i][3],
                                    'employ_name':data[i][4],
                                    "Licensig": data[i][5],
                                    'stating':data[i][6],
                                    "IDsort":data[i][7],
                                    "Time":data[i][8],
                                    "Arrayjson":data[i][9],
                                    "url_image_licens":data[i][10]}
                            Ferquntlye.append(obje)
                        return list(Ferquntlye)
                except sqlite3.IntegrityError:
                    print("couldn't add Python twice")
                    # conn.commit() 
                connection.close()



    # بيانات المسافرين

    def Delete_Travelers_Day(id_process):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            tabel = """DELETE FROM Travelers_DAY WHERE process_ID =?"""
            cursor.execute(tabel,[id_process])
            connect.commit() 
        except sqlite3.IntegrityError:
             print('error sqlite in delete')
        connect.close()
        



# عملية اضافة بيانات المسافرين
    def insert_Troval_drive_day(item,id_process,sorting):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            dtat_table = '''INSERT INTO Travelers_DAY (process_ID,nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,ِAttachments_Json,user,sorting) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?,?)'''
            data = (id_process,item['nameTrovel'],item['Gender'],item['ageTrovel']
                    ,item['workplace'],item['Address'],item['ID_numberCart'],item["iDdrive_DAY"],item["destination"],item['Attachments_Json'],item['user'],sorting)
 
            dtat_table_None = '''INSERT INTO Travelers_DAY (process_ID,nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,user,sorting) 
                VALUES(?,?,?,?,?,?,?,?,?,?,?)'''
            data_None = (id_process,item['nameTrovel'],item['Gender'],item['ageTrovel']
                    ,item['workplace'],item['Address'],item['ID_numberCart'],item["iDdrive_DAY"],item["destination"],item['user'],sorting)
            
            if len(item['Attachments_Json']) > 0:
                print(item['nameTrovel'])
                cursor.execute(dtat_table,data)
            else:
                print(item['nameTrovel'])
                cursor.execute(dtat_table_None,data_None)
          
            connect.commit()
        except:
             pass



# جلب البيانات  الرئيسية لمستفيدين من الصرف  للعرض     
    def Brings_Travelers(oprtion=None,nameTrovles=None,Time=None):
        connection =  sqlite3.connect(nameData())
        try:
            cursor = connection.cursor()
            # cursor.execute("SELECT * FROM ferquntlye ")
            with connection:
                if oprtion is None:
                    cursor.execute("SELECT ID,process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,Time,ِAttachments_Json,sorting FROM Travelers_DAY ")
                elif oprtion == 'count':
                     cursor.execute('SELECT COUNT(DISTINCT process_ID) AS counts FROM Travelers_DAY WHERE sorting=? AND Time=?',[nameTrovles,Time])
                elif oprtion == 'countAll':
                     cursor.execute('SELECT COUNT(*) AS counts FROM Travelers_DAY WHERE sorting=? AND Time=?',[nameTrovles,Time])
                elif oprtion == 'countJSON':
                     cursor.execute('SELECT COUNT(DISTINCT process_ID) AS counts FROM Travelers_DAY WHERE ِAttachments_Json IS NOT NULL AND sorting=? AND Time=?',[nameTrovles,Time])
                elif oprtion == 'countMonth':
                     cursor.execute('SELECT COUNT(DISTINCT process_ID) AS counts FROM Travelers_DAY WHERE sorting=? AND  strftime("%Y-%m",Time) = ? ',[nameTrovles,Time])
                elif oprtion == 'countAllMonth':
                     cursor.execute('SELECT COUNT(*) AS counts FROM Travelers_DAY WHERE sorting=? AND strftime("%Y-%m",Time) = ? ',[nameTrovles,Time])
                elif oprtion == 'countJSONMonth':
                     cursor.execute('SELECT COUNT(DISTINCT process_ID) AS counts FROM Travelers_DAY WHERE ِAttachments_Json IS NOT NULL AND sorting=? AND  strftime("%Y-%m",Time) = ? ',[nameTrovles,Time])
                else:
                    cursor.execute("SELECT ID,process_ID, nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,Time,ِAttachments_Json,sorting,user FROM Travelers_DAY")
                # Get the data
                data = cursor.fetchall()
                # dataone = cursor.fetchone()
                Ferquntlye= []
                if data is not None:
                    if oprtion == 'count' or oprtion == 'countJSON' or oprtion == 'countAll':
                         return data
                    else:
                        return list(data)
        except sqlite3.IntegrityError:
            print("couldn't add Python twice")
            # conn.commit() 
        connection.close()
# SELECT * FROM Travelers_DAY a JOIN Travelers_DAY b ON  a.process_ID = b.process_ID WHERE  a.ID <> b.ID AND a.ID < b.ID
# SELECT COUNT(DISTINCT process_ID) AS counts,* FROM Travelers_DAY  ;


# وظائف الممنوعات    
    def insert_LIST_prohibited(name_Prohibited,amount,type=None):
        connection =  sqlite3.connect(nameData())
        try:
            with connection:      
                if type is None:               
                    teable_insert_qurey= '''INSERT INTO Prohibited_items_list (name_Prohibited,amount) VALUES(?,?)'''
                    data_insert_tuple = (str(name_Prohibited),str(amount))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
                else:
                    teable_insert_qurey= '''UPDATE Prohibited_items_list SET name_Prohibited=?, amount=? WHERE ID=?'''
                    data_insert_tuple = (str(name_Prohibited),str(amount),str(type))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
        except sqlite3.IntegrityError:
                print("there is a problem") 
        connection.close() 




    def get_list_prohibited():
        conn = sqlite3.connect(nameData())
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Prohibited_items_list")
            data = cursor.fetchall()
            return data
        except sqlite3.IntegrityError:
             pass
        conn.close()
        






    def insert_Pablic_prohibited(name_Prohibited
                                 ,amount,
                                 trafficker
                                 ,Gender_trafficker
                                 ,AGE_trafficker,
                                 url_prohibited,
                                 url_trafficker,user,sorting,type=None):
        connection =  sqlite3.connect(nameData())
        try:
            with connection:      
                if type is None:               
                    teable_insert_qurey= '''INSERT INTO Prohibited_items_cash (name_Prohibited,amount,trafficker
                    ,Gender_trafficker,AGE_trafficker,url_prohibited,url_trafficker,user,sorting) VALUES(?,?,?,?,?,?,?,?,?)'''
                    data_insert_tuple = (str(name_Prohibited),str(amount),str(trafficker)
                                         ,str(Gender_trafficker),str(AGE_trafficker),sqlite3.Binary(url_prohibited),sqlite3.Binary(url_trafficker),str(user),str(sorting))
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
                else:
                    teable_insert_qurey= '''UPDATE Prohibited_items_cash SET name_Prohibited=?, amount=?,
                    trafficker=?,Gender_trafficker=?,AGE_trafficker=?,url_prohibited=?,url_trafficker=?, user=?,sorting=?
                      WHERE ID=?'''
                    data_insert_tuple = (str(name_Prohibited),str(amount),str(trafficker)
                                         ,str(Gender_trafficker),str(AGE_trafficker),sqlite3.Binary(url_prohibited)
                                         ,sqlite3.Binary(url_trafficker),str(user),str(sorting),type)
                    cursor = connection.cursor()
                    cursor.execute(teable_insert_qurey,data_insert_tuple)
                    connection.commit()
        except sqlite3.IntegrityError:
                print("there is a problem") 
        connection.close() 



    def get_pablic_prohibited(pages=None,Namepro=None,Time=None,Sorting=None):
        connect = sqlite3.connect(nameData())
        # print(Namepro,Time,Sorting)
        try:
            cursor= connect.cursor()
            # print(pages)
            if pages is not None  and pages != 'month' and pages != 'yars' and pages != 'day':
                cursor.execute("SELECT ID,TimeInsert,name_Prohibited,amount,trafficker,Gender_trafficker,AGE_trafficker,user,sorting FROM Prohibited_items_cash")
            elif pages == 'day':
                cursor.execute("""SELECT  ID,TimeInsert,name_Prohibited,amount,trafficker,Gender_trafficker,AGE_trafficker,user,sorting
                 FROM Prohibited_items_cash WHERE  strftime('%Y-%m-%d',TimeInsert)=? AND sorting=? """,[str(Time),Sorting])
            elif pages == 'month':
                cursor.execute("""SELECT  ID,TimeInsert,name_Prohibited,amount,trafficker,Gender_trafficker,AGE_trafficker,user,sorting
                 FROM Prohibited_items_cash WHERE  strftime('%Y-%m',TimeInsert)=? AND sorting=? """,[str(Time),Sorting])
            elif pages == 'yars':
                cursor.execute("""SELECT  ID,TimeInsert,name_Prohibited,amount,trafficker,Gender_trafficker,AGE_trafficker,user,sorting
                 FROM Prohibited_items_cash WHERE  strftime('%Y',TimeInsert)=? AND sorting=?""",[str(Time),Sorting])
            else:
                cursor.execute("SELECT ID,TimeInsert,name_Prohibited,amount,trafficker,Gender_trafficker,AGE_trafficker FROM Prohibited_items_cash")
            data = cursor.fetchall()
            # print(data[0][8],'prohibited')
            return data  
        except sqlite3.IntegrityError:
             pass
        connect.close()




    def get_pablic_prohibited_All():
    
        connect = sqlite3.connect(nameData())
        try:
            cursor= connect.cursor()
            cursor.execute("SELECT * FROM Prohibited_items_cash")
            datad = cursor.fetchall()
            ooP = {}
            arrays =[]
            for key in range(len(datad)):
                    ooP['ID'] = datad[key][0] 
                    ooP['TimeInsert'] = datad[key][1]
                    ooP['name_Prohibited'] = datad[key][2]
                    ooP['amount'] = datad[key][3]
                    ooP['trafficker'] = datad[key][4]
                    ooP['Gender_trafficker'] = datad[key][5]
                    ooP['AGE_trafficker'] = datad[key][6]
                    ooP['url_prohibited'] = datad[key][7]
                    ooP['url_trafficker'] = datad[key][8]
                    ooP['user'] = datad[key][10]
                    ooP['sorting'] = datad[key][11]
                    arrays.append(ooP)
                    ooP={}
            # print(datad[0][0])
            return arrays  
        except sqlite3.IntegrityError:
             pass
        connect.close()


#  وظائف المطلوببين 

        # *************************************************************************
        # wanted code insert 

    def Delete_Winted_Day(ID):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            tabel = """DELETE FROM wanted WHERE ID =?"""
            cursor.execute(tabel,[ID])
            connect.commit() 
        except sqlite3.IntegrityError:
             print('error sqlite in delete')
        connect.close()
        

    def insert_pablic_wanted(Data_insert,kind=None):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            if   Data_insert['Done_kind'] is not None:
                table_u = """INSERT INTO wanted (ID,name_wanted,ID_numberCart,age_wanted,Gender_wanted,charge,Done,Time_Arrest,url_image_wanted,user,sorting) VALUES (?,?,?,?,?,?,?,?,?,?,?)"""
                data_update_table = (
                                    Data_insert['ID'],Data_insert['name_wanted'],Data_insert['number_cart'],
                                    Data_insert['age_wanted'],Data_insert['Gender_wanted'],Data_insert['charge'],
                                    Data_insert['Done_kind']['Done'],Data_insert['Done_kind']['Time_Arrest'],
                                    Data_insert['Done_kind']['url_image_wanted'])
                cursor.execute(table_u,data_update_table)
            else:
                table_u = """INSERT INTO wanted (ID,name_wanted,ID_numberCart,age_wanted,Gender_wanted,charge,Done,Time_Arrest,url_image_wanted) VALUES (?,?,?,?,?,?,?,?,?)"""
                data_update_table = (Data_insert['ID'],Data_insert['name_wanted'],Data_insert['number_cart'],
                                     Data_insert['age_wanted'],Data_insert['Gender_wanted'],Data_insert['charge'],
                                      'هارب',Data_insert['Done_kind'],
                                        Data_insert['Done_kind'])
            
                cursor.execute(table_u,data_update_table)
            connect.commit()
        except sqlite3.IntegrityError:
             pass 
        connect.close()
    


    def Arrest_wanted(name_wanted,url_image_wanted,user,sorting):
        print(user,sorting)
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            table_arrest = """UPDATE wanted SET Done='مضبوط', Time_Arrest=?,
            url_image_wanted =?,user=?,sorting=? WHERE trim(name_wanted)=trim(?)"""
            data_Arrest = (str(datetime.now().date()),sqlite3.Binary(url_image_wanted),user,sorting,name_wanted)
            cursor.execute(table_arrest,data_Arrest)
            connect.commit()
        except sqlite3.IntegrityError:
                pass
        connect.close()


    def get_pablic_wanted():
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            cursor.execute('SELECT * FROM wanted')
            data = cursor.fetchall()

            oobjct= {}
            arrays_data = []
            for o in range(len(data)):
                oobjct['ID'] = data[o][0]
                oobjct['TimeInsert'] = data[o][1]
                oobjct['name_wanted'] = data[o][2]
                oobjct['ID_numberCart'] = data[o][3]
                oobjct['age_wanted'] = data[o][4]
                oobjct['Gender_wanted'] = data[o][5]
                oobjct['charge'] = data[o][6]
                oobjct['Done'] = data[o][7]
                oobjct['Time_Arrest'] = data[o][8]
                oobjct['url_image_wanted'] = data[o][9]
                oobjct['user'] = data[o][11]
                oobjct['sorting'] = data[o][12]
                arrays_data.append(oobjct)
                oobjct = {}
            return arrays_data
        except:
             pass 
        connect.close()



    def get_sub_wanted():
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            cursor.execute('SELECT ID,name_wanted,Gender_wanted,age_wanted,ID_numberCart,charge FROM wanted WHERE Done ="هارب"')
            data = cursor.fetchall()
            return data
        except:
             pass 
        connect.close()

        
    def get_Arrest_wanted(kind=None,Time=None,sorting=None):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            # cursor.execute('SELECT ID,Time_Arrest,name_wanted,age_wanted,Gender_wanted,ID_numberCart,charge FROM wanted')
            # cursor.execute('SELECT ID,name_wanted,age_wanted,Gender_wanted,ID_numberCart,charge FROM wanted')
            if kind == 'all':
                cursor.execute('SELECT charge,ID_numberCart,Gender_wanted,age_wanted,name_wanted,ID FROM wanted')
            elif kind == 'allSearch':
                cursor.execute('SELECT name_wanted,Gender_wanted,age_wanted,ID_numberCart,charge,Done,Time_Arrest,user,sorting FROM wanted')
            elif kind == 'month':
                cursor.execute('SELECT COUNT(*) FROM wanted WHERE Time_Arrest=? AND sorting=?',[str(Time),sorting])
            elif kind == 'Yars':
                cursor.execute('SELECT COUNT(*) FROM wanted WHERE strftime("%Y-%m",Time_Arrest)=? AND sorting=?',[str(Time),sorting])            
            else:
                cursor.execute('SELECT charge,ID_numberCart,age_wanted,Gender_wanted,name_wanted,Time_Arrest,ID FROM wanted')
            data_her = cursor.fetchall()
            return data_her
        except:
             pass 
        connect.close()





# *************************************************************************************
# Deportees insert data  

    def insert_pablic_Deportees(Data_insert,kind=None):
        connect = sqlite3.connect(nameData())
        try:
        
            cursor = connect.cursor()
            if kind is not None:
                 
                table_UPDATE = """UPDATE Deportees_DAY  SET namedeportees=?,agedeportees=?,Gender=?,ID_numberCart=?,
                Imageurl=?,iDdrive_DAY=?,destination=?,user=?, sorting=? WHERE ID =?"""
                data_table_UPDATE = (Data_insert['namedeportees'],Data_insert['agedeportees'],Data_insert['Gender'],
                                     Data_insert['ID_numberCart'],sqlite3.Binary(Data_insert['Imageurl'])
                                     ,Data_insert['iDdrive_DAY'],Data_insert['destination'],Data_insert['userName'],Data_insert['ID'],Data_insert['sorting'])
                cursor.execute(table_UPDATE,data_table_UPDATE)


            else:    
                table_u = """INSERT INTO Deportees_DAY (ID,namedeportees,agedeportees,Gender,ID_numberCart,Imageurl,iDdrive_DAY,destination,user,sorting) VALUES (?,?,?,?,?,?,?,?,?,?)"""
                data_table = (Data_insert['ID'],Data_insert['namedeportees'],Data_insert['agedeportees'],Data_insert['Gender'],
                              Data_insert['ID_numberCart'],sqlite3.Binary(Data_insert['Imageurl']),Data_insert['iDdrive_DAY'],
                              Data_insert['destination'],Data_insert['userName'],Data_insert['sorting'])
                cursor.execute(table_u,data_table)

            # print(Data_insert)
            connect.commit()
        except sqlite3.IntegrityError:
            print('this error') 
        connect.close()
    



    def get_pablic_Deportees_DAY():
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            cursor.execute('SELECT * FROM Deportees_DAY')
            data = cursor.fetchall()

            oobjct= {}
            arrays_data = []
            for o in range(len(data)):
                oobjct['ID'] = data[o][0]
                oobjct['namedeportees'] = data[o][1]
                oobjct['Gender'] = data[o][2]
                oobjct['agedeportees'] = data[o][3]
                oobjct['ID_numberCart'] = data[o][4]
                oobjct['Imageurl'] = data[o][5]
                oobjct['iDdrive_DAY'] = data[o][6]
                oobjct['destination'] = data[o][7]
                oobjct['Time'] = data[o][8]
                oobjct['user'] = data[o][9]
                oobjct['sorting'] = data[o][10]
                arrays_data.append(oobjct)
                oobjct = {}
            return arrays_data
        except:
             pass 
        connect.close()



        
    def get_Deportees(pages=None,Time=None,sorting=None):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            if pages is not None:
                if pages == 'month':
                    cursor.execute('SELECT COUNT(*) FROM Deportees_DAY WHERE strftime("%Y-%m-%d",Time)=? AND sorting=?',[str(Time),sorting])
                elif pages == 'Yars':
                    cursor.execute('SELECT COUNT(*) FROM Deportees_DAY WHERE strftime("%Y-%m",Time)=? AND sorting=?',[str(Time),sorting])
                else:
                    cursor.execute('SELECT namedeportees,Gender,agedeportees,ID_numberCart,iDdrive_DAY,destination,Time,user,sorting FROM Deportees_DAY')
            else:
                cursor.execute('SELECT ID,namedeportees,Gender,agedeportees,ID_numberCart,Imageurl,iDdrive_DAY,destination,Time FROM Deportees_DAY')
            data_her = cursor.fetchall()
            # print(data_her)
            return data_her
        except sqlite3.IntegrityError:
            pass 
        connect.close()




    #******************************************************************************************
    #  list_vierfy
    def insert_verify(name,ID_numberCart,type_difference,count_difference,kind_list,user):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            table = """INSERT INTO list_vierfy (name,ID_numberCart,type_difference,count_difference,kind_list,user) VALUES (?,?,?,?,?,?)"""
            table_data =(name,ID_numberCart,type_difference,count_difference,kind_list,user)
            cursor.execute(table,table_data)
            connect.commit()
        except sqlite3.IntegrityError:
                pass
        connect.close()




# *******************************************************************************************
        # CREATE TABLE IF NOT EXISTS Loads_today 
        #     (ID INTEGER PRIMARY KEY AUTOINCREMENT,type_payload TEXT NULL ,amount_payload INTEGER NULL,Sender TEXT NULL,
        #     ID_numberCart_SINDER INTEGER  NULL,Recipient TEXT NULL,phone INTEGER NULL,
        #     name_office TEXT NULL, drive_name TEXT NULL,destination TEXT NULL,kind_oprtion TEXT NULL)

    def insert_message(Id,type_payload,amount_payload,Sender,ID_numberCart_SINDER,sender_phone,
                       Recipient,phone_recipient,ID_numberCart_recipient,name_office,drive_name,destination,kind_oprtion,user,sorting,kind_opr=None):
        connect = sqlite3.connect(nameData())
        try:
            cursor = connect.cursor()
            if kind_opr is None:
                table = """INSERT INTO Loads_today (ID,type_payload,amount_payload,Sender,ID_numberCart_SINDER,sender_phone,Recipient,phone_recipient,ID_numberCart_recipient,
                            name_office,drive_name,destination,kind_oprtion,user,sorting)VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
                table_data = (Id,type_payload,amount_payload,Sender,ID_numberCart_SINDER,
                              sender_phone,Recipient,phone_recipient,ID_numberCart_recipient,
                              name_office,drive_name,destination,kind_oprtion,user,sorting)
                cursor.execute(table,table_data)
            else:
                table_u = """UPDATE Loads_today  SET type_payload=?,amount_payload=?,Sender=?
                            ,ID_numberCart_SINDER=?,sender_phone=?,Recipient=?,phone_recipient=?,ID_numberCart_recipient=?,name_office=?,
                            drive_name=?,destination=?, kind_oprtion=?,user=?, sorting=? WHERE ID=?"""
                table_data_u = (type_payload,amount_payload,Sender,ID_numberCart_SINDER,
                                sender_phone,Recipient,phone_recipient,ID_numberCart_recipient
                                ,name_office,drive_name,destination,kind_oprtion,user,sorting,Id)
                cursor.execute(table_u,table_data_u)
            connect.commit()
        except sqlite3.IntegrityError:
               pass
        connect.close()





        
    def get_message(kind=None,time=None,text=None,sort=None):
        connect = sqlite3.connect(nameData())
        try:
            cursor= connect.cursor()
            if kind is None:
                cursor.execute("SELECT * FROM Loads_today")
            elif kind == 'month':
                cursor.execute("SELECT COUNT(*) FROM Loads_today WHERE Time=? AND trim(kind_oprtion)=trim(?) AND sorting=?",[str(time),text,sort])
            else:
                cursor.execute("SELECT COUNT(*) FROM Loads_today WHERE strftime('%Y-%m',Time)=? AND trim(kind_oprtion)=trim(?) AND sorting=?",[str(time),text,sort])
            data_bies = cursor.fetchall()
            print(data_bies)
            return data_bies
        except sqlite3.IntegrityError:
                pass