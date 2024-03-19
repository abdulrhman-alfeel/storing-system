from tkinter import ttk,filedialog
import tkinter as tk
from tkinter import messagebox
from convertcod.internal_storage import *
from datetime import datetime, timedelta

# import threading
from sqiltyFoun import StationMonthSqly
from convertcod.userfind import *
# from Print.viewpdf import switchMonth
from convertcod.json_parse import randomnumber
from convertcod.TOPlevel import Moudel
from convertcod.view_image import veiw_image ,convert_image_buffer
from convertcod.camera import cameraCop
from convertcod.TOPlevel import select_custom
import io
import json
# import gc
Cash= ''
chaking = False
class MyClassOffice(ttk.Frame):
    # def __init__(self,pags_labl,aciton,nuber,textnuber,textnubermonth):
    def __init__(self, parent,controller):
            ttk.Frame.__init__(self,parent)
            global ID_numberCart_entry
            global office_name_entry
            global owner_name_entry
            global Guarantee_entry
            global treeview
            global buttonInsert
            global frameAmont
            global dates
            global user_text
            global userConternr
            global widgets_frame
            global treeFrame
            global contro
            global FerquntlyeDeay
            global IDsort_entry
            global data_employ
            global url_image_license
            global ButtonOn_licenses
            global widgets_button
            global url_image_licenses_url

            self.number = 4
            contro = controller
            # global user_Time
            self.Faroms ={}
            self.dataEdit = {}
            self.id_kind = 0
            self.brcod = False
            dates= []
            data_employ = []
            url_image_license = {}
            url_image_licenses_url = {}
            
            self.DataSOrt = []
            Datasort  = StationMonthSqly.inComin_dataAllwitch()
            start_date = datetime.now()
            end_date = datetime(2028, 9, 30)
            
            FerquntlyeDeay = StationMonthSqly.inComin_dataAll() 
            for day in range((end_date - start_date).days + 1):
                datall = start_date + timedelta(days=day)
                dates.append(datall.date())

            for r in Datasort:
                    # print(r[1])
                    self.DataSOrt.append(r[1])
                    # padding=(5,5),
            widgets_frame = ttk.LabelFrame(self, height=700)
            widgets_frame.grid(row=1, column=1, padx=10, pady=2)
            # sticky="nsew"
            widgets_frame.pack_propagate(0)
            # widgets_frame.pack(side='right',anchor='e')
            
            
            frameAmont = ttk.LabelFrame(widgets_frame)
            frameAmont.grid(column=0,row=0,padx=5,pady=2,sticky='ew')
            frameAmont.anchor('center')
            userConternr = ttk.LabelFrame(frameAmont,text='اسم المستخدم')
            user_text = ttk.Label(userConternr)
            user_text.grid(column=0,row=0,padx=5,pady=2) 
            office_name_entry = ttk.Entry(widgets_frame,justify='right')
            office_name_entry.insert(0,'اسم المكتب')
            office_name_entry.bind("<FocusIn>", lambda e: office_name_entry.delete('0', "end") )
            office_name_entry.grid(row=2, column=0,padx=5, pady=10, sticky="ew")

            
            SortNew = ttk.LabelFrame(widgets_frame,text="اسم الفرزة")
            SortNew.grid(row=3,column=0,padx=5)
            IDsort_entry = ttk.Combobox(SortNew,values=self.DataSOrt)
            # IDsort_entry.current(0)
            IDsort_entry.grid(row=0, column=0,padx=5, pady=10, sticky="ew")
            

            
            owner_name_entry= ttk.Entry(SortNew,justify='right')
            owner_name_entry.grid(row=0, column=1, pady=10, sticky="ew")
            owner_name_entry.insert(0,'اسم المالك')
            owner_name_entry.bind("<FocusIn>",lambda e:owner_name_entry.delete(0,'end'))
                        
            


            FrameStart = ttk.Frame(widgets_frame)
            FrameStart.grid(row=4,column=0,padx=5)
            pachNew = ttk.LabelFrame(FrameStart,text="البطاقة الشخصية")
            pachNew.grid(row=0,column=0,padx=5,pady=10)
            ID_numberCart_entry = ttk.Entry(pachNew,justify='right')
            ID_numberCart_entry.grid(row=0, column=0, pady=10, 
            # sticky="ew"
            )
            ID_numberCart_entry.insert(0,'رقم البطاقة')
            ID_numberCart_entry.bind("<FocusIn>",lambda e: ID_numberCart_entry.delete(0,"end"))


            
            thelabltext = ttk.LabelFrame(FrameStart,text="الترخيص")
            thelabltext.grid(row=0,column=1,pady=15,padx=5)
            Guarantee_entry= ttk.Entry(thelabltext,justify='right')
            Guarantee_entry.insert(0,"رقم الرخصة")
            Guarantee_entry.grid(row=0, column=0,padx=5, pady=5, 
            # sticky="ew"
            )
            Guarantee_entry.bind("<FocusIn>", lambda e: Guarantee_entry.delete(0,"end"))
            
        

            widgets_button = ttk.Frame(widgets_frame)
            widgets_button.grid(row=5,column=0,padx=10,pady=10)

            ButtonOn = ttk.Button(widgets_button,text='اضافة موظفين', underline=0 ,command=lambda:self.Add_data_employ())
            ButtonOn.grid(row=0,column=0,pady=15,padx=5)
            
            ButtonOn_licenses = ttk.Button(widgets_button,text='صورة الرخصة', underline=0 ,command=lambda:self.select_image_licenses_office())
            ButtonOn_licenses.grid(row=0,column=1,pady=15,padx=5)
            # ButtonOn.place(y=50)
            
        
            treeFrameButon = ttk.Frame(widgets_frame,width=20)
            treeFrameButon.grid(row=9,column=0, padx=10, pady=(10, 5))
            # , sticky="nsew"
            buttonT = ttk.Button(treeFrameButon,text="تهيئة",
                                command=self.databis,width=14)
            buttonT.grid(row=0, column=1,padx=5, pady=5, 
            # sticky="ew"
            )
            buttonInsert = ttk.Button(treeFrameButon,text="حفظ", 
                                        command=self.insert_row,width=14)
            buttonInsert.grid(row=0, column=0,padx=5, pady=5, 
            # sticky="ew"
            )
        


            treeFrame = ttk.Frame(self,width=1000,height=700)
            treeFrame.grid(row=1,column=0, pady=5,padx=10)
            treeFrame.pack_propagate(0)
            fromButtom = ttk.Frame(treeFrame)
            fromButtom.pack(side='bottom',anchor="n")
        




            #     separator = ttk.Separator(widgets_frame,orient="vertical")
            # separator.grid(row=8, column=0, padx=(10,5), pady=5, sticky="ew")
            treeScroll = ttk.Scrollbar(treeFrame,orient='vertical')
            treeScroll.pack(side="right", fill="y")
            
            treeScrollButtom = ttk.Scrollbar(treeFrame,orient='horizontal')
            treeScrollButtom.pack(side='bottom', fill="x")
            cols= ('التاريخ',"الترخيص", "اسم الفرزة","البطاقة الشخصية","اسم المالك",
                   "اسم المكتب",'معرف المكتب',"م")
            # cols= ("الترخيص","رقم السيارة", "لون السيارة اليوم","نوع السيارة","رقم البطاقة","اسم السائق",'رقم معرف السائق',"م")
            treeview = ttk.Treeview(treeFrame, show="headings",
                                    yscrollcommand=treeScroll.set,xscrollcommand=treeScrollButtom.set, columns=cols, height=700)
            treeview.column("م",anchor="center",)
            treeview.column("معرف المكتب",anchor="center")
            treeview.column("اسم المكتب",anchor="center",)
            treeview.column("اسم الفرزة",anchor="center")
            treeview.column("اسم المالك",anchor="center")
            treeview.column("البطاقة الشخصية",anchor="center")
            treeview.column("الترخيص",anchor="center")
            treeview.column("التاريخ",anchor="center")
            treeview.tag_bind("row",'<Button-3>', lambda event: self.on_tree_view_select(event))
            # treeview.column("Employment",width=100,anchor="center")
            treeview.pack(side="right",pady=5)
            treeScroll.config(command=treeview.yview)
            treeScrollButtom.config(command=treeview.xview)
            treeview.xview_moveto(100)
            self.keyPrssnum = 0 



    def select_image_licenses_office(self):
        global url_image_license
        global url_image_licenses_url
        def select(kind):
            global url_image_license
            global url_image_licenses_url
            if kind == 'files':
                url_image_licenses_url = filedialog.askopenfilename(initialdir=os.getcwd,title='select image licenses',
                                                            filetypes=(('jpg file','.jpg'),
                                                                        ('JPG FILE','.JPG'),
                                                                        ('PNG FILE','.PNG'),
                                                                        ('png file','.png'),
                                                                        ('All file','text')))
            else:
                url_image_licenses_url = cameraCop()

            try:
                url_bse64= veiw_image(url_image_licenses_url)
                url_image_license = url_bse64
                ButtonOn_licenses.configure(image=url_image_license)
                ButtonOn_licenses.update_idletasks()
                min.destroy()
            except:
                pass
        min= select_custom(self,'المكتب',select,contro.list_file,contro.camera) 
        
    
    
    # add employ office
    def Add_data_employ(self):
        global data_employ
        global number
        trovel = Moudel(self,'اضافة موظفين')
        Buttomn = {}
        Buttomn_ID_number = {}
        image_button = {}
        image_button_ID_number = {}
        number = 4

        def Add_entry():
            global number
            number += 1
            frams = ttk.LabelFrame(frame_trovel)
            frams.grid(row=number,column=0)
            arrays = repetition_row(frams)
            Buttomn[number] = ttk.Button(frams,text='صورة الموظف',command=lambda  index=number:select_image(Buttomn[index],index,'perosnality'))
            Buttomn[number].grid(row=1,column=2,pady=15)
            Buttomn_ID_number[number] = ttk.Button(frams,text='صورة البطاقة الشخصية',command=lambda  index=number:select_image(Buttomn_ID_number[index],index,"ID_number"))
            Buttomn_ID_number[number].grid(row=1,column=3,pady=15)
            data_employ.append({"entry":arrays,"function_employ":Buttomn[number],'function_ID_number':Buttomn_ID_number[number],"url_image_employ":None,"url_image_IDnumber":None,'ID':number})
            
            canves.configure(scrollregion=canves.bbox('all'))
            canves.update()




        buttom_Add = ttk.Button(trovel,command=Add_entry,text='جديد')
        buttom_Add.pack(side='top',fill='both')



        scrollbar_x = tk.Scrollbar(trovel,orient='horizontal')
        scrollbar_x.pack(side='bottom',fill='x')

        scrollbar_y = tk.Scrollbar(trovel,orient='vertical')
        scrollbar_y.pack(side='right',fill='y')

        canves = tk.Canvas(trovel,width=1300,height=600,yscrollcommand=scrollbar_y.set,xscrollcommand=scrollbar_x.set)
        canves.pack(fill='both',expand=True,padx=15,pady=15)

        canves.bind('<Configure>',lambda e:canves.configure(scrollregion=canves.bbox('all')))
        scrollbar_x.config(command=canves.xview)
        scrollbar_y.config(command=canves.yview)

        frame_trovel = ttk.Frame(canves)
        # frame_trovel.pack(fill='both',expand=True,padx=10,pady=10)
        canves.create_window((0,0),window=frame_trovel,anchor='nw')

        for index in [0,1,2,3,4,5,6]:
            frame_trovel.columnconfigure(index=index,weight=1)
            frame_trovel.rowconfigure(index=index,weight=1)
        


        # def shift_cursor2(event,frimeng): 
        #     # print(event)
            
        #     position = frimeng.index(INSERT) 
        
        #     # Changing position of cursor one character right 
        #     frimeng.icursor(position - 1) 




        
        def on_right_arrow(event):
             event.widget.tk_focusNext().focus()

        def on_left_arrow(event):
             event.widget.tk_focusPrev().focus()

    


        def repetition_row(frams,kinding= None):
            data = ['entry_name','entry_age','entry_number_ID',"entry_phone",'entry_address']
            a_data= ['اسم الموظف','العمر',"رقم البطاقة الشخصية",'رقم التلفون','العنوان']
            
            data.reverse()
            a_data.reverse()

            oo_entry = {}
        
            oo_array =[]
            key_index = 0
            for key in data:
                key_index +=1
                fram_Entry= ttk.LabelFrame(frams,text=a_data[key_index-1])
                fram_Entry.grid(row=0,column=key_index)
                oo_entry["".join(str(key))]= ttk.Entry(fram_Entry,justify='right',validate='focusin',exportselection=True)
                # oo_entry["".join(str(key))].bindtags(((str(oo_entry["".join(str(key))])), "TEntry", "KeyRelease", "\t", "all"))
                oo_entry["".join(str(key))].bind("<Right>",on_right_arrow)
                oo_entry["".join(str(key))].bind("<Left>",on_left_arrow)
           
                if kinding is not None :
                    kind = kinding
                    kind.reverse()
                    oo_entry["".join(str(key))].insert(0,kind[key_index-1])
                oo_entry["".join(str(key))].grid(row=0,column=0)
                # oo_array.append( oo_entry["".join(str(key))])
            
            return oo_entry



        def select_image(Buttomn_fream,id,kind_opr):
            def select(kind):
                global data_employ
                
                if kind == 'files':
                    file_name = filedialog.askopenfilename(initialdir=os.getcwd(),
                                                        filetypes=(("jpg file",'.jpg'),
                                                                ("JPG FILE" ,'.JPG'),
                                                                ("png file",'.png'),
                                                                ('PNG FILE', '.PNG'),
                                                                ('All file','.text')),title='select image file')
                else:
                    file_name= cameraCop()
                
                photo = veiw_image(file_name)
                if kind_opr == 'perosnality':
                    image_button[id]= photo
                else:
                    image_button_ID_number[id] = photo
                data_cameng = data_employ
                data_employ = []
                # Buttomn_fream.config(image=photo)

                for pic in data_cameng:
                    if pic['ID'] != id:
                            data_employ.append(pic)
                    else:
                            if kind_opr == 'perosnality':
                                data_employ.append({"entry":pic['entry'],"function_employ":Buttomn_fream.config(image=image_button[id]),
                                                    'function_ID_number':pic['function_ID_number'],
                                                    "url_image_employ":file_name,"url_image_IDnumber":pic['url_image_IDnumber'],'ID':pic['ID']})
                            else:
                                data_employ.append({"entry":pic['entry'],"function_employ":pic['function_employ'],
                                                    "function_ID_number":Buttomn_fream.config(image=image_button_ID_number[id])
                                                    ,"url_image_employ":pic['url_image_employ'],"url_image_IDnumber":file_name,'ID':pic['ID']})
                            
                # pic['function_employ'].update()
                # Buttomn_fream.update_idletasks()
                        
                Buttomn_fream.update()
                canves.configure(scrollregion=canves.bbox('all'))
                canves.update_idletasks()
                min.destroy()
            min= select_custom(self,'المكتب',select,contro.list_file,contro.camera) 
        

        def exit_entry():
            global data_employ
            main = []
            totle= []
            try:
                for pcc in data_employ:
                    # print(pcc['entry'].values(),'vallllllllllllure')
                    for pif in  pcc['entry'].values():
                        print(pif.get())
                        if len(pif.get()) > 0 :
                            main.append(pif.get())
                    if len(main) > 0:
                        totle.append({"entry":main , "ID":pcc['ID'],'function_employ':pcc['function_employ'],'function_ID_number':pcc['function_ID_number'],
                                    "url_image_employ":pcc['url_image_employ'],"url_image_IDnumber":pcc['url_image_IDnumber']})
                    main= []
                data_employ = totle    
            except:
                 pass
            # print(totle,'totle')
            trovel.destroy()
            # print(data_employ,'data_employ')

        if len(data_employ) <= 0 :       
            for item in range(number):
                frams = ttk.LabelFrame(frame_trovel)
                frams.grid(row=item+1,column=0)
                arrays =repetition_row(frams)
                Buttomn[item+1] = ttk.Button(frams,text='صورة الموظف',command=lambda  index=item+1:select_image(Buttomn[index],index,'perosnality'))
                Buttomn[item+1].grid(row=1,column=2,pady=15)
                Buttomn_ID_number[item+1] = ttk.Button(frams,text='صورة البطاقة الشخصية',
                                                       command=lambda  index=item+1:select_image(Buttomn_ID_number[index],index,"ID_number"))
                Buttomn_ID_number[item+1].grid(row=1,column=3,pady=15)
                data_employ.append({"entry":arrays,"function_employ":Buttomn[item+1],
                                    'function_ID_number':Buttomn_ID_number[item+1],"url_image_employ":None,"url_image_IDnumber":None,'ID':item+1})
        else:
            data_comin = data_employ
            comin = []
            pin = []
            photo_buttom= {}
            photo_ID = {}
            for pic in data_comin:
                frams = ttk.LabelFrame(frame_trovel,width=500)
                frams.grid(row=int(pic['ID']),column=0)
                arrays = repetition_row(frams,pic['entry'])
                if pic['url_image_employ'] is not None: 
                    # print(pic['url_image_employ'])encode('utf-8')
                   
                    photo_buttom[int(pic["ID"])] = veiw_image(pic['url_image_employ'])
                    Buttomn[int(pic['ID'])] = tk.Button(frams,image=photo_buttom[int(pic["ID"])]
                                                         ,command=lambda  index=int(pic['ID']):select_image(Buttomn[index],index,'perosnality'),width=200)
                else:
                    Buttomn[int(pic['ID'])] = ttk.Button(frams,text='صورة الموظف'
                                                         ,command=lambda  index=int(pic['ID']):select_image(Buttomn[index],index,'perosnality'))
                
                Buttomn[int(pic['ID'])].grid(row=1,column=2,pady=15)
                if pic['url_image_IDnumber'] is not None :
                    
                    photo_ID[int(pic['ID'])] = veiw_image(pic['url_image_IDnumber'])
                    Buttomn_ID_number[int(pic['ID'])] = tk.Button(frams,image=photo_ID[int(pic['ID'])]
                                                                   ,command=lambda  index=int(pic['ID']):select_image(Buttomn_ID_number[index],index,"ID_number"),width=1000)
                else:    
                    Buttomn_ID_number[int(pic['ID'])] = ttk.Button(frams,text='صورة البطاقة الشخصية',
                                                                   command=lambda  index=int(pic['ID']):select_image(Buttomn_ID_number[index],index,"ID_number"))
                Buttomn_ID_number[int(pic['ID'])].grid(row=1,column=3,pady=15)
                comin.append({"entry":arrays,"function_employ":Buttomn[int(pic['ID'])],
                              'function_ID_number':Buttomn_ID_number[int(pic['ID'])],"url_image_employ":pic['url_image_employ'],
                              "url_image_IDnumber":pic['url_image_IDnumber'],'ID':int(pic['ID'])})
            data_employ =  comin

        buttom_save = ttk.Button(trovel,command=exit_entry,text='حفظ')
        buttom_save.pack(side='top',fill='both')





    def prossecc(self):
        self.insert_row()
        
    def SwitchData(self,saw,Page):
        Man = tk.Menu(Page,tearoff=0)
        Man.add_command(label="اليومي",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='day'))
        Man.add_command(label="الشهري",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='month'))
        Man.post(Page.winfo_rootx(),Page.winfo_rooty())

    #  عملية  الصرف 
    def insert_row(self,kind_opration=None):
           
        name_office = office_name_entry.get()
        IDsort = IDsort_entry.get()
        Admin = owner_name_entry.get()
        ID_numbercart = ID_numberCart_entry.get()
        license_office =Guarantee_entry.get()

        empty_employ = []
        for item in data_employ:


            empty_employ.append({"entry":item['entry'],"url_image_employ":item['url_image_employ'],
                                   "url_image_IDnumber":item['url_image_IDnumber'],'ID':item['ID']})

        if len(empty_employ) > 0:
            # arrays_employe = json_stringify(empty_employ)
            arrays_employe = json.dumps(empty_employ,indent=4)
        else:
            arrays_employe = None
        if len(url_image_licenses_url) > 0:
            data_image = convert_image_buffer(url_image_licenses_url)
            if kind_opration is None:
                iDoffice = randomnumber()
                StationMonthSqly.insert_Office(iDoffice,name_office,Admin,
                                            ID_numbercart,arrays_employe,license_office,IDsort,data_image)
            else:
                iDoffice = kind_opration
                StationMonthSqly.insert_Office(iDoffice,name_office,Admin,
                                            ID_numbercart,arrays_employe,license_office,IDsort,data_image,'update')             
            self.empytePage()
            self.load_data()
        else:
             messagebox.showwarning(title='خطا',message='يجب اضفاة ترخيص المكتب')


    #عمليات التعديل

    def on_tree_view_select(self,event): 
            try:
                data = StationMonthSqly.inCominOffice_Pablic()
                id_row = treeview.identify_row(event.y)
                treeview.selection_set(id_row)          
                row_value = treeview.item(id_row)["values"] 
                # print(row_value)
                selectClick = tk.Menu(treeview,tearoff=0)
                print( row_value)
                dataMath = next((ite for ite in data if int(ite['iDoffice']) == int(row_value[6])),None)
                if dataMath is not None:
                    # print(driveData,row_value[8])
                    selectClick.add_command(label='تعديل',command=lambda:self.empyteُEdit(dataMath))
                    self.empytePage() 
                    buttonInsert.config(text="تعديل", command=lambda:self.insert_row(kind_opration=dataMath['iDoffice']))
                # else:
                #     print('error',row_value[2])
                #     print('error',FerquntlyeDeay)
                selectClick.post(event.x_root,event.y_root)
            except:
                print('خطاء تحديد')

    #  عمليات التعديل
    def empyteُEdit(self,row):
                global data_employ
                global url_image_licenses_url
                global url_image_license
                # data_office = StationMonthSqly.inCominOffice_Pablic()
                owner_name_entry.delete(0,"end")
                ID_numberCart_entry.delete(0,"end")
                office_name_entry.delete(0,"end")
                IDsort_entry.set(row['IDsort'])
                ID_numberCart_entry.insert(0,row['ID_numberCart'])
                office_name_entry.insert(0,row['office_name'])
                Guarantee_entry.delete(0,"end")
                Guarantee_entry.insert(0,row['Licensig'])
                owner_name_entry.insert(0,row['owner_name'])
                if len(row['employ_name']) > 0 and row['employ_name'] != 'None':
                    data_employ = json_parse(row['employ_name'])
                url_image_licenses_url = io.BytesIO(row['url_image_licens'])
                imageing = veiw_image(url_image_licenses_url)
                url_image_license = imageing
                ButtonOn_licenses.config(image= url_image_license)
                ButtonOn_licenses.update_idletasks()
                userConternr.grid_forget()


    #  عمليات التحديث
    def empytePage(self):
                global data_employ 
                global ButtonOn_licenses
                owner_name_entry.delete(0,"end")
                ID_numberCart_entry.delete(0,"end")
                office_name_entry.delete(0,"end")
                ID_numberCart_entry.insert(0,'رقم البطاقة')
                office_name_entry.insert(0,'اسم المكتب')
                Guarantee_entry.delete(0,"end")
                Guarantee_entry.insert(0,"رقم الرخصة")
                owner_name_entry.insert(0,'اسم المالك')
                # ButtonOn_licenses.destroy()
                for items in widgets_button.winfo_children():
                     items.destroy()
                ButtonOn = ttk.Button(widgets_button,text='اضافة موظفين', underline=0 ,command=lambda:self.Add_data_employ())
                ButtonOn.grid(row=0,column=0,pady=15,padx=5)
                ButtonOn_licenses = ttk.Button(widgets_button,text='صورة الرخصة', underline=0 ,command=lambda:self.select_image_licenses_office())
                ButtonOn_licenses.grid(row=0,column=1,pady=15,padx=5)
                ButtonOn_licenses.update()
                widgets_button.update()
                data_employ = []
                userConternr.grid_forget()
                # gc.collect()

    def databis(self):  
                global chaking
                chaking = False
                self.brcod=False
                buttonInsert.config(text="اضافة",
                                    command=self.prossecc)
                self.empytePage()                  

                
    def load_data(self):
                # global new
                global arrayPash
               
                index = 0
                # station =  StationMonthSqly.inComin_dataAll()
              
                
                arrayPash= []
                
                items= treeview.get_children()
                
                for item in items:
                     treeview.delete(item)
                treeview.update()
                lisvalues = list({'التاريخ',"الترخيص", "اسم الفرزة","البطاقة الشخصية","اسم المالك",
                   "اسم المكتب",'معرف المكتب',"م"})
                
                for col_name in lisvalues:
                        treeview.heading(col_name, text=col_name)
                data_office = StationMonthSqly.inCominOffice_Pablic()
                for i in data_office:

                    index += 1
                    # sort = next((f for f in station if f['IDsort'] == i['IDsort'] ),None)
                    objectTree = (i["Time"],i['Licensig'],i['IDsort'],i['ID_numberCart'],i['owner_name'],i['office_name'],i['iDoffice'],index)
                    treeview.insert('', tk.END, values=objectTree,tags=("event",'row'))
                    treeview.configure(selectmode='extended') 
            
                gc.collect()




