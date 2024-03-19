from tkinter import ttk , filedialog, messagebox
import tkinter as tk
from PIL import ImageTk ,Image
import os
from convertcod.TOPlevel import Moudel
from sqiltyFoun import StationMonthSqly
from datetime import datetime , timedelta
import re
from sqiltyFoun import StationMonthSqly
from convertcod.view_image import veiw_image,convert_image_buffer
from convertcod.json_parse import randomnumber
from convertcod.userfind import responsebletUser
import io
from convertcod.internal_storage import InsertJson
from convertcod.camera import cameraCop
from convertcod.TOPlevel import select_custom


class Deportees(tk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global canves_trafficker_kind
        global url_image
        global url_image_u
        global Button_imag_Arrest
        global Entry_Deportees_6

        # global Entry_Deportees_1
        global Entry_Deportees_1
        global Entry_Deportees_2
        global Entry_Deportees_3
        global Entry_Deportees_4
        global Entry_Deportees_5   
        global Entry_Deportees_7
        global Entry_Deportees_8
        global Frame_continer_images
        global Frame_continer_entry
        global canves_trafficker_kind
        global button_new_Deportees
        global arrays_drive
        global arrays_sort
        global contro

        contro = controller
        url_image ={}

        url_image_u ={}


        arrays_drive = []
        arrays_sort = []

        Frame_form = tk.Frame(self)
        Frame_form.pack(side='top',padx=30)
        Frame_continer_entry = ttk.LabelFrame(Frame_form,padding=(20,20))
        Frame_continer_entry.pack(side='right',padx=20)

        

        Entry_Deportees_2 = ttk.Entry(Frame_continer_entry,justify='center',width=50)
        Entry_Deportees_2.grid(row=0,column=0,ipadx=10,padx=5,pady=5) 
        Entry_Deportees_2.insert(0,'ابحث عن اسم المرحل')
        Entry_Deportees_2.bind("<FocusIn>", lambda e: Entry_Deportees_2.delete(0,'end'))
        Entry_Deportees_2.bind("<KeyRelease>",self.listner_name_deportees)
       

        Frame_label_2 = ttk.LabelFrame(Frame_continer_entry,text='ادخل اسم المرحل')
        Frame_label_2.grid(row=1,column=0,padx=5,pady=5)

        Entry_Deportees_1 = ttk.Entry(Frame_label_2,justify='center',width=50)
        Entry_Deportees_1.grid(row=1,column=0,ipadx=10,padx=5,pady=5) 
        # Entry_Deportees_1.bind("<KeyRelease>",self.listner_name_deportees)



        frame_gender = ttk.Frame(Frame_continer_entry)
        frame_gender.grid(row=2,column=0,padx=5,pady=5)
        
        Frame_label_3 = ttk.LabelFrame(frame_gender,text='العمر')
        Frame_label_3.grid(row=0,column=0,padx=5,pady=5)
        Entry_Deportees_3 = ttk.Entry(Frame_label_3,justify='center')
        Entry_Deportees_3.grid(padx=5,pady=5) 



        Frame_label_4 = ttk.LabelFrame(frame_gender,text='الجنس')
        Frame_label_4.grid(row=0,column=1,padx=5,pady=5)
        Entry_Deportees_4 = ttk.Entry(Frame_label_4,justify='center')
        Entry_Deportees_4.grid(padx=5,pady=5) 
        

 
        frame_CHARGE = ttk.Frame(Frame_continer_entry)
        frame_CHARGE.grid(row=3,column=0,padx=5,pady=5)
        Frame_label_5 = ttk.LabelFrame(frame_CHARGE,text='رقم البطاقة')
        Frame_label_5.grid(row=0,column=1,padx=5,pady=5)
        Entry_Deportees_5 = ttk.Entry(Frame_label_5,justify='center')
        Entry_Deportees_5.grid(padx=5,pady=5) 


        
        Frame_label_8 = ttk.LabelFrame(frame_CHARGE,text='الفرزة')
        Frame_label_8.grid(row=0,column=0,padx=5,pady=5)
        Entry_Deportees_8 = ttk.Combobox(Frame_label_8,justify='center')
        Entry_Deportees_8.grid(padx=5,pady=5) 
        Entry_Deportees_8.bind("<FocusIn>",self.select_sort)
   


        destination_Frame = ttk.Frame(Frame_continer_entry)
        destination_Frame.grid(row=4,column=0,padx=5,pady=5)
        

        Frame_label_6 = ttk.LabelFrame(destination_Frame,text='وجهة المرحل')
        Frame_label_6.grid(row=0,column=1,padx=5,pady=5)
        Entry_Deportees_6 = ttk.Combobox(Frame_label_6,justify='center')
        Entry_Deportees_6.grid(padx=5,pady=5) 

        Frame_label_7 = ttk.LabelFrame(destination_Frame,text='السواق')
        Frame_label_7.grid(row=0,column=0,padx=5,pady=5)
        Entry_Deportees_7 = ttk.Combobox(Frame_label_7,justify='center')
        Entry_Deportees_7.grid(padx=5,pady=5) 
  


        Frame_buttom= ttk.Frame(Frame_continer_entry)
        Frame_buttom.grid(row=5,column=0,padx=5,pady=5)
        button_new_Deportees = ttk.Button(Frame_buttom,text='اضافة',command=self.inser_Deprtees)
        button_new_Deportees.pack(side='right',fill='both',pady=20,padx=20)
        button_new_reste = ttk.Button(Frame_buttom,text='تهيئة',command=lambda:self.empty_All_deportees('restert'))
        button_new_reste.pack(side='right',fill='both',pady=20,padx=20)



        Frame_continer_images = ttk.LabelFrame(Frame_form,padding=(20,10))
        Frame_continer_images.pack(side='right',padx=25)
        


        canves_trafficker_kind = tk.Canvas(Frame_continer_images,width=400,height=550,border=4,)
        canves_trafficker_kind.grid(row=0,column=1,padx=15,pady=15,)
        canves_trafficker_kind.pack_propagate(0)
    #   ,height=15,
      
        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                            text='صورة المرحل',command=self.select_image_deportees)    
        Button_imag_Arrest.pack(fill='both',expand=True)




        
    def select_image_deportees(self):
        def select(kind):
            if kind == 'files':
                url_select = filedialog.askopenfilename(initialdir=os.getcwd,title='select image licenses',
                                                                filetypes=(('jpg file','.jpg'),
                                                                    ('JPG FILE','.JPG'),
                                                                    ('PNG FILE','.PNG'),
                                                                    ('png file','.png'),
                                                                    ('All file','text')))
            else:
                url_select= cameraCop()
            try:
                    self.opration_image_deportess(url_select)
                    min.destroy()
            except:
                pass
        
        min= select_custom(self,'المكتب',select,contro.list_file,contro.camera) 
        


        
    def opration_image_deportess(self,url_select):
        global url_image_u
        global url_image


        url_image_u = url_select
        url_bse64= veiw_image(url_select,new=400)
        url_image = url_bse64

        for desory in canves_trafficker_kind.winfo_children():
                desory.destroy()

        Button_imag_Arrest = tk.Button(canves_trafficker_kind,
                                    text='صورة المضبوط',command=self.select_image_deportees)   
         
        Button_imag_Arrest.pack(fill='both',expand=True)
        Button_imag_Arrest.config(image=url_image,border=0)
        Button_imag_Arrest.update_idletasks()





    def empty_All_deportees(self,k=None):
       
        for desory in canves_trafficker_kind.winfo_children():
                desory.destroy()

        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                            text='صورة المضبوط',command=self.select_image_deportees)    
        Button_imag_Arrest.pack(fill='both',expand=True)

        for item in (Entry_Deportees_1,Entry_Deportees_2,Entry_Deportees_3,Entry_Deportees_4,Entry_Deportees_5,Entry_Deportees_6,Entry_Deportees_7):
            item.delete(0,'end')
        Frame_continer_entry.config(text='')
        if k is not None:
            Entry_Deportees_2.insert(0,'ابحث عن اسم المرحل')

        



    def inser_Deprtees(self):
        self.OOp = {}
        Edite = False 

        vrification = 0
        namedeportees = Entry_Deportees_1.get()
        agedeportees = Entry_Deportees_3.get()
        Gender = Entry_Deportees_4.get()
        ID_numberCart = Entry_Deportees_5.get()
        destination = Entry_Deportees_6.get()
        ID_drive = Entry_Deportees_7.get()
        sorting = Entry_Deportees_8.get()
        

        for items in (Entry_Deportees_1,Entry_Deportees_3,Entry_Deportees_4
                      ,Entry_Deportees_5,Entry_Deportees_6,Entry_Deportees_7,Entry_Deportees_8):
            if len(items.get()) > 0 :
                vrification += 1

        # print(len(Frame_continer_entry.config('text')[4]))
        if isinstance(Frame_continer_entry.config('text')[4],int) :
             ID = Frame_continer_entry.config('text')[4]
             Edite = True
        else:
             ID = randomnumber()


        user = responsebletUser()

        if vrification >= 7  and len(url_image_u) > 0 :
            # convert url_image to blob image
            data_image = convert_image_buffer(url_image_u)

            self.OOp = {"ID":ID,'namedeportees':namedeportees,"Gender":Gender,"agedeportees":agedeportees,"ID_numberCart":ID_numberCart,
                        'iDdrive_DAY':ID_drive,'destination':destination,'Imageurl':data_image,'userName':user['userName'],'sorting':sorting}

            if Edite == True:
                StationMonthSqly.insert_pablic_Deportees(self.OOp,'update')         
            else:    
                StationMonthSqly.insert_pablic_Deportees(self.OOp)   
            opration = {"kindopr":"تعديل" if Edite is not None else 'إضافة',"Timeopr":str(datetime.now().time()),
                        'nameusefly':str(namedeportees),'nameusefly_1':None}
            InsertJson(opration)      
            
            self.empty_All_deportees(k='تم')
            self.lodes_deports()
        else:
             messagebox.showwarning(title='المعلومات',message='يجب اكمال البيانات')





    def listner_name_deportees(self,event):
        print(event)           
        
        for it in (90,88,67,86,66,78,77,188,190,191,222,186,76,75,74,71,72,70,68,83,65,81,87,69,82,84,89,85,73,79,80):
            if event.keycode == it:
                keyword = Entry_Deportees_2.get()
                print(keyword)
                resultes = self.filter_data_deportees(data, self.starts_Deportees_with_a,keyword)
            elif event.keycode == 8:
                 self.empty_All_deportees()
            else:
                 pass
        # print(resultes)





    def filter_data_deportees(self,data, condition,keyword):
        results = []
        varify = False
        try:
            for item in data:
                if condition(item['namedeportees'],keyword):
                    results.append(item)
                    varify = True

            if varify == True :
                for pic in results:
                    for items in (Entry_Deportees_1,Entry_Deportees_3,Entry_Deportees_4,Entry_Deportees_5,Entry_Deportees_6,Entry_Deportees_7):
                        items.delete(0,'end')
                    Frame_continer_entry.config(text=pic['ID'])
                    Entry_Deportees_1.insert(0,pic['namedeportees'])
                    Entry_Deportees_3.insert(0,pic['agedeportees'])
                    Entry_Deportees_4.insert(0,pic['Gender'])
                    Entry_Deportees_5.insert(0,pic['ID_numberCart'])
                    Entry_Deportees_6.insert(0,pic['destination'])
                    Entry_Deportees_7.insert(0,pic['iDdrive_DAY'])
                    try:
                        if len(pic['Imageurl']) > 0:
                            image_ure = io.BytesIO(pic['Imageurl'])
                            self.opration_image_deportess(image_ure)
                    except:
                        for desory in canves_trafficker_kind.winfo_children():
                                desory.destroy()

                        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                                    text='صورة المضبوط',command=self.select_image_deportees)    
                        Button_imag_Arrest.pack(fill='both',expand=True)
        except:
            pass
        return results
    




    def starts_Deportees_with_a(self,word,keyword):
        return word.lower().startswith(keyword)
    

    def lodes_deports(self):
        global data
        global Data_sort 
        data = StationMonthSqly.get_pablic_Deportees_DAY()
        Data_sort = StationMonthSqly.inComin_dataAll()
        for item in Data_sort:
            arrays_sort.append(item['nameSorting'])
        Entry_Deportees_8.config(values=arrays_sort)


# Data_insert['sorting']
    
    def select_sort(self,event):
        global arrays_drive
        arrays_drive=[]
        IDsort_data = next((pic for pic in Data_sort if pic['nameSorting'].lower() == Entry_Deportees_8.get().lower()),None)
        if IDsort_data is not None:       
            Drive_data = StationMonthSqly.brings_drive_Pablic()
            for item in Drive_data:
                if item['IDsort'] == IDsort_data['nameSorting'] :
                    arrays_drive.append(item['namedrive'])

            Entry_Deportees_6.config(values=IDsort_data['destination_Json'])
            Entry_Deportees_7.config(values=arrays_drive)