from tkinter import *
from tkinter import ttk, messagebox
from convertcod.internal_storage import insert_selectprinter , get_selectprinter
from convertcod.TOPlevel import Moudel
from convertcod.userfind import findUser ,responsebletUser
def insrt_printer():
    array = get_selectprinter()
    if len(array) <= 0:
        insert_selectprinter(boxselecter.get(),'insert')
        # boxselecter.delete(0,"end")
        messagebox.showinfo(message='تمت العملية بنجاح')
    else:
        insert_selectprinter(boxselecter.get(),'update')
        # boxselecter.delete(0,"end")
        messagebox.showinfo(message='تمت العملية بنجاح')
    
def SelectPrinter(master):
    # if findUser() == True:
        # usersactyle = responsebletUser()
        # if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
            global boxselecter
            level = Moudel(master,'حدد منفذ')
            array = get_selectprinter()
            find = next((item[1] for item in array),None)
            labelTextFrom = ttk.LabelFrame(level,text='حدد منفذ الطابعة ',width=100)
            labelTextFrom.grid(row=1,column=3,pady=15)
            boxselecter = ttk.Entry(labelTextFrom,width=45)
            boxselecter.pack(padx=30,pady=10,fill='both',anchor='center')
            if find is not None:
                boxselecter.insert(0,find)
            boxselecter.bind("<FocusIn>", lambda e:boxselecter.delete(0,"end"))
            funcjop = ttk.Button(labelTextFrom,text='ادخال',command=insrt_printer) 
            funcjop.pack(side='bottom',fill='both',anchor='center',padx=30,pady=30)
        # else:
            # messagebox.showwarning(title="صلاحية المسؤل",message='ليس لديك الصلاحية الكافية ')
            

def conectionEngneer(master):
    global Software
    level = Moudel(master,'للتواصل بالدعم')
    labelTextFrom = ttk.LabelFrame(level,text='للتواصل بالدعم او الاستفسار ',width=100)
    labelTextFrom.grid(row=1,column=3,pady=15,padx=25)
    Software = ttk.Label(labelTextFrom,text="م/عبدالرحمن الفيل")
    Software.pack(padx=30,pady=10)
    funcjop = ttk.Label(labelTextFrom,text='+966 502927536') 
    funcjop.pack(side="left",fill='both',anchor='center',padx=30,pady=30)
    funcjoptext = ttk.Label(labelTextFrom,text='+967 775227593') 
    funcjoptext.pack(side='left',fill='both',anchor='center',padx=30,pady=30)
    # level.overrideredirect(True)
