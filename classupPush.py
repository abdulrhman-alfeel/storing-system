from tkinter import ttk, filedialog
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
from PIL import ImageTk,Image
from convertcod.view_image import convert_image_buffer
from convertcod.camera import cameraCop
from convertcod.TOPlevel import select_custom
import io
# import gc
Cash= ''
chaking = False
class MyClassPush(ttk.Frame):
    # def __init__(self,pags_labl,aciton,nuber,textnuber,textnubermonth):
    def __init__(self, parent,controller):
            ttk.Frame.__init__(self,parent)
            global ID_numberCart_entry
            global namedrive_entry
            global kind_care_entry
            global number_Care_entry
            global Guarantee_entry
            global Color_care
            global treeview
            global buttonInsert
            global frameAmont
            global dates
            global user_text
            global userConternr
            global namerecevid
            global widgets_frame
            global treeFrame
            global contro
            global FerquntlyeDeay
            global IDsort_entry
            global button_image_care
            global button_image_drive
            global button_image_thelabl
            global treeFrameButon
            global DataSOrt




            contro = controller
            # global user_Time
            self.dataEdit = {}
            self.id_kind = 0
            self.brcod = False
            dates= []
            DataSOrt = []
            self.Url_drive= {}



            start_date = datetime.now()
            end_date = datetime(2028, 9, 30)
            FerquntlyeDeay = StationMonthSqly.inComin_dataAll() 
            for day in range((end_date - start_date).days + 1):
                datall = start_date + timedelta(days=day)
                dates.append(datall.date())
        
            widgets_frame = ttk.LabelFrame(self, padding=(5,5),height=700)
            widgets_frame.grid(row=1, column=1, padx=10, pady=2, sticky="nsew")
            widgets_frame.pack_propagate(0)
            # widgets_frame.pack(side='right',anchor='e')
            frameAmont = ttk.LabelFrame(widgets_frame)
            frameAmont.grid(column=0,row=0,padx=5,pady=2,sticky='ew')
            frameAmont.anchor('center')
            userConternr = ttk.LabelFrame(frameAmont,text='اسم المستخدم')
            user_text = ttk.Label(userConternr)
            user_text.grid(column=0,row=0,padx=5,pady=2) 
        
            namedrive_entry = ttk.Entry(widgets_frame,justify='right')
            namedrive_entry.insert(0,'اسم السائق')
            namedrive_entry.bind("<FocusIn>", lambda e: namedrive_entry.delete('0', "end") )
            namedrive_entry.grid(row=2, column=0,padx=5, pady=10, sticky="ew")
            
            FrameStart = ttk.Frame(widgets_frame)
            FrameStart.grid(row=3,column=0,padx=5)
            SortNew = ttk.LabelFrame(FrameStart,text="اسم الفرزة")
            SortNew.grid(row=0,column=1,padx=5)
            IDsort_entry = ttk.Combobox(SortNew)
            # IDsort_entry.current(0)
            IDsort_entry.grid(row=0, column=1,padx=5, pady=10, sticky="ew")

            pachNew = ttk.LabelFrame(FrameStart,text="البطاقة الشخصية")
            pachNew.grid(row=0,column=0,padx=5)
            ID_numberCart_entry = ttk.Entry(pachNew,justify='right')
            ID_numberCart_entry.grid(row=0, column=0, pady=10, sticky="ew")
            ID_numberCart_entry.insert(0,'رقم البطاقة')
            ID_numberCart_entry.bind("<FocusIn>",lambda e: ID_numberCart_entry.delete(0,"end"))
            
            namerecevid = ttk.LabelFrame(widgets_frame,text=" السيارة",width=10)
            namerecevid.grid(row=4,column=0,padx=5,pady=10)
            Color_care = ttk.Entry(namerecevid,justify='right')
            Color_care.grid(row=0, column=1,padx=5, pady=10, sticky="ew")
            Color_care.insert(0,'لون السيارة')
            Color_care.bind("<FocusIn>",lambda e:Color_care.delete(0,'end'))

            kind_care_entry= ttk.Entry(namerecevid,justify='right')
            kind_care_entry.grid(row=0, column=0, pady=10, sticky="ew")
            kind_care_entry.insert(0,'نوع السيارة')
            kind_care_entry.bind("<FocusIn>",lambda e:kind_care_entry.delete(0,'end'))
            
            Farmstatment = ttk.Frame(widgets_frame)
            Farmstatment.grid(row=5,column=0,pady=15,padx=5)

            thelabltext = ttk.LabelFrame(Farmstatment,text="الترخيص")
            thelabltext.grid(row=0,column=1,pady=10,padx=5)
            Guarantee_entry= ttk.Entry(thelabltext,justify='right')
            Guarantee_entry.insert(0,"رقم الرخصة")
            Guarantee_entry.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            Guarantee_entry.bind("<FocusIn>", lambda e: Guarantee_entry.delete(0,"end"))
            
            Spnlabltext = ttk.LabelFrame(Farmstatment,text="رقم السيارة")
            Spnlabltext.grid(row=0,column=0,pady=10,padx=5)
            number_Care_entry= ttk.Entry(Spnlabltext,justify='right')
            number_Care_entry.insert(0,"رقم السيارة")
            number_Care_entry.grid(row=0, column=0,padx=5, pady=10, sticky="ew")
            number_Care_entry.bind("<FocusIn>",lambda e: number_Care_entry.delete(0,'end'))
            
            treeFrameButon = ttk.Frame(widgets_frame,width=40)
            treeFrameButon.grid(row=6,column=0, padx=10, pady=(10, 5), sticky="nsew")
            
            
            
            self.Buttom_all_save()

            treeFrame = ttk.Frame(self,width=1050,height=700)
            treeFrame.grid(row=1,column=0, pady=5,padx=10)
            treeFrame.pack_propagate(0)

            treeScroll = ttk.Scrollbar(treeFrame,orient='vertical')
            treeScroll.pack(side="right", fill="y")
            
            treeScrollButtom = ttk.Scrollbar(treeFrame,orient='horizontal')
            treeScrollButtom.pack(side='bottom', fill="x")
            cols= ('الفرزة',"الترخيص","رقم السيارة", "لون السيارة","نوع السيارة",
                   "رقم البطاقة","اسم السائق",'معرف السائق',"م")

            treeview = ttk.Treeview(treeFrame, show="headings",
                                    yscrollcommand=treeScroll.set,xscrollcommand=treeScrollButtom.set, columns=cols, height=700)
            treeview.column("م",anchor="center",)
            treeview.column("معرف السائق",anchor="center")
            treeview.column("اسم السائق",anchor="center")
            treeview.column("رقم البطاقة",anchor="center")
            treeview.column("نوع السيارة",anchor="center")
            treeview.column("لون السيارة",anchor="center")
            treeview.column("رقم السيارة",anchor="center")
            treeview.column("الترخيص",anchor="center")
            treeview.column("الفرزة",anchor="center")
            treeview.tag_bind("row",'<Button-3>', lambda event: self.on_tree_view_select(event))
            # treeview.column("Employment",width=100,anchor="center")
            treeview.pack(side="right",pady=5)
            treeScroll.config(command=treeview.yview)
            treeScrollButtom.config(command=treeview.xview)
            treeview.xview_moveto(100)
            self.keyPrssnum = 0 

    def Buttom_all_save(self):
            global button_image_care
            global button_image_drive
            global button_image_thelabl
            global buttonInsert
            button_image_care = ttk.Button(treeFrameButon,text=" صورة للسيارة",
                                 command=lambda:self.import_Image('url_Image_care'),width=14)
            button_image_care.grid(row=0, column=0,padx=5, pady=5, sticky="ew")
            
            button_image_drive = ttk.Button(treeFrameButon,text="أخذ صورة للسائق",
                                 command=lambda:self.import_Image('url_Image_drive'),width=14)
            button_image_drive.grid(row=0, column=1,padx=5, pady=5, sticky="ew")
            
            button_image_thelabl = ttk.Button(treeFrameButon,text="صورة الترخيص",
                                 command=lambda:self.import_Image('url_image_license'),width=14)
            button_image_thelabl.grid(row=0, column=2,padx=5, pady=5, sticky="ew")
            

            buttonT = ttk.Button(treeFrameButon,text="تهيئة",
                                 command=self.databis,width=14)
            buttonT.grid(row=1, column=2,padx=5, pady=5, sticky="ew")
            
            buttonInsert = ttk.Button(treeFrameButon,text="حفظ", 
                                      command=self.insert_row,width=14)
            buttonInsert.grid(row=1, column=1,padx=5, pady=5, sticky="ew")
        

    def veiw_image(self,filename,new=90):
        self.image = Image.open(filename)
        print(self.image)

        width , height = self.image.size
        aspect_ratio = width / height
        new_width = new
        new_height = int(new_width / aspect_ratio)
        resized_imag = self.image.resize((new_width,new_height))

        self.photo = ImageTk.PhotoImage(resized_imag)


        return self.photo

    def extra_veiw_image(self,kin_opration):
        if kin_opration == 'url_Image_drive':
            button_image_drive.config(image=self.Url_drive[kin_opration]['showe'])
        elif kin_opration == 'url_image_license':
            button_image_thelabl.config(image=self.Url_drive[kin_opration]['showe'])
        else:
            button_image_care.config(image=self.Url_drive[kin_opration]['showe'])


    def prossecc(self):
        self.insert_row()


    def import_Image(self,kin_opration):
        def select(kind):
            if kind == 'files':
                filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="select image file",
                    filetypes=(("jpg File", ".jpg"),
                            ("JPG File",".JPG"),
                            ("PNG File",".PNG"),
                            ("png File",".png"),
                            ("All file", ".text")))
            else:
                filename= cameraCop()
            # self.Url_drive[kin_opration] = {"url":filename}
            photo = self.veiw_image(filename)

            self.Url_drive[kin_opration] = {'url':filename,'showe':photo}
            self.extra_veiw_image(kin_opration)
            min.destroy()
        min= select_custom(self,'المكتب',select,contro.list_file,contro.camera) 



    def SwitchData(self,saw,Page):
        Man = tk.Menu(Page,tearoff=0)
        Man.add_command(label="اليومي",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='day'))
        Man.add_command(label="الشهري",columnbreak=10,accelerator=" ",command=lambda:self.load_data(statemant=saw,tim='month'))
        Man.post(Page.winfo_rootx(),Page.winfo_rooty())

    #  عملية  الصرف
    def insert_row(self,v=None):
        try:
            ColorCare = Color_care.get()
            kindCare= kind_care_entry.get()
            ID_numberCart= ID_numberCart_entry.get()
            namedrive= namedrive_entry.get()
            number_Care= number_Care_entry.get()
            Guarantee= Guarantee_entry.get()
            sorting = IDsort_entry.get()
            
            
            station =  StationMonthSqly.inComin_dataAll()
            
            ObjectALl_Station = next((ite for ite in station 
                                      if ite['nameSorting'].lower().replace(" ","") == sorting.lower().replace(" ","") 
                                      ),None)
            
            if len(namedrive) > 0 and  namedrive != 'اسم السائق' and len(ID_numberCart) > 0 and ID_numberCart != 'رقم البطاقة' and len(number_Care) > 0 and number_Care !=  "رقم السيارة" and len(kindCare) > 0 and kindCare != 'نوع السيارة' and len(station) > 0 and len(self.Url_drive) >=2 :
                try:
                    image_care = convert_image_buffer(self.Url_drive['url_Image_care']['url'])
                except :
                      image_care = None
                
                try:
                    image_drive = convert_image_buffer(self.Url_drive['url_Image_drive']['url'])
                except :
                      image_drive = None

                try: 
                    image_license = convert_image_buffer(self.Url_drive['url_image_license']['url'])
                except :
                      image_license = None

                if ObjectALl_Station is not None:
                    # print(ObjectALl_Station['nameSorting'])
                    # IDsort = ObjectALl_Station['IDsort']
                    IDsort = sorting
                    
                    if v is None:
                        iddrive = randomnumber()
                        StationMonthSqly.insert_Pablic(iddrive,namedrive,ID_numberCart,kindCare,
                                                       ColorCare,number_Care,Guarantee,IDsort
                                                       ,image_care,image_drive,image_license)
                    else:

                        StationMonthSqly.insert_Pablic(v,namedrive,ID_numberCart,kindCare,
                                                       ColorCare,number_Care,Guarantee,IDsort,
                                                       image_care,image_drive,image_license,type='update')
                    opration = {"kindopr":"تعديل" if v is not None else 'إضافة',"Timeopr":str(datetime.now().time()),'nameusefly':str(namedrive),'nameusefly_1':None}
                    InsertJson(opration)
                    self.databis()
                    self.load_data()
                    self.brcod = False
                    gc.collect()
                    buttonInsert.config(text="إضافة", command=self.insert_row)
                    self.empytePage()
                else:
                       messagebox.showwarning(title="Error", message="لايتطابق اسم الفرزة مع اسماء الفرز الموجودة")
            else:
                if len(station) <= 0:  
                    messagebox.showwarning(title="Error", message="يجب ادخال بيانات الفرز اولاً")
                else:
                    messagebox.showwarning(title="Error", message="يجب ادخال البيانات اولاً")
                
                # self.empytePage()
        except ValueError:
            messagebox.showwarning(title="Error", message="يجب ادخال البيانات اولاً")
    #عمليات التعديل

    

    def on_tree_view_select(self,event): 
            try:
                id_row = treeview.identify_row(event.y)
                treeview.selection_set(id_row)          
                row_value = treeview.item(id_row)["values"] 
                # print(row_value)
                selectClick = tk.Menu(treeview,tearoff=0)
                # print( row_value[7])
                dataMath = next((ite for ite in driveData if int(ite['iDdrive']) == int(row_value[7])),None)
                if dataMath is not None:
                    selectClick.add_command(
                        label='تعديل',
                        command=lambda:self.empyteُEdit(row_value))
                    selectClick.add_command(
                    label='عرض',
                    accelerator='view',
                    command=lambda:self.view_data_drive(dataMath))
                selectClick.post(event.x_root,event.y_root)
            except:
                print('خطاء تحديد')

    # view data drive all
    def view_data_drive(self,data_drive):
        self.OOp = {}
        frame_trovle = Moudel(self,data_drive['namedrive'])
        frame_window = ttk.Frame(frame_trovle)
        frame_window.pack(side="top", fill='both', pady=10,padx=10)

        for index in [0,1,2,3,4,5]:
            frame_window.columnconfigure(index=index,weight=1)
            frame_window.rowconfigure(index=index,weight=1)
        
        photo_care = self.veiw_image(io.BytesIO(data_drive['url_Image_care']),new=450)
        self.OOp['care'] = photo_care
        photo_personality = self.veiw_image(io.BytesIO(data_drive['url_Image_drive']),new=250)
        self.OOp['drive'] = photo_personality
        photo_license = self.veiw_image(io.BytesIO(data_drive['url_image_license']),new=200)
        self.OOp['license'] = photo_license



        label_care = tk.Label(frame_window, image=self.OOp['care'])
        label_care.grid(row=0,column=0,padx=10,pady=10)

        label_license = tk.Label(frame_window, image=self.OOp['license'])
        label_license.grid(row=1,column=0,padx=10,pady=10)



        frame_label= ttk.LabelFrame(frame_window,text='بيانات السائق')
        frame_label.grid(row=0,column=1,padx=10,pady=10)
        label_personality = tk.Label(frame_label, image=self.OOp['drive'])
        label_personality.grid(row=0,column=0,padx=10,pady=10)

        label_name = tk.Label(frame_label, text=f"الاسم:{data_drive['namedrive']}")
        label_name.grid(row=1,column=0,padx=10,pady=10)
        
        label_ID_numberCart = tk.Label(frame_label, text=f"البطاقة الشخصية:{data_drive['ID_numberCart']}")
        label_ID_numberCart.grid(row=2,column=0,padx=10,pady=10)

        label_kind_care = tk.Label(frame_label, text=f"نوع السيارة:{data_drive['kind_care']}")
        label_kind_care.grid(row=3,column=0,padx=10,pady=10)
        
        label_color_care = tk.Label(frame_label, text=f"لون السيارة:{data_drive['Color_care']}")
        label_color_care.grid(row=4,column=0,padx=10,pady=10)
        
        label_numberCart = tk.Label(frame_label, text=f"رقم السيارة:{data_drive['number_Care']}")
        label_numberCart.grid(row=5,column=0,padx=10,pady=10)



    #  عمليات التحديث
    def empyteُEdit(self,row):
        print(row)
        self.empytePage() 
        Color_care.delete(0,'end')
        Color_care.insert(0,row[3])
        kind_care_entry.delete(0,"end")
        ID_numberCart_entry.delete(0,"end")
        namedrive_entry.delete(0,"end")
        IDsort_entry.set(row[0])
        ID_numberCart_entry.insert(0,row[5])
        namedrive_entry.insert(0,row[6])
        number_Care_entry.delete(0,"end")
        number_Care_entry.insert(0,row[2])
        Guarantee_entry.delete(0,"end")
        Guarantee_entry.insert(0,row[1])
        kind_care_entry.insert(0,row[4])
        buttonInsert.config(command=lambda:self.insert_row(v=row[7]))
        userConternr.grid_forget()
        namerecevid.grid(row=4,column=0,pady=15,padx=5)
        Data_drive = StationMonthSqly.brings_drive_Pablic()
        for pic in Data_drive:
            if int(pic['iDdrive']) == int(row[7]):
                
                if pic['url_Image_care'] is not None:
                    photo = self.veiw_image(io.BytesIO(pic['url_Image_care']))
                    self.Url_drive['url_Image_care']={'url':io.BytesIO(pic['url_Image_care']),'showe':photo}
                
                if pic['url_Image_drive'] is not None:
                    photo_drive = self.veiw_image(io.BytesIO(pic['url_Image_drive']))
                    self.Url_drive['url_Image_drive']={'url':io.BytesIO(pic['url_Image_drive']),'showe':photo_drive}
                
                if pic['url_image_license'] is not None:
                    photo_license = self.veiw_image(io.BytesIO(pic['url_image_license']))
                    self.Url_drive['url_image_license']={'url':io.BytesIO(pic['url_image_license']),'showe':photo_license}
        
        for item in list(self.Url_drive):
             print(item)
             self.extra_veiw_image(item)




    #  عمليات التحديث
    def empytePage(self):
                Color_care.delete(0,'end')
                Color_care.insert(0,'لون السيارة')
                kind_care_entry.delete(0,"end")
                ID_numberCart_entry.delete(0,"end")
                namedrive_entry.delete(0,"end")
                ID_numberCart_entry.insert(0,'رقم البطاقة')
                namedrive_entry.insert(0,'اسم السائق')
                number_Care_entry.delete(0,"end")
                number_Care_entry.insert(0,"رقم السيارة")
                Guarantee_entry.delete(0,"end")
                Guarantee_entry.insert(0,"رقم الرخصة")
                kind_care_entry.insert(0,'نوع السيارة')
                IDsort_entry.delete(0,'end')
                userConternr.grid_forget()
                
                for picdl in treeFrameButon.winfo_children():
                      picdl.destroy()
                # button_image_drive.config(text="صورة للسائق",image=0)
                # button_image_thelabl.config(text="صورة الترخيص",image=0)
                # button_image_care.config(text="صورة للسيارة",image=0)
                
            
                self.Buttom_all_save()
                self.Url_drive= {}

                namerecevid.grid(row=4,column=0,pady=15,padx=5)
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
        global station
        global driveData
        index = 0
        station =  StationMonthSqly.inComin_dataAll()
        arrayPash= []
        items= treeview.get_children()
        for item in items:
                treeview.delete(item)
        treeview.update()
        lisvalues = list({'الفرزة',"الترخيص","رقم السيارة", "لون السيارة","نوع السيارة","رقم البطاقة","اسم السائق",'معرف السائق',"م"})
        
        for col_name in lisvalues:
                treeview.heading(col_name, text=col_name)
        driveData = StationMonthSqly.brings_drive_Pablic()
        for i in driveData:
            index += 1
            sort = next((f for f in station if f['nameSorting'] == i['IDsort'] ),None)
            objectTree = (sort['nameSorting'],i['Guarantee'],i['number_Care'],i['Color_care'],i['kind_care'],i['ID_numberCart'],i['namedrive'],i["iDdrive"],index)
            treeview.insert('', tk.END, values=objectTree,tags=("event",'row'))
            treeview.configure(selectmode='extended') 
    
        Datasort  = StationMonthSqly.inComin_dataAllwitch()
        for r in Datasort:
                print(r[1])
                DataSOrt.append(r[1])
        IDsort_entry.config(values=DataSOrt)
        gc.collect()
        


