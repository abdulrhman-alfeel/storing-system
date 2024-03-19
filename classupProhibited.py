from tkinter import ttk , filedialog, messagebox
import tkinter as tk
from PIL import ImageTk ,Image
import os
from convertcod.TOPlevel import Moudel
from sqiltyFoun import StationMonthSqly
from datetime import datetime , timedelta
from convertcod.view_image import   convert_image_buffer
import re
import io
from convertcod.userfind import responsebletUser
from convertcod.internal_storage import InsertJson
from convertcod.camera import cameraCop
from convertcod.TOPlevel import select_custom

import time
import tracemalloc



class Prohibited(tk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global canves_trafficker_kind
        global url_image_trafficker
        global url_image_prohibited
        global Button_image_prohibited
        global Button_image_trafficker

        global Entry_prohibited_1
        global Entry_prohibited_2
        global Entry_prohibited_3
        global Entry_prohibited_4
        global Entry_prohibited_5
        global url_image_prohibited_u
        global url_image_trafficker_u
        global Frame_continer_images
        global canves_trafficker
        global canves_trafficker_kind
        global button_new_prohibited
        global array_sorting 
        global Entry_prohibited_6
        global controllicon


        controllicon = controller
        url_image_trafficker ={}
        url_image_prohibited ={}

        url_image_trafficker_u ={}
        url_image_prohibited_u ={}

        array_sorting = []

        Frame_buttom_top = ttk.Frame(self,padding=(5,10))
        Frame_buttom_top.pack(side='top')

        button_new_list_prohibited = tk.Button(Frame_buttom_top,border=0,text='جديد  قائمة الممنوعات',command=self.Add_prohibited)
        button_new_list_prohibited.pack(side='right',pady=5,padx=20)

        button_new_list_view = tk.Button(Frame_buttom_top,border=0,text=' المضبوطات',command=self.veiw_data_cash)
        button_new_list_view.pack(side='right',pady=5,padx=20)



        Frame_form = tk.Frame(self)
        Frame_form.pack(side='top',padx=30)
        Frame_continer_entry = ttk.LabelFrame(Frame_form,padding=(5,5))
        Frame_continer_entry.pack(side='right',padx=20)

        
        Frame_label_1 = ttk.LabelFrame(Frame_continer_entry,text='نوع المضبوط',)
        Frame_label_1.grid(row=0,column=1,padx=5,pady=5)
        Entry_prohibited_1 = ttk.Combobox(Frame_label_1,justify='center')
        Entry_prohibited_1.grid(ipadx=10,padx=5,pady=5)


        Frame_label_2 = ttk.LabelFrame(Frame_continer_entry,text='كمية المضبوط')
        Frame_label_2.grid(row=0,column=0,padx=5,pady=5)
        Entry_prohibited_2 = ttk.Entry(Frame_label_2,justify='center')
        Entry_prohibited_2.grid(ipadx=10,padx=5,pady=5) 
        

        Frame_label_3 = ttk.LabelFrame(Frame_continer_entry,text='اسم المهرب')
        Frame_label_3.grid(row=1,padx=5,pady=5,columnspan=30)
        Entry_prohibited_3 = ttk.Entry(Frame_label_3,justify='center')
        Entry_prohibited_3.grid(ipadx=40,padx=5,pady=5) 


        Frame_label_4 = ttk.LabelFrame(Frame_continer_entry,text='جنس المهرب')
        Frame_label_4.grid(row=2,column=1,ipadx=10,padx=5,pady=5)
        Entry_prohibited_4 = ttk.Entry(Frame_label_4,justify='center')
        Entry_prohibited_4.grid(padx=5,pady=5) 
        

        Frame_label_5 = ttk.LabelFrame(Frame_continer_entry,text='عمر المهرب')
        Frame_label_5.grid(row=2,column=0,ipadx=10,padx=5,pady=5)
        Entry_prohibited_5 = ttk.Entry(Frame_label_5,justify='center')
        Entry_prohibited_5.grid(padx=5,pady=5) 


        Frame_label_6 = ttk.LabelFrame(Frame_continer_entry,text='الفرزة المضبوط فيها ')
        Frame_label_6.grid(row=3,column=0,ipadx=10,padx=5,pady=5)
        Entry_prohibited_6 = ttk.Combobox(Frame_label_6,justify='center')
        Entry_prohibited_6.grid(padx=5,pady=5) 


        Frame_continer_images = ttk.LabelFrame(Frame_form,padding=(20,10))
        Frame_continer_images.pack(side='right',padx=25)
        
        canves_trafficker = tk.Canvas(Frame_continer_images,width=350,height=300)
        canves_trafficker.grid(row=0,column=0,padx=5,pady=5)
        canves_trafficker.pack_propagate(0)


        Button_image_trafficker = tk.Button(canves_trafficker,width=35,height=10
                                            ,text='صورة المهرب',command=lambda:self.select_image('trafficker'))    
        Button_image_trafficker.pack(fill='both',expand=True)



        canves_trafficker_kind = tk.Canvas(Frame_continer_images,width=400,height=350,border=4,)
        canves_trafficker_kind.grid(row=0,column=1,padx=15,pady=15,)
        canves_trafficker_kind.pack_propagate(0)
    
        Button_image_prohibited = tk.Button(canves_trafficker_kind,width=35,height=15,
                                            text='صورة المادةالمضبوط',command=lambda:self.select_image('prohibited'))    
        Button_image_prohibited.pack(fill='both',expand=True)

        Frame_buttom= ttk.Frame(self)
        Frame_buttom.pack(side='bottom',fill='both',pady=20,padx=20)
        button_new_prohibited = ttk.Button(Frame_buttom,text='اضافة',command=self.inser_prohibited)
        button_new_prohibited.pack(fill='both',pady=20,padx=20)
        button_new_reste = ttk.Button(Frame_buttom,text='تهيئة',command=self.Empyt)
        button_new_reste.pack(fill='both',pady=20,padx=20)
        self.loades_name_prohibited()
        # self.lodes()
    def Add_prohibited(self):
        main = Moudel(self,'اضافة ممنوعات جديدة')
        Top_3 = ttk.Frame(main)
        Top_3.pack(fill='both',expand=True)
        
        fram_Topd = tk.LabelFrame(Top_3)
        fram_Topd.pack(side='top',expand=True)
        
        code_frame = ttk.LabelFrame(fram_Topd,text='اسم الممنوع')
        code_frame.grid(row=0, column=0,padx=10, pady=10, )
        codeItems_entry = ttk.Entry(code_frame, width=20 )
        codeItems_entry.grid(padx=10,pady=10)
        
        amount_frame = ttk.LabelFrame(fram_Topd,text='كمية الممنوع')
        amount_frame.grid(row=1, column=0,padx=10, pady=10, )
        amountItems_entry = ttk.Combobox(amount_frame,values=["كل الكميات"], width=20 )
        amountItems_entry.grid(padx=10,pady=10)


        tabel = ttk.LabelFrame(Top_3,width=100)
        tabel.pack()
        scrollbar_box = ttk.Scrollbar(tabel,orient='vertical')
        scrollbar_box.pack(side='right',fill='y')
        col = ('الكمية الممنوعة',"اسم الممنوع")
        list_box = ttk.Treeview(tabel,show='headings',columns=col,yscrollcommand=scrollbar_box.set)
        list_box.pack(expand=True)
        list_box.column('اسم الممنوع',width=150,anchor='center')
        list_box.column('الكمية الممنوعة',width=150,anchor='center')
        list_box.tag_bind("row",'<Button-3>',lambda e:update_it(e))
    
        def Add(type=None):
            if len(codeItems_entry.get()) > 0 and len(amountItems_entry.get()) > 0 :
                    if type is None:
                        StationMonthSqly.insert_LIST_prohibited(codeItems_entry.get(),amountItems_entry.get())
                    else:
                        StationMonthSqly.insert_LIST_prohibited(codeItems_entry.get(),amountItems_entry.get(),type)
                    get_it()
                    empty_entry()
            # man.destroy()
                # else:
                #     print('error')
            # except:
            #     pass    
        def get_it():
            children = list_box.get_children()
            for d in children:
                list_box.delete(d)

            column = list({'الكمية الممنوعة',"اسم الممنوع"})
            for col_name in column:
                list_box.heading(col_name,text=col_name)
            data = StationMonthSqly.get_list_prohibited()
            array_compex = []
            for item in data:
                # print(item)
                array_compex.append(item[2])
                list_box.insert('',tk.END,values=(item[3],item[2]),tags=('even','row'))
                list_box.configure(selectmode='extended') 

            Entry_prohibited_1.config(values=array_compex)
        get_it()
            
            
        def update_it(event):
            id_row = list_box.identify_row(event.y)
            list_box.selection_set(id_row)          
            row_value = list_box.item(id_row)["values"] 
            # print(row_value)
            numberprevdis = row_value[1]
            codeItems_entry.delete(0,'end')                 
            codeItems_entry.insert(0,numberprevdis)
            
            amountItems_entry.delete(0,'end')                 
            amountItems_entry.insert(0,row_value[0])
            data = StationMonthSqly.get_list_prohibited()
            
            OOp = next((item for item in data if item[2] == row_value[1]),None)
            insert_attachment.config(command=lambda: Add(type=OOp[0]),text='تعديل')


        def empty_entry():
            codeItems_entry.delete(0,'end')
            amountItems_entry.delete(0,'end')
            insert_attachment.config(command=Add,text='اضافة')

        insert_attachment = ttk.Button(Top_3,text='اضافة',width=20, command=Add)
        insert_attachment.pack(side="top",padx=10,pady=10)

        Add_attachment = ttk.Button(Top_3,text='تهيئة',width=20, command=empty_entry)
        Add_attachment.pack(side="top",padx=10,pady=10)





    def loades_name_prohibited(self):
            data = StationMonthSqly.get_list_prohibited()
            array_compex = []
            for item in data:
                print(item)
                array_compex.append(item[2])
            Entry_prohibited_1.config(values=array_compex)


    def inser_prohibited (self,kind=None):
        global Button_image_prohibited
        global Button_image_trafficker
        # global url_image_prohibited_u
        global url_image_trafficker_u
        name_prohibited = Entry_prohibited_1.get()
        amount = Entry_prohibited_2.get()
        trafficker_name = Entry_prohibited_3.get()
        gunder_trafficker = Entry_prohibited_4.get()
        age_trafficker = Entry_prohibited_5.get()
        index = 0
        for F in (name_prohibited,amount,trafficker_name,gunder_trafficker,age_trafficker,str(url_image_prohibited_u),str(url_image_trafficker_u),Entry_prohibited_6.get()):
            if len(F) > 0:
                index +=1
        
        if index >= 7:
            print(url_image_prohibited_u)
            user = responsebletUser()
            image_prohibited = convert_image_buffer(url_image_prohibited_u)
            image_trafficker = convert_image_buffer(url_image_trafficker_u)
            if kind is None:
                StationMonthSqly.insert_Pablic_prohibited(name_prohibited,amount,trafficker_name,gunder_trafficker,
                                                          age_trafficker,image_prohibited,image_trafficker,user['userName'],Entry_prohibited_6.get())
            else:    
                StationMonthSqly.insert_Pablic_prohibited(name_prohibited,amount,trafficker_name,gunder_trafficker
                                                          ,age_trafficker,image_prohibited,image_trafficker,user['userName'],Entry_prohibited_6.get(),kind)
            
            opration = {"kindopr":"تعديل" if kind is not None else 'إضافة',"Timeopr":str(datetime.now().time()),'nameusefly':str(name_prohibited),'nameusefly_1':str(trafficker_name)}
            InsertJson(opration)
            self.Empyt()
        else:
            messagebox.showwarning(title='البيانات ناقصة',message= 'اكمل البيانات إذا سمحت')



    def Empyt(self):
            global url_image_prohibited_u
            global url_image_trafficker_u
            global Button_image_prohibited
            global Button_image_trafficker

            for F in (Entry_prohibited_1,Entry_prohibited_2,Entry_prohibited_3,Entry_prohibited_4,Entry_prohibited_5):
                    F.delete(0,'end')
                
            url_image_trafficker_u = {}
            url_image_prohibited_u = {}

            for P in canves_trafficker.winfo_children():
                P.destroy()
            
            for d in canves_trafficker_kind.winfo_children():
                d.destroy()
            

            Button_image_trafficker = tk.Button(canves_trafficker,width=35,height=10
                                                ,text='صورة المهرب',command=lambda:self.select_image('trafficker'))    
            Button_image_trafficker.pack(fill='both',expand=True)

            Button_image_prohibited = tk.Button(canves_trafficker_kind,width=35,height=15,
                                                text='صورة المادةالمضبوط',command=lambda:self.select_image('prohibited'))    
            Button_image_prohibited.pack(fill='both',expand=True)
            button_new_prohibited.config(text='إضافة',command=self.inser_prohibited)


    def lodes(self):
        Datasort  = StationMonthSqly.inComin_dataAllwitch()
        for r in Datasort:
                # print(r[1])
            array_sorting.append(r[1])
        Entry_prohibited_6.config(values=array_sorting)


    def  select_image(self,kind) :
        global url_image_trafficker
        global url_image_prohibited
        global url_image_prohibited_u
        global url_image_trafficker_u

        def select(selectedkind):
            global url_image_trafficker
            global url_image_prohibited
            global url_image_prohibited_u
            global url_image_trafficker_u
            if selectedkind == 'files':
                url_select = filedialog.askopenfilename(initialdir=os.getcwd,title='select image licenses',
                                                                filetypes=(('jpg file','.jpg'),
                                                                            ('JPG FILE','.JPG'),
                                                                            ('PNG FILE','.PNG'),
                                                                            ('png file','.png'),
                                                                            ('All file','text')))
            elif selectedkind == 'camera':
                url_select = cameraCop()
            else:
                pass

            if url_select is not None:
                try:
                    if kind == 'prohibited':
                        url_image_prohibited_u = url_select
                        url_bse64= self.veiw_image(url_select,new=400)
                        url_image_prohibited = url_bse64
                        Button_image_prohibited.config(image=url_image_prohibited,border=0)
                        Button_image_prohibited.update_idletasks()
                    else:
                        url_image_trafficker_u = url_select
                        url_bse64= self.veiw_image(url_select,new=350)
                        url_image_trafficker = url_bse64
                        Button_image_trafficker.config(image=url_image_trafficker,border=0)
                        Button_image_trafficker.update_idletasks()
                    min.destroy()
                except:
                    pass
     
        min= select_custom(self,'الممنوعات',select,controllicon.list_file,controllicon.camera) 
       

      
    



    def veiw_image(self,filename,new=90):
          
        self.image = Image.open(filename)
        print(self.image)

        width , height = self.image.size
        aspect_ratio = width / height
        new_width = new
        new_height = int(new_width / aspect_ratio)
        resized_imag = self.image.resize((new_width,new_height))

        photo = ImageTk.PhotoImage(resized_imag)
        return photo
    


    def veiw_data_cash(self):
        global root_view
        data_time = []

        # start_time = datetime(2024,1,1)
        start_time = datetime.now()
        end_time = datetime(2030,1,1)


        def search_function(e):
            sear= search_entry_1.get()
            print(e)
            if e.keycode != 8:
                loding_view_prohibited(sear)
            else:
                loding_view_prohibited()

        for day in range((end_time - start_time).days + 1):
            datays = start_time + timedelta(days=day)
            data_time.append(datays.date())

        root_view = Moudel(self,'عرض المضبوطات')

        Frame_search = ttk.Frame(root_view)
        Frame_search.pack(side='top',padx=10,pady=10)

        search_entry_1 = ttk.Entry(Frame_search,justify='center')
        search_entry_1.grid(row=0,column=2,)
        search_entry_1.insert(0,'ابحث  عن ماتريد')
        search_entry_1.bind("<FocusIn>", lambda e: search_entry_1.delete(0,'end'))
        search_entry_1.bind("<KeyRelease>", lambda e : search_function(e))

        search_entry_2 = ttk.Entry(Frame_search,justify='center')
        search_entry_2.grid(row=0,column=1,)
        search_entry_2.insert(0,'نوع المضبوط')
        search_entry_2.bind("<FocusIn>", lambda e: search_entry_2.delete(0,'end'))
        

        search_entry_3 = ttk.Combobox(Frame_search,justify='center',values=data_time)
        search_entry_3.grid(row=0,column=0,)
        search_entry_3.current(0)
        # search_entry_3.insert(0,'نوع المضبوط')
        # search_entry_3.bind("<FocusIn>", lambda e: search_entry_3.delete(0,'end'))




        Frame_view = ttk.Frame(root_view)
        Frame_view.pack(side='top',padx=5,pady=5)

        scrolle_y = ttk.Scrollbar(Frame_view)
        scrolle_y.pack(side='right',fill='y')

        # coll = ("م","نوع المضبوط",'تاريخ الضبط','كمية المضبوط','اسم المهرب','جنس المهرب',"عمر المهرب")
        coll = ("عمر المهرب",'جنس المهرب','اسم المهرب','الكمية المضبوطة','نوع المضبوط','تاريخ الضبط','م')
        view_tree = ttk.Treeview(Frame_view, show='tree headings',
                                  yscrollcommand=scrolle_y.set,
                                  columns=coll
                                  )
        view_tree.pack(fill='both',expand=True)
        view_tree.column('م',anchor='center')
        view_tree.column('تاريخ الضبط',anchor='center')
        view_tree.column('نوع المضبوط',anchor='center')
        view_tree.column('الكمية المضبوطة',anchor='center')
        view_tree.column('اسم المهرب',anchor='center')
        view_tree.column('جنس المهرب',anchor='center')
        view_tree.column('عمر المهرب',anchor='center')
        view_tree.tag_bind('row',"<Button-3>",lambda e:on_tree_view_select(e))

        scrolle_y.config(command=view_tree.yview)
        imag_oop = {}
        
        def add_inseert_viewtree(pic):
            value = list(pic)
            value.reverse()

            view_tree.insert("",tk.END, values=value,tags=('event','row'))
            view_tree.configure(selectmode='extended')
     
        def loding_view_prohibited(kind= None):
            data_cash = StationMonthSqly.get_pablic_prohibited()

            tree_heading = list({"عمر المهرب",'جنس المهرب','اسم المهرب','الكمية المضبوطة','نوع المضبوط','تاريخ الضبط','م'})
            for items in tree_heading:
                view_tree.heading(items,text=items)

            virfy = False
           
            if search_entry_2.get() != 'نوع المضبوط' and len(search_entry_2.get()) > 0 :
                virfy = True
           
           
            for d in view_tree.get_children():
                    view_tree.delete(d)

            if kind is not None:
                for pic in data_cash:
                    # print(pic,'hhhh')
                    # if re.search(pic[4].replace(" ","").capitalize(),kind.replace(" ","").capitalize()):
                    if pic[4].lower().startswith(kind):
                        print(search_entry_1.get()) 
                        # if datetime.strptime(pic[1],"%Y-%m-%d").date() == datetime.strptime(search_entry_3.get(),"%Y-%m-%d").date():
                            # if virfy == True :
                            #    if re.search(pic[2].replace(" ",""),search_entry_2.get().replace(" ","")):
                                    # print('hhhhhhhh')
                                    # add_inseert_viewtree(pic)
                            # else:
                        add_inseert_viewtree(pic)
            else:
                for pic in data_cash:
                    # print(pic)
                   add_inseert_viewtree(pic)
        loding_view_prohibited()

 
 
        def on_tree_view_select(event):
            id_row = view_tree.identify_row(event.y)
            view_tree.selection_set(id_row)
            row_value = view_tree.item(id_row)['values']
            # print(row_value)
            Main = tk.Menu(view_tree,tearoff=0)
            cashing = StationMonthSqly.get_pablic_prohibited_All()

            data_prohibited = next((cash for cash in cashing if int(cash['ID']) == int(row_value[6])),None)
            
            Main.add_command(label='تعديل',accelerator='Eidte', command=lambda:self.Edit_data(data_prohibited))
                
            Main.add_command(label='عرض',accelerator='view',command=lambda:self.view_data_Prohibited(data_prohibited))
          
            Main.post(event.x_root,event.y_root)





    def Edit_data(self,item):
        global url_image_trafficker_u
        global url_image_prohibited_u
        global url_image_trafficker
        global url_image_prohibited
        global Button_image_trafficker
        global Button_image_prohibited
        self.Empyt()
        self.Object = {}
        Entry_prohibited_1.delete(0,'end')
        Entry_prohibited_1.insert(0,item['name_Prohibited'])
        Entry_prohibited_2.delete(0,'end')
        Entry_prohibited_2.insert(0,item['amount'])
        Entry_prohibited_3.delete(0,'end')
        Entry_prohibited_3.insert(0,item['trafficker'])
        Entry_prohibited_4.delete(0,'end')
        Entry_prohibited_4.insert(0,item['Gender_trafficker'])
        Entry_prohibited_5.delete(0,'end')
        Entry_prohibited_5.insert(0,item['AGE_trafficker'])
        photo_care = self.veiw_image(io.BytesIO(item['url_prohibited']),new=450)
        url_image_prohibited= photo_care
        url_image_prohibited_u = io.BytesIO(item['url_prohibited'])
        photo_personality = self.veiw_image(io.BytesIO(item['url_trafficker']),new=250)
        
        Button_image_prohibited.config(image=url_image_prohibited,border=0)
        Button_image_prohibited.update_idletasks()
        url_image_trafficker= photo_personality
        url_image_trafficker_u = io.BytesIO(item['url_trafficker'])
        Button_image_trafficker.config(image=url_image_trafficker,border=0)
        Button_image_trafficker.update_idletasks()
        button_new_prohibited.config(text='تعديل',command=lambda:self.inser_prohibited(item['ID']))
        try:
            frame_trovle.destroy()
        except:
            pass
        try:
            root_view.destroy()
        except:
            pass

        
          # view data drive all
    
    
    
    
    def view_data_Prohibited(self,data_prohibited):
        self.OOp = {}
        global frame_trovle

        frame_trovle = Moudel(self,data_prohibited['trafficker'])
        
        frame_window = ttk.Frame(frame_trovle)
        frame_window.pack(side="top", fill='both', pady=10,padx=10)

        
        for index in [0,1,2,3,4,5]:
            frame_window.columnconfigure(index=index,weight=1)
            frame_window.rowconfigure(index=index,weight=1)


        photo_care = self.veiw_image(io.BytesIO(data_prohibited['url_prohibited']),new=450)
        self.OOp['prohibited'] = photo_care
        photo_personality = self.veiw_image(io.BytesIO(data_prohibited['url_trafficker']),new=250)
        self.OOp['trafficker'] = photo_personality


        label_care = tk.Label(frame_window, image=self.OOp['prohibited'])
        label_care.grid(row=0,column=0,padx=10,pady=10)
     
        Button_care = ttk.Button(frame_window, text='تعديل',command=lambda:self.Edit_data(data_prohibited),width=40)
        Button_care.grid(row=1,column=0,padx=10,pady=10)

        frame_label= ttk.LabelFrame(frame_window,text='بيانات المهرب')
        frame_label.grid(row=0,column=1,padx=10,pady=10)

        label_personality = tk.Label(frame_label, image=self.OOp['trafficker'])
        label_personality.grid(row=0,column=0,padx=10,pady=10)
    
        label_name = tk.Label(frame_label, text=f"نوع المادة المهربة: {data_prohibited['name_Prohibited']}")
        label_name.grid(row=1,column=0,padx=10,pady=10)
        
        # label_ID_numberCart = tk.Label(frame_label, text=f"البطاقة الشخصية:{data_prohibited['ID_numberCart']}")
        # label_ID_numberCart.grid(row=2,column=0,padx=10,pady=10)

        label_kind_care = tk.Label(frame_label, text=f"الكمية: {data_prohibited['amount']}")
        label_kind_care.grid(row=2,column=0,padx=10,pady=10)
        
        label_color_care = tk.Label(frame_label, text=f"اسم المهرب: {data_prohibited['trafficker']}")
        label_color_care.grid(row=3,column=0,padx=10,pady=10)
        
        label_numberCart = tk.Label(frame_label, text=f"جنس المهرب: {data_prohibited['Gender_trafficker']}")
        label_numberCart.grid(row=4,column=0,padx=10,pady=10)

        label_age_trafficker = tk.Label(frame_label, text=f"عمر المهرب: {data_prohibited['AGE_trafficker']}")
        label_age_trafficker.grid(row=5,column=0,padx=10,pady=10)
        
