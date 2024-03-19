import sqlite3
from tkinter import messagebox
from convertcod.json_parse import json_parse
from convertcod.processor import resource_path;
# from convertcod.processor import resource_path
import os
def set_item(username,password,responsibil,jsonRespons):
    # connt = sqlite3.connect('.\\assets\\backup\\data_storng.db')
    connt = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
            cursor =connt.cursor()
            tabelUpdet = 'INSERT INTO logtion (userName,passwordUSER,Responsibilities,jsonResponsibilities) VALUES(?,?,?,?)'
            datatable = (username,password,responsibil,jsonRespons)
            # cursor =cursor.execute(tabelUpdet,[new_tasks])
            cursor.execute(tabelUpdet,datatable)
            connt.commit()
    except sqlite3.IntegrityError:
        messagebox.showwarning(title="Error",message="المستخدم موجود بالفعل")
    connt.close()
    
def Updat_item(key,username,password,jsonRespons):
    # connt =  sqlite3.connect('.\\assets\\backup\\data_storng.db')
    connt = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
            cursor =connt.cursor()
            tabelUpdet = 'UPDATE logtion SET userName=?,passwordUSER=?,jsonResponsibilities=? WHERE ID=?'
            datatable = (username,password,jsonRespons,key)
            # cursor =cursor.execute(tabelUpdet,[new_tasks])
            cursor.execute(tabelUpdet,datatable)
            connt.commit()
            messagebox.showwarning(title="Error",message="تمت العملية بنجاح")
    except sqlite3.IntegrityError:
        messagebox.showwarning(title="Error",message="المستخدم موجود بالفعل")

    connt.close()
    
    
def get_itemLogin(passwordUSER, userName):
    # global navigationLogin
    navigationLogin = {}
    # conntcxt =  sqlite3.connect('.\\assets\\backup\\data_storng.db')
    conntcxt = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    cursor =conntcxt.cursor() 
    try:
        tabelUpdet = ' SELECT * FROM logtion WHERE trim(passwordUSER) = trim(?) AND trim(userName) =trim(?) '
        # dataLogin = ()
        cursor.execute(tabelUpdet,[passwordUSER,userName])
        DATAnav = cursor.fetchall()
        if len(DATAnav) > 0 :
            for i in DATAnav:
                    navigationLogin["ID"] = i[0]
                    navigationLogin["userName"] = i[1]
                    navigationLogin["passwordUSER"] = i[2]
                    navigationLogin["Responsibilities"] = i[3]
                    navigationLogin['jsonResponsibilities'] =  i[4]
                    navigationLogin["datatim"] = i[5]
            # print(navigationLogin,'hiiii')
            set_itemActivite(navigationLogin) 
            return navigationLogin
        else:
              messagebox.showwarning(title="Error",message="كلمة المرور او اسم المستخدم غير صحيح")
    except sqlite3.IntegrityError:
        messagebox.showwarning(title="Error",message="هناك مشكلة في الوصول إلى البيانات")
        print('Error')
    conntcxt.close()

def get_loginAll():
    try:
        # coniction =  sqlite3.connect('.\\assets\\backup\\data_storng.db')
        coniction = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
        try:
            cursor = coniction.cursor()
            cursor.execute('SELECT * FROM logtion')
            dataAll = cursor.fetchall()  
            # print(dataAll) 
            if dataAll is not None :
                return dataAll
            else:
                return []
        except sqlite3.IntegrityError:
            messagebox.showwarning(title="Error",message= 'هناك مشكلة في الوصول للقاعدة ')     
        coniction.close()
    except sqlite3.IntegrityError:
        return None
    
def set_itemActivite(new_tasks):
    # print(json_parse(new_tasks["jsonResponsibilities"]))
    navigation =get_item()
    # conntdw = sqlite3.connect('.\\assets\\backup\\data_storng.db')
    conntdw = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor =conntdw.cursor()
        # print("hlllow")
        if len(navigation) > 0 :
            cursor.execute('''UPDATE logtionActivite SET activity ="false"''')
            tabelUpdet = 'INSERT INTO logtionActivite (userName,passwordUSER,Responsibilities,activity,jsonResponsibilities) VALUES(?,?,?,"true",?)'
            datatable = (new_tasks['userName'],new_tasks['passwordUSER'],new_tasks['Responsibilities'],new_tasks["jsonResponsibilities"])
            cursor.execute(tabelUpdet,datatable)
        else:
            tabelUpdet = '''INSERT INTO logtionActivite (userName,passwordUSER,Responsibilities,activity,jsonResponsibilities) VALUES(?,?,?,"true",?)'''
            datatable = (new_tasks['userName'],new_tasks['passwordUSER'],new_tasks['Responsibilities'],new_tasks["jsonResponsibilities"])
            cursor.execute(tabelUpdet,datatable)
        conntdw.commit()
    except sqlite3.IntegrityError:
        print('Error')
    conntdw.close()
    
def get_item():
    # global navigation
    # conntas =  sqlite3.connect('.\\assets\\backup\\data_storng.db')
    conntas = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
        cursor =conntas.cursor()
        tabelUpdet = 'SELECT * FROM logtionActivite WHERE activity="true"'
        # tabelUpdet = 'SELECT * FROM logtionActivite'
        cursor.execute(tabelUpdet)
        loginActiv = cursor.fetchall()
        navigation = {}
        arraymov =[]
        # print(loginActiv)
        if len(loginActiv) > 0:
            for i in loginActiv:
                # print(json_parse(i[5]))
                navigation["ID"] = i[0]
                navigation["userName"] = i[1]
                navigation["passwordUSER"] = i[2]
                navigation["Responsibilities"] = i[3]
                navigation["activity"] = i[4]
                navigation["jsonResponsibilities"] = json_parse(i[5])
                navigation["datatim"] = i[6]
        return navigation
    except sqlite3.IntegrityError:
        print('Error')
    conntas.close()
    
def set_loguot():
    # connt =  sqlite3.connect('.\\assets\\backup\\data_storng.db')
    connt = sqlite3.connect(resource_path('assets\\backup\\data_storng.db'))
    try:
            cursor =connt.cursor()
            tabelUpdet = 'UPDATE logtionActivite SET activity ="false" '
            cursor.execute(tabelUpdet)
            connt.commit()
    except sqlite3.IntegrityError:
        print('Error', sqlite3.IntegrityError)
    connt.close()
    
