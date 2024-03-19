from tkinter import *
from tkinter import ttk
from convertcod.internal_Loginstorge import *
from convertcod.json_stringify import json_stringify
from convertcod.json_parse import json_parse
from sqiltyFoun import StationMonthSqly

class RegisterEdite(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global checkarrys
        global sorting
        sorting =  StationMonthSqly.inComin_dataAll()

        checkarrys = []
        self.newPage()
        self.loading()
    def founInsert(self):
            usernamre =name_pach.get()
            passwor= spent_entry.get()
            swatcharray = []
            for pic in checkarrys:
                swatcharray.append({"name":pic['name'],'value': pic["value"].get()})
            print(swatcharray)
            if len(usernamre) > 0 and usernamre != 'ادخل اسم المستخدم' and len(passwor) > 0 and passwor != 'ادخل كلمة مرور' :
                newimportres= "true" if  newimport.get() == True else 'false'
                newAddcridesres = "true"  if newAddcrides.get() == True else 'false'
                backcominres = "true" if  backcomin.get() == True else 'false'
                printstatmentres = "true" if  printstatmeent.get() == True else 'false'
                representative = "true" if  representative_message.get() == True else 'false'
                editcoshin = "true" if  editecoshin.get() == True else 'false'
                if responsibilities.replace(" ","") != 'المسؤل المباشر'.replace(" ",""):
                    jsonSorting = None if printstatmentres != 'true' and representative  != 'true' else swatcharray
                else:
                    jsonSorting = None 
                jsonRespons = {"البحث والاستعلام":newimportres,"طباعة تقرير يومي":newAddcridesres,'اعادة طباعة الكوشن':backcominres,
                        "تعديل الكوشن":editcoshin,
                        "مندوب فرزة":printstatmentres,
                        "مندوب رسائل":representative,
                        "نوع الفرزة":jsonSorting
                        }               
                # print(jsonRespons)
                Updat_item(ID,usernamre,passwor,json_stringify(jsonRespons))
                name_pach.delete(0,'end')
                name_pach.insert(0,'ادخل اسم المستخدم')
                spent_entry.delete(0,'end')
                spent_entry.insert(0,'ادخل كلمة مرور')
                newimport_chackbox.state(["!selected"])
                newAddcrides_chackbox.state(["!selected"])
                edite_coshin.state(["!selected"])
                Printstatment_chackbox.state(["!selected"])
                for pic in viewsort.winfo_children():
                    pic.destroy()
            
                self.loading()              
            else:
                messagebox.showwarning(title="Error",message="يرجى اكمال البيانات ")
            
    def loading(self):
        global datauser
        gettree = treeview.get_children()
        for item in gettree:
            treeview.delete(item)
        treeview.update()
        datauser= get_loginAll()
        # print(datauser)
        lisHeading = list({'تاريخ انشاء الحساب',"نوع الحساب",'اسم المستخدم'})
        if len(datauser) > 0 :
            for colsname in  lisHeading:
                treeview.heading(colsname,text=colsname)
            for values in datauser:
                valu = list(values)
                # valu.reverse()
                item = (valu[5],valu[3],valu[1])
                # print(item)
                treeview.insert('',END,values=item)
                treeview.configure(selectmode='extended')

    def on_selectuser(self,event):
            global ID
            global responsibilities
            selcted = treeview.selection()[0]
            table = treeview.item(selcted)["values"]

            # print(table[0])
            if datauser is not None and len(datauser) > 0 :
                for item in datauser:
                    if table[2] == item[1]:
                        ID = item[0]
                        responsibilities = item[3]
                        name_pach.delete(0,'end')
                        name_pach.insert(0,item[1])
                        spent_entry.delete(0,'end')
                        spent_entry.insert(0,item[2])
                        if item[4] is not None and len(item[4]) > 0 :
                            dataRespons = json_parse(item[4])
                            # print(dataRespons)
                            if dataRespons["البحث والاستعلام"] == 'true':
                                newimport.set(value=True)
                                newimport_chackbox.state(["selected"])
                            else:
                                newimport.set(value=False)
                                newimport_chackbox.state(["!selected"])
                            if dataRespons["طباعة تقرير يومي"] == 'true':
                                    newAddcrides.set(value=True)
                                    newAddcrides_chackbox.state(["selected"])
                            else:
                                newAddcrides.set(value=False)
                                newAddcrides_chackbox.state(["!selected"])
                            if dataRespons['اعادة طباعة الكوشن'] == 'true':
                                    backcomin.set(value=True)
                                    backcomin_chackbox.state(["selected"])
                            else:
                                backcomin.set(value=False)
                                backcomin_chackbox.state(["!selected"])
                            if dataRespons["تعديل الكوشن"] == 'true':
                                    editecoshin.set(value=True)
                                    edite_coshin.state(["selected"])
                            else:
                                editecoshin.set(value=False)
                                edite_coshin.state(["!selected"])
                            if dataRespons["مندوب فرزة"] == 'true':
                                printstatmeent.set(value=True)
                                Printstatment_chackbox.state(["selected"])
                            else:
                                printstatmeent.set(value=False)
                                Printstatment_chackbox.state(["!selected"])                                           
                            if dataRespons["مندوب رسائل"] == 'true':
                                representative_message.set(value=True)
                                deposits_chackbox.state(["selected"])
                            #     viewsort.grid(row=1,column=1,padx=20,pady=20)
                            # if dataRespons["مندوب فرزة"] is not None:
                            #     self.deletchack(other=dataRespons['نوع الفرزة'])
                            else:
                                representative_message.set(value=False)
                                deposits_chackbox.state(["!selected"])    




    def deletchack(self,e=None,other=None):
        if e is not None:
            for items in checkarrys:
                if items['name'] != e:
                    items['value'].set(value=False)
        if other is not None:
            selected = next((item for item in other if item['value'] == True),None)
            for items in checkarrys:
                if items['name'] == selected['name']:
                    items['value'].set(value=True)
                else:
                    items['value'].set(value=True)



    def newPage(self):
            global name_pach
            global spent_entry
            global newimport
            global newAddcrides
            global stopCrides
            global printstatmeent
            global newimport_chackbox
            global newAddcrides_chackbox
            global Printstatment_chackbox
            global treeview
            global representative_message
            global backcomin_chackbox
            global backcomin
            global edite_coshin
            global editecoshin
            global deposits_chackbox
            # global viewsort
            index= 0
            newimport = BooleanVar()
            newAddcrides= BooleanVar()
            stopCrides = BooleanVar()
            EditCrides= BooleanVar()
            representative_message= BooleanVar()

            printstatmeent = BooleanVar()
            editecoshin = BooleanVar()
            backcomin = BooleanVar()

        

            frame = ttk.Frame(self,padding=15)
            frame.pack(anchor='center',padx=20,pady=60,fill='both')
        
            widgets_frame = ttk.LabelFrame(frame, text="تسجيل مستخدم",padding=10)
            widgets_frame.grid(row=0,column=1,padx=20,pady=5,sticky='nesw')
            # widgets_frame.place(y=250,x=600)
    
            pachNew = ttk.Frame(widgets_frame)
            pachNew.grid(row=0,column=0,pady=15,padx=5)
            text_kind = ttk.Label(pachNew,text="...اسم المستخدم" )
            text_kind.grid(row=0,column=1,padx=15,pady=15)
    
            name_pach = ttk.Entry(pachNew,width=20)
            name_pach.grid(row=0, column=0,padx=5, pady=5)
            name_pach.insert(0,'ادخل اسم المستخدم')
            name_pach.bind("<FocusIn>", lambda e:name_pach.delete(0,'end'))




            # viewsort= ttk.LabelFrame(widgets_frame,padding=10)
            # # viewsort.grid_forget()
            # viewsort.grid(row=1,column=1,padx=20,pady=20)
        
            # scrollbar = ttk.Scrollbar(viewsort, orient='vertical')
            # scrollbar.pack(side='right', fill='y')
            # # scrollbarhst = ttk.Scrollbar(viewsort,orient='horizontal')
            # # scrollbarhst.pack(side='bottom', fill='x')
            
            # canva = Canvas(viewsort ,width=200,height=150,yscrollcommand=scrollbar.set)
            # canva.pack(expand=True)

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
            viewChack.grid(row=1,column=0,padx=10,pady=20)
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
            frame_three.grid(row=1,column=0,padx=2,pady=2) 
            textStpo_chakbox = ttk.Label(frame_three, text='اعادة طباعة الكوشن')
            textStpo_chakbox.grid(row=0,column=1,sticky='nsew')
            backcomin_chackbox=ttk.Checkbutton(frame_three,variable=backcomin)
            backcomin_chackbox.grid(row=0,column=0,sticky='nsew')



            frame_foure = ttk.Frame(viewChack)
            frame_foure.grid(row=1,column=1,padx=10,pady=10) 
            edit_leble = ttk.Label(frame_foure, text='تعديل الكوشن')
            edit_leble.grid(row=0,column=1,sticky='nsew')
            edite_coshin=ttk.Checkbutton(frame_foure,variable=editecoshin)
            edite_coshin.grid(row=0,column=0,sticky='nsew')



            frame_five = ttk.Frame(viewChack)
            frame_five.grid(row=2,column=0,padx=10,pady=10) 
            textPrint= ttk.Label(frame_five,text="مندوب فرزة")
            textPrint.grid(row=0,column=1,sticky='nsew')
            Printstatment_chackbox= ttk.Checkbutton(frame_five,variable=printstatmeent)
            Printstatment_chackbox.grid(row=0,column=0,sticky='nsew')
            # Printstatment_chackbox.bind('<FocusIn>', lambda e='مندوب فرزة':self.showSort(e))
            




            frame_sixe = ttk.Frame(viewChack)
            frame_sixe.grid(row=2,column=1,padx=10,pady=10) 
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
            
    
            
            
            kindspent_entry =ttk.Button(widgets_frame,text="ادخال",command=self.founInsert,width=20)
            kindspent_entry.grid(row=4, column=0,padx=5, pady=5, sticky="ew")
            
            FarmTree = ttk.Frame(frame,
                                width=800,
                                height=500
                                )
            FarmTree.grid(row=0,column=0,padx=20,pady=5,sticky='nesw')
            FarmTree.pack_propagate(0)
            treeScroll= ttk.Scrollbar(FarmTree)
            treeScroll.pack(side='right',fill='y')
            treeScroll_x= ttk.Scrollbar(FarmTree,orient='horizontal')
            treeScroll_x.pack(side='bottom',fill='x')
            cols=('تاريخ انشاء الحساب',"نوع الحساب",'اسم المستخدم')
            
            treeview = ttk.Treeview(FarmTree,show='headings', yscrollcommand=treeScroll.set,xscrollcommand=treeScroll_x.set,columns=cols,height=500)
            treeview.pack(side='right',anchor='center')
            treeview.column('اسم المستخدم',width=350,anchor='center')
            treeview.column('نوع الحساب',width=300,anchor='center')
            treeview.column('تاريخ انشاء الحساب', width=300,anchor='center')
            treeScroll.config(command=treeview.yview)
            treeScroll_x.config(command=treeview.xview)
            treeview.xview_moveto(100)
            treeview.bind('<<TreeviewSelect>>',self.on_selectuser)
