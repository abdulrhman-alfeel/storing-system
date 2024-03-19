from tkinter import ttk , filedialog, messagebox
import tkinter as tk
import os
from sqiltyFoun import StationMonthSqly
from datetime import datetime 
from convertcod.internal_storage import InsertJson
from sqiltyFoun import StationMonthSqly
from convertcod.view_image import veiw_image,convert_image_buffer
from convertcod.userfind import responsebletUser
import io 
from convertcod.camera import cameraCop
from convertcod.TOPlevel import select_custom

class Arrest_wanted(tk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global canves_trafficker_kind
        global url_image
        global url_image_u
        global Button_imag_Arrest
        global Entry_prohibited_6

        # global Entry_prohibited_1
        global Entry_prohibited_1
        global Entry_prohibited_2
        global Entry_prohibited_3
        global Entry_prohibited_4
        global Entry_prohibited_5
        global Frame_continer_images
        # global canves_trafficker
        global canves_trafficker_kind
        global button_new_prohibited
        global Entry_prohibited_7
        global data_sortin
        global contro

        contro = controller
        url_image ={}

        url_image_u ={}


        data_sortin = []

        Frame_form = tk.Frame(self)
        Frame_form.pack(side='top',padx=30)
        Frame_continer_entry = ttk.LabelFrame(Frame_form,padding=(20,20))
        Frame_continer_entry.pack(side='right',padx=20)

        
       

        Frame_label_2 = ttk.LabelFrame(Frame_continer_entry,text='ادخل اسم المضبوط')
        Frame_label_2.grid(row=0,column=0,padx=5,pady=5)

        Entry_prohibited_2 = ttk.Entry(Frame_label_2,justify='center',width=50)
        Entry_prohibited_2.grid(row=0,column=0,ipadx=10,padx=5,pady=5) 
        Entry_prohibited_2.insert(0,'ادخل اسم المضبوط')
        Entry_prohibited_2.bind("<FocusIn>", lambda e: Entry_prohibited_2.delete(0,'end'))
        Entry_prohibited_2.bind("<KeyRelease>",self.listner_name)


        Entry_prohibited_1 = ttk.Entry(Frame_label_2,justify='center',width=50)
        Entry_prohibited_1.grid(row=1,column=0,ipadx=10,padx=5,pady=5) 



        frame_gender = ttk.Frame(Frame_continer_entry)
        frame_gender.grid(row=1,column=0,padx=5,pady=5)
        
        Frame_label_3 = ttk.LabelFrame(frame_gender,text='العمر')
        Frame_label_3.grid(row=0,column=0,padx=5,pady=5)
        Entry_prohibited_3 = ttk.Entry(Frame_label_3,justify='center')
        Entry_prohibited_3.grid(padx=5,pady=5) 



        Frame_label_4 = ttk.LabelFrame(frame_gender,text='الجنس')
        Frame_label_4.grid(row=0,column=1,padx=5,pady=5)
        Entry_prohibited_4 = ttk.Entry(Frame_label_4,justify='center')
        Entry_prohibited_4.grid(padx=5,pady=5) 
        

 
        frame_CHARGE = ttk.Frame(Frame_continer_entry)
        frame_CHARGE.grid(row=2,column=0,padx=5,pady=5)
        Frame_label_5 = ttk.LabelFrame(frame_CHARGE,text='رقم البطاقة')
        Frame_label_5.grid(row=0,column=0,padx=5,pady=5)
        Entry_prohibited_5 = ttk.Entry(Frame_label_5,justify='center')
        Entry_prohibited_5.grid(padx=5,pady=5) 

        Frame_label_6 = ttk.LabelFrame(frame_CHARGE,text='التهمة')
        Frame_label_6.grid(row=0,column=1,padx=5,pady=5)
        Entry_prohibited_6 = ttk.Entry(Frame_label_6,justify='center')
        Entry_prohibited_6.grid(padx=5,pady=5) 
        

        Frame_label_7 = ttk.LabelFrame(Frame_continer_entry,text='الفرزة المضبوط فيها')
        Frame_label_7.grid(row=3,column=0,columnspan=40,padx=5,pady=5)
        Entry_prohibited_7 = ttk.Combobox(Frame_label_7,justify='center')
        Entry_prohibited_7.grid(padx=5,pady=5) 


        Frame_buttom= ttk.Frame(Frame_continer_entry)
        Frame_buttom.grid(row=4,column=0,padx=5,pady=5)
        button_new_prohibited = ttk.Button(Frame_buttom,text='اضافة',command=self.inser_Arrest)
        button_new_prohibited.pack(side='right',fill='both',pady=20,padx=20)
        button_new_reste = ttk.Button(Frame_buttom,text='تهيئة',command=lambda:self.empty_All("تهيئة"))
        button_new_reste.pack(side='right',fill='both',pady=20,padx=20)



        Frame_continer_images = ttk.LabelFrame(Frame_form,padding=(20,10))
        Frame_continer_images.pack(side='right',padx=25)
        
        # canves_trafficker = tk.Canvas(Frame_continer_images,width=350,height=300)
        # canves_trafficker.grid(row=0,column=0,padx=5,pady=5)
        # canves_trafficker.pack_propagate(0)


        # Button_image_trafficker = tk.Button(canves_trafficker,width=35,height=10
        #                                     ,text='بصمة المضبوط',command=lambda:self.select_image('trafficker'))    
        # Button_image_trafficker.pack(fill='both',expand=True)



        canves_trafficker_kind = tk.Canvas(Frame_continer_images,width=400,height=550,border=4,)
        canves_trafficker_kind.grid(row=0,column=1,padx=15,pady=15,)
        canves_trafficker_kind.pack_propagate(0)
    #   ,height=15,

        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                            text='صورة المضبوط',command=self.select_image)    
        Button_imag_Arrest.pack(fill='both',expand=True)


    def select_image(self):
        def select(kind):
            if kind == 'files':
                url_select = filedialog.askopenfilename(initialdir=os.getcwd,title='select image licenses',
                                                                filetypes=(('jpg file','.jpg'),
                                                                            ('JPG FILE','.JPG'),
                                                                            ('PNG FILE','.PNG'),
                                                                            ('png file','.png'),
                                                                            ('All file','text')))
            else:
                url_select = cameraCop()
            try:
                    self.opration_image(url_select)
                    min.destroy()
            except:
                pass
        min= select_custom(self,'المكتب',select,contro.list_file,contro.camera) 



        
    def opration_image(self,url_select):
        global url_image_u
        global url_image


        url_image_u = url_select
        url_bse64= veiw_image(url_select,new=400)
        url_image = url_bse64

        for desory in canves_trafficker_kind.winfo_children():
                desory.destroy()

        Button_imag_Arrest = tk.Button(canves_trafficker_kind,
                                    text='صورة المضبوط',command=self.select_image)   
        Button_imag_Arrest.pack(fill='both',expand=True)
        Button_imag_Arrest.config(image=url_image,border=0)
        Button_imag_Arrest.update_idletasks()





    def empty_All(self,k=None):
        for desory in canves_trafficker_kind.winfo_children():
                desory.destroy()

        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                            text='صورة المضبوط',command=self.select_image)    
        Button_imag_Arrest.pack(fill='both',expand=True)

        for item in (Entry_prohibited_1,Entry_prohibited_2,Entry_prohibited_3,Entry_prohibited_4,Entry_prohibited_5,Entry_prohibited_6):
            item.delete(0,'end')
        if k is not None:
            Entry_prohibited_2.insert(0,'ادخل اسم المضبوط')
        self.lodes()
        



    def inser_Arrest(self):
        vrification = 0
        name = Entry_prohibited_1.get()

        for items in (Entry_prohibited_1,Entry_prohibited_3,Entry_prohibited_4,Entry_prohibited_5,Entry_prohibited_6,Entry_prohibited_7):
            if len(items.get()) > 0 :
                vrification += 1

        if vrification >= 5  and len(str(url_image_u)) > 0 :
            user = responsebletUser()
            StationMonthSqly.Arrest_wanted(name_wanted=name,url_image_wanted=convert_image_buffer(url_image_u),user=user['userName'],sorting=Entry_prohibited_7.get())         
            opration = {"kindopr":'ضبط مطلوب',"Timeopr":str(datetime.now().time()),'nameusefly':name ,'nameusefly_1':None}
            InsertJson(opration) 
            self.empty_All(k='تم')
        else:
             messagebox.showwarning(title='المعلومات',message='يجب اكمال البيانات')





    def listner_name(self,event):
        print(event)
        
        for it in (90,88,67,86,66,78,77,188,190,191,222,186,76,75,74,71,72,70,68,83,65,81,87,69,82,84,89,85,73,79,80):
            if event.keycode == it:
                keyword = Entry_prohibited_2.get()
                resultes = self.filter_data(data, self.starts_with_a,keyword)
            elif event.keycode == 8:
                 self.empty_All()
            else:
                 pass
        # print(resultes)





    def filter_data(self,data, condition,keyword):
        results = []
        varify = False
        try:
            for item in data:
                if condition(item['name_wanted'],keyword):
                    results.append(item)
                    varify = True
            if varify == True :
                for pic in results:
                    for items in (Entry_prohibited_1,Entry_prohibited_3,Entry_prohibited_4,Entry_prohibited_5,Entry_prohibited_6):
                        items.delete(0,'end')
                    Entry_prohibited_1.insert(0,pic['name_wanted'])
                    Entry_prohibited_3.insert(0,pic['age_wanted'])
                    Entry_prohibited_4.insert(0,pic['Gender_wanted'])
                    Entry_prohibited_5.insert(0,pic['ID_numberCart'])
                    Entry_prohibited_6.insert(0,pic['charge'])
                    try:
                        if len(str(pic['url_image_wanted'])) > 0:
                            self.opration_image(io.BytesIO(pic['url_image_wanted']))
                    except:
                        for desory in canves_trafficker_kind.winfo_children():
                                desory.destroy()

                        Button_imag_Arrest = ttk.Button(canves_trafficker_kind,
                                                    text='صورة المضبوط',command=self.select_image)    
                        Button_imag_Arrest.pack(fill='both',expand=True)
                
        except:
            pass
        return results
    

    def starts_with_a(self,word,keyword):
        return word.lower().startswith(keyword)
    



    def lodes(self):
        global data
        data_sortin=[]
        data = StationMonthSqly.get_pablic_wanted()
        Data_sort = StationMonthSqly.inComin_dataAll()
        for item in Data_sort:
            # print(item)
            data_sortin.append(item['nameSorting'])
        Entry_prohibited_7.config(values=data_sortin)

    
    def lodes_data(self,items):
        # self.empty_All(self)
        Entry_prohibited_1.insert(0,items[1])
        Entry_prohibited_3.insert(0,items[2])
        Entry_prohibited_4.insert(0,items[3])
        Entry_prohibited_5.insert(0,items[4])
        Entry_prohibited_6.insert(0,items[5])
