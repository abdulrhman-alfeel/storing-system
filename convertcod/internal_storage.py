import sqlite3
from datetime import datetime
from convertcod.json_parse import json_parse
from convertcod.json_stringify import json_stringify
from convertcod.processor import resource_path
import gc
# from convertcod.processor import resource_path
import os
cache={'page':'new'}
# Set the value of the key to the JSON-serialized newTasks list.
def set_itemx(userName,kindMovment):
    get_virfe()
    if len(userName) > 0:
        stayuser = 'true'
        if kindMovment.replace(" ",'') == 'خروج المستخدم'.replace(" ","") or kindMovment.replace(" ",'') == 'اغلاق'.replace(" ","") or kindMovment.replace(" ",'') == 'تقليص اعتمادات البترول'.replace(" ","") or kindMovment.replace(" ",'') == 'تقليص اعتمادات الديزل'.replace(" ","") :
                stayuser = 'false'
                starttabel = "INSERT INTO movement (userName,datamovement,kindMovement,stayuser,dataExet) VALUES (?,?,?,?,?)"
                datatabel = (userName,str(datetime.now()),kindMovment,stayuser,str(datetime.now()))
        else:
            starttabel = "INSERT INTO movement (userName,datamovement,kindMovement,stayuser) VALUES (?,?,?,?)"
            datatabel = (userName,str(datetime.now()),kindMovment,stayuser)
        conntd = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
        try:
            cursor =conntd.cursor()
            if len(navigation) > 0 :
                tabelUpdet = 'UPDATE movement SET stayuser="false", dataExet=? WHERE stayuser ="true"'
                cursor.execute(tabelUpdet,[str(datetime.now())])
                cursor.execute(starttabel,datatabel)
            else:
                cursor.execute(starttabel,datatabel)
            conntd.commit()
        except sqlite3.IntegrityError:
            print('Error')
        conntd.close()
        gc.collect()
    
def InsertJson(oprtion):
    try:
        naviga= get_virfe()
        array=  naviga["arrayMovement"]  
        array.append(oprtion)
        json = list(array)

        j= json_stringify(json)
        # print(j,naviga['ID'])
        # connta = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
        connta =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
        cursor= connta.cursor()
        try:
            tabelUpdet = 'UPDATE movement SET arrayMovement=? WHERE stayuser="true" '
            cursor.execute(tabelUpdet,[j])
            connta.commit()
        except sqlite3.IntegrityError:
            print('Error in sqlite')
        connta.close()
    except ValueError:
        print('error data tembty')
    gc.collect()

def get_virfe():
    global navigation
    navigation = {}
    # connta = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    connta =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor =connta.cursor()
        tabelUpdet = 'SELECT * FROM movement WHERE stayuser="true"'
        cursor.execute(tabelUpdet)
        DATAnav = cursor.fetchall()
        # print(DATAnav)
        if len(DATAnav) > 0 and DATAnav is not None:
            for i in DATAnav:
                    navigation["ID"] = i[0]
                    navigation["userName"] = i[1]
                    navigation["datamovement"] = i[2]
                    navigation["kindMovment"] = i[3]
                    navigation["stayuser"] = i[4]
                    jsonData = i[6]
                    if jsonData is not None and len(jsonData) > 0 :
                         navigation["arrayMovement"] = json_parse(jsonData)
                    else:
                         navigation["arrayMovement"] = []
            # print(navigation)
        if len(DATAnav) > 0:
            # print(navigation)
            return navigation
        else:
            return {"kindMovment":""}
    except sqlite3.IntegrityError:
        print('Error', sqlite3.IntegrityError)
    connta.close()
    gc.collect()
nav = {}

def get_itemx():
    arraymovem = []
    # global arraymovem
    # conntad = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    conntad =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    cursor =conntad.cursor()
    try:
        cursor.execute('SELECT * FROM movement')
        DATAd = cursor.fetchall()

        for i in range(len(DATAd)):
                arraymovem.append({"ID":DATAd[i][0],"userName":DATAd[i][1],"datamovement":DATAd[i][2],"kindMovment": DATAd[i][3],"stayuser":DATAd[i][4],'arrayMovement':DATAd[i][6]})
                # nav={}
        # print(arraymovem)
        if len(DATAd) > 0:
            return arraymovem
     
    except sqlite3.IntegrityError:
        print('Error', sqlite3.IntegrityError)
    conntad.close()
    gc.collect()    
    # json_tasks = cache.get(key)
    # if json_tasks is None:
    #     return None
    # else:
    #     return json_tasks

#تحديد ملف حفظ بطائق الاعتمادات
def insert_select(selecter,kind):
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        if kind == "insert":
            tabelselect = 'INSERT INTO selectAdddir (dircarteAdd ) VALUES(?)'
            cursor.execute(tabelselect,[selecter])
        else:
            tableselectupdat = 'UPDATE selectAdddir SET dircarteAdd= ? '
            cursor.execute(tableselectupdat,[selecter])
        coon.commit()
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()
def get_select():
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        tabelselect = 'SELECT * FROM selectAdddir'
        cursor.execute(tabelselect)
        data = cursor.fetchall()
        return data
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()
        
#تحديد ملف حفظ الطباعة
def insert_selectprinter(selecter,kind):
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        if kind == "insert":
            tabelselect = 'INSERT INTO selectPrinter (dircarteUsb) VALUES(?)'
            cursor.execute(tabelselect,[selecter])
        else:
            tableselectupdat = 'UPDATE selectPrinter SET dircarteUsb=? '
            cursor.execute(tableselectupdat,[selecter])
        coon.commit()
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()
# لاستعلام عن المنفذ
def get_selectprinter():
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        tabelselect = 'SELECT * FROM selectPrinter'
        cursor.execute(tabelselect)
        data = cursor.fetchall()
        if len(data) > 0 :
            return data
        else:
            return []
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()

def insert_selectData(selecter,kind):
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        if kind == "insert":
            tabelselect = 'INSERT INTO selectData (dirDatabase) VALUES(?)'
            cursor.execute(tabelselect,[selecter])
        else:
            tableselectupdat = 'UPDATE selectData SET dirDatabase=? '
            cursor.execute(tableselectupdat,[selecter])
        coon.commit()
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()
# لاستعلام عن المنفذ
def get_selectData():
    # coon = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    coon =  sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor = coon.cursor()
        tabelselect = 'SELECT * FROM selectData'
        cursor.execute(tabelselect)
        data = cursor.fetchall()
        if len(data) > 0 :
            return data
        else:
            return []
    except sqlite3.IntegrityError:
        print("sqlite problem")
    coon.close()
