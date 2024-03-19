from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.internal_storage import *
# from PIL.ImageTk import PhotoImage


class LoginPage(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        def toggle_mode():
            if mode_switch.instate(["selected"]): 
                controller.call("set_theme","light")
            else: 
                controller.call("set_theme","dark")
        button = ttk.Button(self, text="اغلاق", command=lambda:self.quit())
        button.pack(side='right',anchor='ne',pady=5,padx=5)
        mode_switch = ttk.Checkbutton(self, text="تبديل", style="Switch.TCheckbutton", command=toggle_mode)
        mode_switch.pack(side='top',pady=5,padx=5)
        self.newPage(controller)  
    def founInsert(self,controller):
        try:
            userName = name_pach.get()
            passworduser = password_entry.get()
            if  len(userName) > 0 and userName != 'ادخل اسم المستخدم' and len(passworduser) > 0 and passworduser != 'ادخل كلمة مرور' :
                dataNvigat = get_itemLogin(passworduser, userName)
                if len(dataNvigat) > 0 :
                    set_itemx(userName,'بد الدخول')
                    controller.Show_frame(controller.page1)
                    set_itemx(userName,'الفرز')
                    name_pach.delete(0,'end')
                    name_pach.insert(0,'ادخل اسم المستخدم')
                    password_entry.delete(0,'end')
                    password_entry.insert(0,'ادخل كلمة مرور')       
        except: 
            print('error')
    def newPage(self,controller):
            global name_pach
            global password_entry
            viewicontener = ttk.Frame(self)
            viewicontener.pack(anchor='n',fill='none',padx=20,pady=20)
            Labelframe = ttk.Frame(viewicontener)
            Labelframe.grid(row=0,column=0,sticky="nsew")
            widgets_frame = ttk.LabelFrame(viewicontener,width=300,height=700)
            widgets_frame.grid(row=1,column=0,sticky="nsew")
            pachNew = ttk.Frame(widgets_frame)
            pachNew.grid(row=0,column=0,pady=15,padx=5)
            text_kind = ttk.Label(pachNew,text="اسم المستخدم")
            text_kind.grid(row=0,column=0,padx=15,pady=15)
            name_pach = ttk.Entry(pachNew,width=35,justify='right')
            name_pach.grid(row=1, column=0,padx=5, pady=15, sticky="ew")
            name_pach.insert(0,'ادخل اسم المستخدم')
            name_pach.bind("<FocusIn>", lambda e:name_pach.delete(0,'end'))
            pachSpent = ttk.Frame(widgets_frame,width=50)
            pachSpent.grid(row=1,column=0,pady=15,padx=5)
            Spnlabltext = ttk.Label(pachSpent,text="كلمة المرور")
            Spnlabltext.grid(row=0,column=0)
            password_entry= ttk.Entry(pachSpent,width=35,justify='right',show="*")
            password_entry.grid(row=1, column=0,padx=5, pady=15, sticky="ew")
            password_entry.insert(0,'ادخل كلمة مرور')
            password_entry.bind("<FocusIn>",lambda e: password_entry.delete(0,'end'))
            password_entry.bind("<KeyRelease>",lambda event:self.on_press(controller,event))
            kindspent_entry =ttk.Button(widgets_frame,text="دخول",command=lambda :self.founInsert(controller),width=20)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=25)
     
    def on_press(self,controller,event):
        if event.keysym == "Return" :
            self.founInsert(controller)
        # ttk.Button(self,text="Register",width="30",command=lambda:controller.Show_frame(controller.page3)).pack()
