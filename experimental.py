from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.internal_storage import *
import uuid
from convertcod.backup import *
import re
# from PIL.ImageTk import PhotoImage
arrayProject = ["6be36d80-6b20-4a01-8411-dee0df36df1e",
                "1a3dd455-ea62-40b9-8a83-e9b497cb3c69",
                "438d5bd0-9265-4245-8f88-1577bcde5245",
                "04508349-3eef-4a2b-accd-0c57c28fa9c5",
                ]
abdu = uuid.uuid4()
print(abdu)
class Experimental(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global contd
        contd = controller
        def toggle_mode():
            if mode_switch.instate(["selected"]): 
                controller.call("set_theme","light")
            else: 
                controller.call("set_theme","dark")
        button = ttk.Button(self, text="اغلاق", command=lambda:self.quit())
        button.pack(side='right',anchor='ne',pady=5,padx=5)
        mode_switch = ttk.Checkbutton(self, text="تبديل", style="Switch.TCheckbutton", command=toggle_mode)
        mode_switch.pack(side='top',pady=5,padx=5)
        self.newPage()  
    def founInsert(self):
            IMed= False
        # try:           
            passworduser = password_entry.get()
            # data = next((item for item in arrayProject if passworduser.lower() == item.lower() ),None)
        
            if  passworduser.lower() == "6be36d80-6b20-4a01-8411-dee0df36df1e".lower():
                    print('geeeg')
                    UPDATActivate()
                    print("goog")
                    UPDATActivateLMIT(7)
                    print('goooogfanl')
                    IMed= True
            elif  passworduser.lower() == "1a3dd455-ea62-40b9-8a83-e9b497cb3c69".lower():
                    UPDATActivate()
                    UPDATActivateLMIT(30)
                    IMed= True
            elif  passworduser.lower() ==  "438d5bd0-9265-4245-8f88-1577bcde5245".lower():
                    UPDATActivate()
                    UPDATActivateLMIT(180)
                    IMed= True
            elif  passworduser.lower() ==  "04508349-3eef-4a2b-accd-0c57c28fa9c5".lower():
                    UPDATActivate()
                    UPDATActivateLMIT(360)
                    IMed= True
            else:
                    messagebox.showwarning(title="خطاء",message='رقم المونتج غير صالح الرجاء التاكد من الرقم او التواصل بالدعم الفني واخباره بالمشكلة الحاصلة')
                    IMed = False
            if IMed == True:   
                if get_loginAll() is not None or len(get_loginAll) > 0:
                        usercount = get_loginAll()  
                else:
                        usercount = []
                if len(usercount) > 0 :
                        countentr = contd.page2 
                else:
                        countentr = contd.page1
             
                contd.Show_frame(countentr)
                    
        # except: 
            # print('error')
    def newPage(self):
            global password_entry
            viewicontener = ttk.Frame(self)
            viewicontener.pack(anchor='n',fill='none',padx=20,pady=20)
            Labelframe = ttk.Frame(viewicontener)
            Labelframe.grid(row=0,column=0,sticky="nsew")
            try:
                    label=ttk.Label(Labelframe, text="محطة السلام للوقود",font=("Tajawal",35))
                    label.grid(row=0,column=2,sticky="nsew",padx=40)
                #     label=ttk.Label(Labelframe, image=contd.bg)
                #     label.grid(row=0,column=0,sticky="nsew")
            except IOError:
                print('error image')
                
     
            widgets_frame = ttk.LabelFrame(viewicontener, padding=(20,15),width=300,height=700)
            widgets_frame.grid(row=1,column=0,sticky="nsew")
            labelTextFrom = ttk.LabelFrame(widgets_frame,text='للتواصل بالدعم او الاستفسار ',width=100)
            labelTextFrom.grid(row=0,column=0,pady=15,padx=25)
            Software = ttk.Label(labelTextFrom,text="م/عبدالرحمن الفيل")
            Software.pack(padx=30,pady=10)
            funcjop = ttk.Label(labelTextFrom,text='+966 502927536') 
            funcjop.pack(side="left",fill='both',anchor='center',padx=30,pady=30)
            funcjoptext = ttk.Label(labelTextFrom,text='+967 775227593') 
            funcjoptext.pack(side='left',fill='both',anchor='center',padx=30,pady=30)    
            pachSpent = ttk.Frame(widgets_frame,width=50)
            pachSpent.grid(row=2,column=0,pady=15,padx=5)
            Spnlabltext = ttk.Label(pachSpent,text="...ادخل رقم المنتج")
            Spnlabltext.grid(row=0,column=1)
            password_entry= ttk.Entry(pachSpent,width=35)
            password_entry.grid(row=0, column=0,padx=5, pady=15, sticky="ew")
            password_entry.insert(0,'رقم المنتج')
            password_entry.bind("<FocusIn>",lambda e: password_entry.delete(0,'end'))
            password_entry.bind("<KeyRelease>",lambda event:self.on_press(event))
            kindspent_entry =ttk.Button(widgets_frame,text="ادخال",command=self.founInsert,width=20)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=25, sticky="ew")
     
    def on_press(self,event):
        if event.keysym == "Return" :
            self.founInsert()
        # ttk.Button(self,text="Register",width="30",command=lambda:controller.Show_frame(controller.page3)).pack()
