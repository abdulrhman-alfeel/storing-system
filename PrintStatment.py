
from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from Print.PrintDay import *

# from tkPDFViewer import tkPDFViewer as pdf
from sqiltyFoun import *
from datetime import datetime ,timedelta 

class PrintStatment(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.frames = {}
        self.Date = []
        global controll 
        global viewimage

        controll=controller
        start_data = datetime(2023,9,1)
        end_data = datetime(2030,9,1)
        for day in range((end_data - start_data).days +1):
                databis = start_data + timedelta(days=day)
                self.Date.append(databis.date())  
        
        viewlyuot = ttk.LabelFrame(self,width=300)
        viewlyuot.pack(side='right',padx=50)
        
        print_Trovels =ttk.Button(viewlyuot,text="المسافرين",command=lambda:self.select_printe('Trovels') ,padding=(5,5))
        print_Trovels.pack(side="top",anchor="center",padx=20,pady=20)
        print_Message =ttk.Button(viewlyuot,text="الرسائل والودائع" ,command=lambda:self.select_printe('Message') ,padding=(7,7))
        print_Message.pack(side="top",anchor="center",padx=20,pady=20)   
        print_Prohibited =ttk.Button(viewlyuot,text="المضبوطات" ,command=lambda: self.select_printe('Prohibited'),padding=(7,7) )
        print_Prohibited.pack(side="top",anchor="center",padx=20,pady=20) 
        print_Deportees =ttk.Button(viewlyuot,text="المرحلين" ,command=lambda: self.select_printe('Deportees'),padding=(7,7) )
        print_Deportees.pack(side="top",anchor="center",padx=20,pady=20) 
        print_Wanted =ttk.Button(viewlyuot,text="المضبوطين" ,command=lambda: self.select_printe('wanted'),padding=(7,7) )
        print_Wanted.pack(side="top",anchor="center",padx=20,pady=20) 




        viewimage = ttk.Frame(self,width=300,border=2,borderwidth=2)
        viewimage.pack(pady=150)
        imageman = ttk.Label(viewimage,image=controller.man,width=300)
        imageman.pack(side='left',fill='both')
        # imageman.place(x=350,y=10,anchor='center')

        self.continerView("Trovels")




    def select_printe(self,kindprint):
        for view in viewimage.winfo_children():
            view.destroy()
        imageman = ttk.Label(viewimage,image=controll.man,width=300)
        imageman.pack(side='left',fill='both')
        self.continerView(kindprint)

    def continerView(self,kindprint):
        textH1 = 'بيانات الكوشن(المسافرين)'
        match kindprint:
            case 'Trovels':
                textH1= 'بيانات الكوشن(المسافرين)'
            case "Message":
                textH1 = 'بيانات الرسائل والودائع'
            case "Prohibited":
                textH1 = 'بيانات المضبوطات'
            case "Deportees":
                textH1 = "بيانات المرحلين"
            case "wanted": 
                textH1 = "بيانات المضبوطين"

        viewB = ttk.Frame(viewimage,width=50)
        viewB.pack(side='right',fill='both')  
        title = ttk.Label(viewB,text=textH1,font=("Tajawal",25))
        title.pack(side='top',padx=10,pady=30)
        print_day =ttk.Button(viewB,text="طباعة تقارير يومية",command=lambda:self.switchFUNCTION(print_day,'day',kindprint) ,width=35,padding=(5,5))
        print_day.pack(side="top",anchor="ne",padx=20,pady=20)
        print_month =ttk.Button(viewB,text="طباعة تقارير شهرية",command=lambda:self.switchFUNCTION(print_month,'month',kindprint) ,width=35,padding=(7,7))
        print_month.pack(side="top",anchor="ne",padx=20,pady=20)   
        print_yurs =ttk.Button(viewB,text="طباعة تقارير سنوية",command=lambda: self.switchFUNCTION(print_yurs,'yrs',kindprint),width=35,padding=(7,7) )
        print_yurs.pack(side="top",anchor="ne",padx=20,pady=20) 
        
      
        
        # view = ttk.Frame(viewimage)
        # view.pack(side='bottom')
        # select_TextentryD = ttk.Label(viewimage,text="من إلى ")
        # select_TextentryD.pack()
        # select_TextentryD = ttk.Label(view,text="من تاريخ")
        # select_TextentryD.grid(row=1,column=1,padx=10,pady=10)
        
        # select_entryD = ttk.Combobox(view,values=self.Date,width=35)
        # select_entryD.grid(row=2,column=1 ,padx=10,pady=10,sticky='nesw')
        # select_entryD.set(self.Date[0])
        
        # select_toData = ttk.Label(view,text="حتى تاريخ")
        # select_toData.grid(row=1,column=0,padx=10,pady=10)
        
        # select_toDataday = ttk.Combobox(view,values=self.Date,width=35)
        # select_toDataday.grid(row=2,column=0 ,padx=10,pady=10,sticky='nesw')
        # select_toDataday.set(self.Date[0])
        
        # print_to =ttk.Button(view,text="طباعة",command=lambda:self.switchFUNCTION(print_to,'BETWEENPRINT') )
        # print_to.grid(row=3,column=1 ,padx=15,pady=10,sticky='nesw')
        # print_toview =ttk.Button(view,text="عرض", command=lambda:self.switchFUNCTION(print_toview,'BETWEENVIEO') )
        # print_toview.grid(row=3,column=0 ,padx=15,pady=10,sticky='nesw')


        
    def switchFUNCTION(self,print,text,kindprint): 
        user =get_item()
        popUpMenu = Menu(print, tearoff=0, border=0,borderwidth=5)
        if text == 'month':
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='print',TIme='month'))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='view',TIme='month'))
            popUpMenu.add_separator()  
        elif text == 'yrs':  
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='print',TIme='Yars'))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='view',TIme='Yars'))
            popUpMenu.add_separator()  
        # elif text == 'BETWEENVIEO':
        #     popUpMenu.add_separator()
        #     popUpMenu.add_command(label="عرض بالسرد اليومي", accelerator=" ",command=lambda : printDay(kindprint,"user['userName']",print))
        #     popUpMenu.add_separator()
        #     popUpMenu.add_command(label="عرض بالسرد الشهري", accelerator=" ",command=lambda :register_user(varfetc={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"view",'page':print,"user":user['userName']}))  
        #     popUpMenu.add_separator()
        # elif text == 'BETWEENPRINT':
        #     popUpMenu.add_separator()
        #     popUpMenu.add_command(label="طباعة بالسرد اليومي", accelerator=" ",command=lambda : printDay(kindprint,"user['userName']",print))
        #     popUpMenu.add_separator()
        #     popUpMenu.add_command(label="طباعة بالسرد الشهري", accelerator=" ",command=lambda :register_user(varfetc={"type": "BETWEEN","younger-then":select_toDataday.get() ,"bigger":select_entryD.get(),'kindjop':"print",'page':print,"user":"user['userName']"}))  
        #     popUpMenu.add_separator()
        else:
            popUpMenu.add_separator()
            popUpMenu.add_command(label="طباعة", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='print',TIme='day'))
            popUpMenu.add_separator()
            popUpMenu.add_command(label="عرض", accelerator=" ",command=lambda: printDay(kindprint,user['userName'],print,kind='view',TIme='day'))
            popUpMenu.add_separator()  
        infox = print.winfo_rootx()
        infoy = print.winfo_rooty()
        popUpMenu.post(infox,infoy)      