from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MyClass_vew_Travels import MyClass_vew_Travels
from classupPush import MyClassPush
from classupSorted import SortedAdd
from classupTrovel import *
from QurySerch import *
from PrintStatment import PrintStatment
from sqiltyFoun import StationMonthSqly
from datetime import datetime  
from Print.PrintDay import *
from classupWanted import wanted
from classupwanted_Arrest import Arrest_wanted
from convertcod.internal_storage import *
from Register import Register
from RegisterEdite import RegisterEdite
from convertcod.internal_Loginstorge import *
from graph import graph
from classupOffice import MyClassOffice
from classupProhibited import Prohibited
from classupDeportees import Deportees
from classupDeposits import Deposits
from Print.viewpdf import switchMonth
from convertcod.userfind import findUser ,responsebletUser
from convertcod.insertSelectprinter import SelectPrinter, conectionEngneer
import gc
from selected_sorted import Selected_sorted
from backup_new.import_data import Backup_impot
import pyglet
from convertcod.backup import Backup, BackupView, Backend
from backup_new.takget_data import creat_databise_new
from backup_new.export_Admin import *




# aciton = 'new'
class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)

        # Navber = ttk.Frame(self,padding=5)
        pyglet.font.add_file("fount/Tajawal-Medium.ttf")
        global Reducing
        global widgets_frame

        global fromer_import
        global Print
        # المسافر
        global fromer_trovel
        # الفرزة
        global lable_list
        # المكاتب
        global lable_cash
        # السواقين
        global drive_cash
        # الممنوعات
        global lable_import
        # المطلوبين
        global sindrs_import
        # المرحلين
        global fromer_import
        # الرسائل
        global fromer_prodect
        
        global container
        global conter
        global DataSort
        global indexx
        indexx = 0
    
        def toggle_mode():
            if self.mode_switch.instate(["selected"]): 
                controller.call("set_theme","dark")
                controller.style.configure("Treeview", font=('Tajawal', 16),rowheight=40)
            else: 
                controller.call("set_theme","light")
                controller.style.configure("Treeview", font=('Tajawal', 16),rowheight=40)


        viewSpenِAllstationnavber = ttk.Frame(self)
        viewSpenِAllstationnavber.pack(side='top',anchor='ne',pady=2,padx=2,expand=True)
        
        buttonf = tk.Button(viewSpenِAllstationnavber,border=0, 
        text="تسجيل الخروج", command=lambda:self.Exetjop('exitUser',controller) )
        buttonf.grid(row=0, column=7, padx=2, pady=2,)
        buttones = tk.Button(viewSpenِAllstationnavber,border=0, 
                              text="فتح حساب", command=lambda:self.page_restrigint('open'))
        buttones.grid(row=0, column=6, padx=2, pady=2,)
        buttonq = tk.Button(viewSpenِAllstationnavber,border=0,
                             text="تعديل صلاحيات ",command=lambda:self.page_restrigint('edit'))
        buttonq.grid(row=0, column=5, padx=2, pady=2,)
        buttond = tk.Button(viewSpenِAllstationnavber,border=0, 
                             text="حركة الدخول", command=self.postPopUpMenu)
        buttond.grid(row=0, column=4, padx=2, pady=2,)

        Reducing = tk.Button(viewSpenِAllstationnavber,border=0, text="خيارات",command=self.Readucing)
        Reducing.grid(row=0, column=1, padx=2, pady=2,)



        self.mode_switch = ttk.Checkbutton(viewSpenِAllstationnavber, text="تبديل", style="Switch.TCheckbutton", command=toggle_mode)
        self.mode_switch.grid(row=0,column=0)
        
        widgets_frame = ttk.Frame(self)
        widgets_frame.pack(side='top',anchor='ne',pady=2,padx=2)

        lable_list = ttk.Button(widgets_frame,image=controller.sorter,
                                command=lambda:self.Show_frame(self.page5)
                                ,style="Accent.TButton")
        lable_list.grid(row=0,column=9,padx=6, pady=10)


        drive_cash = ttk.Button(widgets_frame,image=controller.driver,
        # ,style="Accent.TButton",
        command=lambda:self.Show_frame(self.page1))
        drive_cash.grid(row=0, column=8,padx=6, pady=10)


        fromer_trovel = ttk.Button(widgets_frame,image=controller.Travelers,
        # ,style="Accent.TButton",
        command=lambda:self.Show_frame(self.page16))
        fromer_trovel.grid(row=0, column=7,padx=6, pady=10)   


        lable_cash = ttk.Button(widgets_frame,image=controller.offices,
        # ,style="Accent.TButton",
        command=lambda:self.Show_frame(self.page2))
        lable_cash.grid(row=0, column=6,padx=6, pady=10)
        lable_import = ttk.Button(widgets_frame,image=controller.forbidden,
                                command=lambda:self.Show_frame(self.page12)
                                #   ,style="Accent.TButton"
                                                            )
        
        lable_import.grid(row=0, column=5,padx=6, pady=10)
        sindrs_import = ttk.Button(widgets_frame,image=controller.wanted,
                                   command=lambda:self.Show_frame(self.page13)
                                #    ,style="Accent.TButton"
                                   )

        sindrs_import.grid(row=0, column=4,padx=6, pady=10)
        fromer_import = ttk.Button(widgets_frame,image=controller.deportees,
        # ,style="Accent.TButton",
                                   command=lambda:self.Show_frame(self.page15))
        fromer_import.grid(row=0, column=3,padx=6, pady=10)      


        fromer_prodect = ttk.Button(widgets_frame,image=controller.sentpyloud ,
        # ,style="Accent.TButton",
                                   command=lambda:self.Show_frame(self.page17))
        fromer_prodect.grid(row=0, column=2,padx=6, pady=10)    

        quryserch = ttk.Button(widgets_frame, image=controller.search, command=self.searching)
        quryserch.grid(row=0, column=1, padx=6, pady=6)
        Print = ttk.Button(widgets_frame, image=controller.printer, command=self.printOprtion)
        Print.grid(row=0, column=0, padx=6, pady=6)  
     
        contin = ttk.Frame(self)
        # contin.grid(row=1,column=0,padx=40,pady=10)
        contin.pack(side='top',padx=10,pady=5)


        viewSpen = ttk.LabelFrame(contin)
        # viewSpen.grid(row=1,column=0,sticky="nsew",padx=40,pady=10)
        viewSpen.pack(side='right',padx=10,pady=5)


        container = ttk.LabelFrame(self)
        container.pack(side="top",anchor="center", expand=True)
        # fromAdd = ttk.Frame(container,padding=(2,2),width=150)
        # # fromAdd.place(x=1685,y=50)
        # fromAdd.grid(row=1,column=1,sticky='nsew')



        self.usercount = controller.usercount
        self.Add_png = controller.add
        self.Refresh = controller.revshe
        self.arrest = controller.arrest
        self.listarrest = controller.listarrest
        self.sorter = controller.sorter
        self.man = controller.man
        self.camera = controller.camera
        self.list_file = controller.list_file
        self.frames={}
        self.page1 = MyClassPush
        self.page2 = MyClassOffice
        self.page3 = QurySerch
        self.page4= MyClass_vew_Travels
        self.page5= SortedAdd
        self.page6= PrintStatment
        self.page7 = Register
        self.page8= RegisterEdite   
        self.page9 = graph
        # self.page9 = Trovel
        self.page10 = Trovel
        # self.page11 = SindrsEdit_travels
        self.page12 = Prohibited
        self.page13 = wanted
        self.page14 = Arrest_wanted
        self.page15 = Deportees
        self.page16 = Selected_sorted
        self.page17 = Deposits
        
        DataSort = StationMonthSqly.inComin_dataAll()
        conter = controller
        





        for F in (
            self.page1,
            self.page2,
                self.page3,
                self.page4,
                self.page5,
                self.page6,  
                self.page8,
                self.page7,
                # graph
                self.page9,
                self.page10,
                self.page12,
                self.page13,
                self.page14,
                self.page15,
                self.page17,
                self.page16
                
                ):
            frame= F(container,self)
            self.frames[F] = frame
            # frame.grid(row=1,column=0)
            frame.grid(row=1,column=0,sticky='nsew')

        currentpage = self.page5 if len(self.usercount) > 0 else self.page7

        self.Show_frame(currentpage)
            


    def selectt_active(self,button_page):
        for key in (fromer_trovel,lable_cash,lable_list,drive_cash,lable_import,sindrs_import,fromer_import,fromer_prodect):
            if key == button_page:
                key.config(style="Accent.TButton")
            else:
                key.config(style="")

    def Show_frame(self,context,data_kind=None):
        global indexx
        self.distripShow(context)
        userFind = responsebletUser()
        if findUser() == True:
            if userFind is not None:
                if context == self.page1:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر'):
                        self.Show_frame_translet(context,data_kind)  
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page2:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind['مندوب رسائل'] == 'true':
                        self.Show_frame_translet(context,data_kind)  
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')    
                elif context == self.page4:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind['مندوب فرزة'] == 'true':
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page5:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر'):
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page10 :
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind["مندوب فرزة"] == 'true':
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page14:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind["مندوب فرزة"] == 'true':
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page15:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind['مندوب فرزة'] == 'true':
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                elif context == self.page7:
                    try:
                        if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') :
                            self.Show_frame_translet(context,data_kind)
                        else:
                            messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                    except:
                        self.Show_frame_translet(context,data_kind)
                elif context == self.page8:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') :
                        self.Show_frame_translet(context,data_kind)
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')

                elif context == self.page16:
                    # if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') :
                        self.Show_frame_translet(context,data_kind)
                    # elif userFind["مندوب فرزة"].lower().replace(" ","") == 'true'.lower().replace(' ',""):
                    #     # print(userFind["نوع الفرزة"])
                    #     kindsorting = next((item for item in userFind["نوع الفرزة"] if item['value'] == True),None)
                    #     finding = next((pic for pic in DataSort if pic['nameSorting'] == kindsorting['name']),None)
                    #     j = {'sort':finding['nameSorting'],'IDsort':finding['IDsort'],"destination_Json":finding['destination_Json']}
                    #     self.Show_frame_translet(self.page10,j)
                    # else:
                    #     messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')


                elif context == self.page17:
                    if userFind['Responsibilities'].lower().startswith('المسؤل المباشر') or userFind['مندوب رسائل'] == 'true':
                        self.Show_frame_translet(context,data_kind)  
                    else:
                        messagebox.showwarning(title='صلاحيات',message='ليس لديك الصلاحيات الكافية')
                else :
                    self.Show_frame_translet(context,data_kind)  
            else :
                self.Show_frame_translet(context,data_kind)  
        else:
            self.Show_frame_translet(self.page7)
            indexx += 1
            if indexx > 1:
                messagebox.showwarning(title="اكمال عملية الدخول",message='يجب اكمال عملية اضافة مستخدم')



    def Show_frame_translet(self,context,data_kind=None):
        pageing = context
        user = get_item()
        # تبديل الصفحات من الكائن
        # self.distripShow(pageing)
        print(pageing)
        frame = self.frames[pageing] 
        frame.tkraise()   
        if len(user) > 0:
            if context == self.page1:
                self.page1.load_data(self)
                set_itemx(user['userName'],'صفحة السواقين')
                self.selectt_active(drive_cash)
            if context == self.page2:
                self.page2.load_data(self)
                set_itemx(user['userName'],'صفحة مكاتب الرسائل')
                self.selectt_active(lable_cash)
            if context == self.page4:
                self.page4.load_data(self)
                set_itemx(user['userName'],'صفحة عرض بيانات المسافر')
            if context == self.page5:
                self.selectt_active(lable_list)
                self.page4.load_data(self)
                set_itemx(user['userName'],'صفحة الفرز')
            if context == self.page10 and  isinstance(data_kind, int) :
                    print(data_kind)
                    self.selectt_active(fromer_trovel)
                    self.page10.Edit_data_travels(self=self.page10,idproc=data_kind)
                    set_itemx(user['userName'],'صفحة كوشن المسافر')
            elif context == self.page10 and not isinstance(data_kind, int) :
                self.page10.lodes_open(self,data_kind)
                self.selectt_active(fromer_trovel)
                set_itemx(user['userName'],'صفحة كوشن المسافر')
            else:
                print('not page10')
            if context == self.page9 :
                self.page9.loden(self=self.page9)
                set_itemx(user['userName'],'حركة المستخدم')
            if context == self.page12 :
                self.selectt_active(lable_import)
                self.page12.lodes(self=self.page12)
                set_itemx(user['userName'],'صفحة الممنوعات')
            if context == self.page13:
                self.selectt_active(sindrs_import)
                self.page13.lodes_open(self=self.page13)
                set_itemx(user['userName'],'المطلوبين امنياً')
            if context == self.page14:
                self.page14.lodes(self)
                self.selectt_active(sindrs_import)
                set_itemx(user['userName'],"ضبط مطلوب")
            if context == self.page14 and data_kind is not None:
                self.page14.lodes_data(self=self.page14,items=data_kind)
                set_itemx(user['userName'],"ضبط مطلوب")
            if context == self.page15:
                self.selectt_active(fromer_import)
                self.page15.lodes_deports(self)
                set_itemx(user['userName'],"صفحة المرحلين")
            if context == self.page7:
                set_itemx(user['userName'],"صفحة فتح حساب")
            if context == self.page8:
                set_itemx(user['userName'],"صفحة تعديل حساب")
                self.page8.loading(self=self.page8)

            if context == self.page16:
                self.selectt_active(fromer_trovel)
                data_sort =  StationMonthSqly.inComin_dataAllwitch()
                if len(data_sort) <= 0:
                    self.page5.verify_trovles(self)
                    pageing = self.page5
                    set_itemx(user['userName'],"صفحة الفرز")
                else:
                    set_itemx(user['userName'],"تحديد اسم الفرزة للكوشن")
                self.page16.loding_sorted()

            if context == self.page17:
                self.selectt_active(fromer_prodect)
                self.page17.swetch_data_page(self=self.page17)
                self.page17.lodens_open_deposits(self=self.page17)
                set_itemx(user['userName'],"صفحة الرسائل والودائع")



    #  هدم البناء 
    def distripShow(self,page):
        for Fd in (
            self.page1
                   ,self.page2,self.page3,self.page4,self.page5,self.page6,self.page8,self.page7,
                    self.page9,
                    self.page10,self.page12,self.page13,self.page14,self.page15,self.page16,self.page17):
            if Fd != page: 
                for widget in Fd.winfo_children(self):
                    widget.destroy
    
    


    def postPopUpMenu(self):
        if findUser() == True: 
            self.Show_frame(self.page9)         


    def vewBackup(self):
        BackupView()
        # pass


    def vewBackupEnd(self):
        Backend()
        pass


    def Readucing(self):
        try:
            if findUser() == True:
                usersactyle = responsebletUser()
                MaunReaducing = tk.Menu(Reducing, tearoff=0)
                copyBack = tk.Menu(MaunReaducing,tearoff=0)
                exportAdmin = tk.Menu(MaunReaducing,tearoff=0)
                importAdmin = tk.Menu(MaunReaducing,tearoff=0)
                MaunReaducing.add_command(label="تبديل منفذ الطابعة",underline=5,command=lambda:SelectPrinter(Reducing),accelerator=" ")
                if usersactyle['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
                    MaunReaducing.add_cascade(label="تصدير", menu=exportAdmin)
                    exportAdmin.add_command(label="البيانات الرئيسية",underline=5, command=BackupData_origin,accelerator=" ")
                    exportAdmin.add_separator()
                    exportAdmin.add_command(label="بيانات المتسخدم",underline=5, command=BackupData_user,accelerator=" ")
                    exportAdmin.add_separator()
                    MaunReaducing.add_cascade(label="استيراد", command=Backup_impot)
                else:
                    MaunReaducing.add_cascade(label="تصدير", command=creat_databise_new)
                    MaunReaducing.add_cascade(label="استيراد", menu=importAdmin)
                    importAdmin.add_command(label="البيانات الرئيسية",underline=5, command=Backup_data_origin_import,accelerator=" ")
                    importAdmin.add_separator()
                    importAdmin.add_command(label="بيانات المتسخدم",underline=5, command=Backup_data_user_import,accelerator=" ")
                    importAdmin.add_separator()

                MaunReaducing.add_cascade(label="نسخ احتياطي",underline=5,menu=copyBack,accelerator=" ")               
                copyBack.add_command(label="نسخ",underline=5, command=Backup,accelerator=" ")
                copyBack.add_separator()

                copyBack.add_command(label="استيراد",underline=5,command=self.vewBackup,accelerator=" ")
                copyBack.add_separator()
                copyBack.add_command(label="اعادة القاعدة الرسمية",underline=5,command=self.vewBackupEnd,accelerator=" ")
                copyBack.add_separator()
                MaunReaducing.add_command(label="للتواصل بالدعم",underline=5,command=lambda:conectionEngneer(Reducing),accelerator=" ")
                MaunReaducing.post(Reducing.winfo_rootx(),Reducing.winfo_rooty())
                # else:
                #     messagebox.showwarning(title="Error",message="ليس لديك الصلاحية الكافية لتنفيذ العملية")     
        except:
            print('error')


    def Exetjop(self,k,controller):
        # try:
            empty = {"userName":""}
            self.getuser = get_item() if len(get_item()) > 0 else empty
            if k == 'exitUser':
                if findUser() == True:
                    controller.Show_frame(controller.page2)
                    self.Show_frame(self.page5)
                    set_itemx(self.getuser['userName'],'خروج المستخدم')   
                    set_loguot()
        # except:
        #     self.quit()



    def printOprtion(self):
        if findUser() == True:
            user = responsebletUser()
            if user['Responsibilities'].replace(" ","") == 'المسؤول المباشر'.replace(" ","") or  user["طباعة تقرير يومي"].replace(" ","") == "true".replace(" ","") :
                self.Show_frame(self.page6)
            else:
                messagebox.showwarning(title="صلاحية", message='ليس لديك الصلاحية الكافية')

    
    def page_restrigint(self,k):
        if findUser() == True:
            user = get_item()
            # print(user)
            # print(user['jsonResponsibilities'])
            jsonRespon = user['jsonResponsibilities']
        if user['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") :    
            if k == 'open':
                self.Show_frame(self.page7)
            else:
                self.Show_frame(self.page8)
        else:
            messagebox.showwarning(title='صلاحية المسؤل المباشر',message='المعذرة ليس لديك الصلاحية الكافية')

    def searching(self):
        if findUser() == True:
            user = responsebletUser()
            if user['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") or user["البحث والاستعلام"].replace(" ","") == "true".replace(" ","") :    
                self.Show_frame(self.page3)
            else:
                messagebox.showwarning(title='صلاحية المسؤل المباشر',message='المعذرة ليس لديك الصلاحية الكافية')

    def wanted(self):
        if findUser() == True:
            user = responsebletUser()
            self.page13.lodes_open(self=self.page13,user_verfi=user)
            self.Show_frame(self.page13)