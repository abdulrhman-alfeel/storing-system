from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.json_stringify import json_stringify
from convertcod.internal_storage import set_itemx
from sqiltyFoun import StationMonthSqly
class Register(ttk.Frame):
    def __init__(self,parent,controller):
            ttk.Frame.__init__(self,parent)

            global name_pach
            global spent_entry
            global newimport
            global newAddcrides
            global backcomin
            global printstatmeent
            global newimport_chackbox
            global newAddcrides_chackbox
            global backcomin_chackbox
            global Printstatment_chackbox
            global edite_coshin
            global editecoshin
            global representative_message
            global checkarrys
            # global viewsort
            global deposits_chackbox
            global Printstatment_chackbox
            
            sorting =  StationMonthSqly.inComin_dataAll()
            checkarrys = []
            newimport = BooleanVar()
            newAddcrides= BooleanVar()
            backcomin = BooleanVar()
            representative_message= BooleanVar()
            printstatmeent = BooleanVar()
            editecoshin = BooleanVar()
            index= 0
            # imageArry = PhotoImage(file= "AERWICON.png")
            # imageArry.width =200

            widgets_frame = ttk.LabelFrame(self, text="تسجيل مستخدم",padding=(20,15))
            widgets_frame.pack(padx=20,pady=20)
            # widgets_frame.place(y=250,x=600)
      
            pachNew = ttk.Frame(widgets_frame)
            pachNew.grid(row=0,column=0,pady=15,padx=5)
            text_kind = ttk.Label(pachNew,text="...اسم المستخدم" )
            text_kind.grid(row=0,column=1,padx=15,pady=15)
           
            name_pach = ttk.Entry(pachNew,width=30)
            name_pach.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            name_pach.insert(0,'ادخل اسم المستخدم')
            name_pach.bind("<FocusIn>", lambda e:name_pach.delete(0,'end'))




            # viewsort= ttk.LabelFrame(widgets_frame,padding=10)
            # viewsort.grid_forget()
            # scrollbar = ttk.Scrollbar(viewsort, orient='vertical')
            # scrollbar.pack(side='right', fill='y')
            # # scrollbarhst = ttk.Scrollbar(viewsort,orient='horizontal')
            # # scrollbarhst.pack(side='bottom', fill='x')
            
            # canva = Canvas(viewsort ,bg="#313131",height=150,yscrollcommand=scrollbar.set)
            # canva.pack(fill='both',expand=True)

            # canva.bind("<Configure>",lambda e: canva.configure(scrollregion=canva.bbox("all")))
            # # scrollbarhst.config(command=canva.xview)
            # scrollbar.config(command=canva.yview)
            
            # upper_frame = ttk.Frame(canva)
            # canva.create_window((0,0),window=upper_frame,anchor='nw')
            # for pic in sorting:
            #     index+= 1
            #     text = ttk.Label(upper_frame,text=pic['nameSorting'])
            #     text.grid(row=index,column=1)
            #     coshin = BooleanVar()
                
            #     new_chackbox = ttk.Checkbutton(upper_frame,variable=coshin)
            #     new_chackbox.grid(row=index,column=0,sticky="nsew")
            #     new_chackbox.bind('<FocusIn>' ,lambda e=pic['nameSorting']:self.deletchack(e))
            #     checkarrys.append({"name":pic['nameSorting'],'value': coshin})
                


            viewChack= ttk.LabelFrame(widgets_frame,text='صلاحية المستخدم',padding=10)
            viewChack.grid(row=1,column=0,padx=20,pady=20)
            # البحث والاستعلام
            # طباعة تقرير يومي
            # اعادة طباعة الكوشن 
            # العمل على بيانات المسافرين
            # العمل على بيانات الحمولات والرسائل

            
            
            frame_one = ttk.Frame(viewChack)
            frame_one.grid(row=0,column=0,padx=10,pady=10) 
            textimport = ttk.Label(frame_one,text="البحث والاستعلام")
            textimport.grid(row=0,column=1)
            newimport_chackbox = ttk.Checkbutton(frame_one,variable=newimport)
            newimport_chackbox.grid(row=0,column=0,sticky="nsew")
            

            
            frame_towe = ttk.Frame(viewChack)
            frame_towe.grid(row=0,column=1,padx=10,pady=10) 
            textAddcrides = ttk.Label(frame_towe,text="طباعة تقرير يومي")
            textAddcrides.grid(row=0,column=1, sticky='nsew')
            newAddcrides_chackbox= ttk.Checkbutton(frame_towe,variable=newAddcrides)
            newAddcrides_chackbox.grid(row=0,column=0,sticky='nsew')
            


            frame_three = ttk.Frame(viewChack)
            frame_three.grid(row=0,column=2,padx=10,pady=10) 
            textStpo_chakbox = ttk.Label(frame_three, text='اعادة طباعة الكوشن')
            textStpo_chakbox.grid(row=0,column=1,sticky='nsew')
            backcomin_chackbox=ttk.Checkbutton(frame_three,variable=backcomin)
            backcomin_chackbox.grid(row=0,column=0,sticky='nsew')



            frame_foure = ttk.Frame(viewChack)
            frame_foure.grid(row=1,column=0,padx=10,pady=10) 
            edit_leble = ttk.Label(frame_foure, text='تعديل الكوشن')
            edit_leble.grid(row=0,column=1,sticky='nsew')
            edite_coshin=ttk.Checkbutton(frame_foure,variable=editecoshin)
            edite_coshin.grid(row=0,column=0,sticky='nsew')



            frame_five = ttk.Frame(viewChack)
            frame_five.grid(row=1,column=1,padx=10,pady=10) 
            textPrint= ttk.Label(frame_five,text="مندوب فرزة")
            textPrint.grid(row=0,column=1,sticky='nsew')
            Printstatment_chackbox= ttk.Checkbutton(frame_five,variable=printstatmeent)
            Printstatment_chackbox.grid(row=0,column=0,sticky='nsew')
            # Printstatment_chackbox.bind('<FocusIn>', lambda e='مندوب فرزة':self.showSort(e))
            




            frame_sixe = ttk.Frame(viewChack)
            frame_sixe.grid(row=1,column=2,padx=10,pady=10) 
            text_office= ttk.Label(frame_sixe,text="مندوب رسائل")
            text_office.grid(row=0,column=1,sticky='nsew')
            deposits_chackbox= ttk.Checkbutton(frame_sixe,variable=representative_message)
            deposits_chackbox.grid(row=0,column=0,sticky='nsew')
            # deposits_chackbox.bind('<FocusIn>', lambda e='مندوب فرزة':self.showSort(e))
        

            pachSpent = ttk.Frame(widgets_frame,width=40)
            pachSpent.grid(row=2,column=0,pady=15,padx=5)
            Spnlabltext = ttk.Label(pachSpent,text="كلمة المرور")
            Spnlabltext.grid(row=0,column=0)
            spent_entry= ttk.Entry(pachSpent,width=25)
            spent_entry.grid(row=0, column=1,padx=5, pady=5, sticky="ew")
            spent_entry.insert(0,'ادخل كلمة مرور')
            spent_entry.bind("<FocusIn>",lambda e: spent_entry.delete(0,'end'))
            
            kindspent_entry =ttk.Button(widgets_frame,text="ادخال",command=lambda: self.founInsert(controller),width=40)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=5, sticky="ew")
            

    # def showSort(self,e):
    #         viewsort.grid(row=1,column=1,padx=20,pady=20)

    def deletchack(self,e):
        for items in checkarrys:
            if items['name'] != e:
                items['value'].set(value=False)
    def founInsert(self,controller):
            # print('hello')
            swatcharray = []
            for sorsub in checkarrys:
                swatcharray.append({"name":sorsub['name'],'value':sorsub['value'].get()})
            self.datauser = get_loginAll()   
            usernamre =name_pach.get()
            passwor= spent_entry.get()
            newimportres= "true"
            newAddcridesres = "true"
            backcominres =  "true"
            printstatmentres = "true"
            representative = "true"
            editcoshin = "true"
            respnbilt ="المسؤل المباشر"
            # jsonSorting = None
            if len(usernamre) > 0 and usernamre != 'ادخل اسم المستخدم' and len(passwor) > 0 and passwor != 'ادخل كلمة مرور' :
                if self.datauser is not None and len(self.datauser) > 0:
                    # print(self.datauser)
                    # print(newimport.get())              
                    # print(userDatat,'hllllllo')
                    newimportres= "true" if  newimport.get() == True else 'false'
                    newAddcridesres = "true"  if newAddcrides.get() == True else 'false'
                    backcominres = "true" if  backcomin.get() == True else 'false'
                    printstatmentres = "true" if  printstatmeent.get() == True else 'false'
                    representative = "true" if  representative_message.get() == True else 'false'
                    editcoshin = "true" if  editecoshin.get() == True else 'false'
                    # jsonSorting = None if printstatmentres != 'true' and representative  != 'true' else swatcharray
                    respnbilt ="مندوب"
                jsonRespons = {"البحث والاستعلام":newimportres,"طباعة تقرير يومي":newAddcridesres,'اعادة طباعة الكوشن':backcominres,
                            "تعديل الكوشن":editcoshin,
                            "مندوب فرزة":printstatmentres,
                            "مندوب رسائل":representative,
                            # "نوع الفرزة":jsonSorting
                            }
                set_item(usernamre,passwor,respnbilt,json_stringify(jsonRespons))
                if  respnbilt.replace(" ","") == 'المسؤل المباشر'.replace(" ","") and  len(self.datauser) <= 1:
                    set_itemActivite({"userName":usernamre,"passwordUSER":passwor,"Responsibilities": respnbilt,"jsonResponsibilities":json_stringify(jsonRespons)})
                    set_itemx(usernamre,'بداية تشغيل')
                    controller.Show_frame(controller.page5,{"Start"})
                messagebox.showinfo(title="تم",message="تم انشاء حساب  بنجاح ")
                # controller.Show_frame(controller.page1,{"name1" : 'OIL',"name2":'new'})
                name_pach.delete(0,'end')
                name_pach.insert(0,'ادخل اسم المستخدم')
                spent_entry.delete(0,'end')
                spent_entry.insert(0,'ادخل كلمة مرور')
                newimport_chackbox.state(["!selected"])
                newAddcrides_chackbox.state(["!selected"])
                backcomin_chackbox.state(["!selected"])
                Printstatment_chackbox.state(["!selected"])  
            else:
                messagebox.showwarning(title="Error",message="يرجى اكمال البيانات ")
            