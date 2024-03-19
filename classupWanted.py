from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from sqiltyFoun import StationMonthSqly
from convertcod.processor import on_KeyPress ,resource_path
import time
from convertcod.json_parse import randomnumber
from convertcod.TOPlevel import  Moudel
from convertcod.view_image import veiw_image
from convertcod.internal_storage import InsertJson
from convertcod.userfind import *
import io

last_updated_at = time.time()
class wanted(ttk.Frame):
    def __init__(self, parent,controller):
        ttk.Frame.__init__(self,parent)
        global fram_Top

        global data_Frame
        global keys
        global canves 
        global a_Frame
        global contro
        global keys_M
        global Frame_Tob_T
        global data_arrays
        global arrays
        global expertDepos
        global number_bisc
        arrays = []
        data_arrays = []
        contro= controller
        keys =0
        number_bisc = 102
        keys_M =0
        frame_button = ttk.Frame(self)
        frame_button.pack()
        # frame_button.columnconfigure((0,1,2,3,4,5),weight=1)
        # frame_button.rowconfigure(0,weight=1)



        Buttom_Add = ttk.Button(self,text='جديد',style="Accent.TButton",command=lambda:self.add_entry(number_bisc + 6),width=20)
        Buttom_Add.pack(side='top',fill='both',pady=5)
        # Buttom_Add.grid(row=0,column=0,padx=15,pady=15)
        
        # Buttom_destory = tk.Button(frame_button,text='تهيئة',border=0,command=self.resturt_Entry)
        #     # Buttom_destory.place(x=1600,y=25)
        # Buttom_destory.grid(row=0,column=1,padx=15)
        



        #lyatou
        fromButtom = ttk.Frame(self)
        fromButtom.pack(side='top',fill='both')
        # fromButtom.pack(side='top',expand=True,fill=tk.BOTH)

        # # الجانب الايسر الخيارات الرئيسية
        frame_Right = ttk.Frame(fromButtom)
        frame_Right.pack(side='right',pady=5,ipadx=100)

        extra_new = ttk.Button(frame_Right,text='حفظ',style='Accent.TButton',command=self.insert_data_print)
        extra_new.pack(side='top',pady=5,ipadx=30)

        extra = ttk.Button(frame_Right,image=controller.arrest,style='Accent.TButton',command=lambda:controller.Show_frame(controller.page14))
        extra.pack(side='top',pady=5,ipadx=50)
    
        view_wented = ttk.Button(frame_Right,image=controller.listarrest,style='Accent.TButton',command=self.veiw_data_Arrest)
        view_wented.pack(side='top',pady=5,ipadx=40)


        self.frame_left = ttk.Frame(fromButtom,width=1100)
        self.frame_left.pack(side='left',pady=5,padx=50)
        scrolle_y = ttk.Scrollbar(self.frame_left,orient='vertical')
        scrolle_y.pack(side=tk.RIGHT,fill=tk.Y)

        scrolle_x = ttk.Scrollbar(self.frame_left,orient='horizontal')
        scrolle_x.pack(side='bottom',fill='x')
      
        canves = tk.Canvas(self.frame_left,yscrollcommand=scrolle_y.set,xscrollcommand=scrolle_x.set,width=1080,height=650)
        canves.pack(side='right')

        scrolle_y.config(command=canves.yview)
        scrolle_x.config(command=canves.xview)
      
        canves.bind("<Configure>",lambda e: canves.configure(scrollregion=canves.bbox("all")))
        


        fram_Top = ttk.Frame(canves)
        # fram_Top.pack(side='top',anchor='center')
        canves.create_window((0,0),window=fram_Top,anchor='ne')
        expertDepos = []

        Frame_Tob_T = {}       

        data_Frame = [
                      {"charge":'التهمة'},{"ID_numberCart_entry":'البطاقة الشخصية'},{"ageWanted":'العمر'},
                      {"Gender":'نوع الجنس'},{"nameWanted_entry":'اسم المطلوب'},{'M':'م'}]

        a_Frame = ('التهمة','البطاقة الشخصية','نوع الجنس','العمر','اسم المطلوب','م')
        
        # self.Entry_automatuk(number_bisc)
        # self.lodes_open()


    def resturt_Entry(self,opriton= None):
            for ite in fram_Top.winfo_children():
                ite.destroy()
            fram_Top.update()
            canves.configure(scrollregion=canves.bbox("all"))
            canves.create_window((0,0),window=fram_Top,anchor='ne')
            canves.update()
            expertDepos = []
            if opriton is not None:
                self.Entry_automatuk(number_bisc )


    def add_entry(self,insex,num=None,ID=randomnumber()):    
        global expertDepos
        global arrays
        global number_bisc
        arrays = []
        king = 0
        # number_bisc = insex 
        #
        index = 0
        if num is not None:       
            king = num
        else:    
            king = number_bisc

        p_ID = 0
        for k in range(king ,insex):
            index += 1
            ID_new = randomnumber()
            if index <= 6:
                frame_experins = ttk.LabelFrame(fram_Top,text=a_Frame[index -1])
                frame_experins.grid(row=k // 6,column= k % 6)
            else:
                index = 1
                frame_experins = ttk.LabelFrame(fram_Top,text=a_Frame[index -1])
                frame_experins.grid(row=k // 6,column= k % 6)

            ex_data_T= ttk.Entry(frame_experins, width=24 ,justify='right',foreground="#000")
            ex_data_T.grid(row=k // 6 ,column= k  % 6 )
        
            if num is not None:
                for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                    ex_data_T.bind(key, lambda event, i=k: self.next_widget(self,event, i))
                ex_data_T.bind("<KeyRelease>", lambda event, p =k: self.insert_lisnter(self,event,p,'loding'))
                if a_Frame[index -1] == "م":
                    # print(a_Frame[index -1])
                    ex_data_T.insert(0,ID_new)
            else:
                for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                    ex_data_T.bind(key, lambda event, i=k: self.next_widget(event, i))
                ex_data_T.bind("<KeyRelease>", lambda event, p =k: self.insert_lisnter(event,p))
                if a_Frame[index -1] == "م":
                    ex_data_T.insert(0,int(ID_new) +1)
            if a_Frame[index -1] == "العمر"  or a_Frame[index -1] == 'نوع الجنس'  :
                    ex_data_T.config(width=10)
            if a_Frame[index -1] == "م" :
                    ex_data_T.config(width=6,state='disabled')
            if a_Frame[index -1] == 'البطاقة الشخصية' :
                    ex_data_T.config(width=15)
            if a_Frame[index -1] == "التهمة" :
                    ex_data_T.config(width=15)

            if responsebletUser()['Responsibilities'].replace(" ","") != 'المسؤل المباشر'.replace(" ","") :
                ex_data_T.config(state='disabled')

            data_arrays.append(ex_data_T)
            arrays.append(ex_data_T)

            if len(arrays) >= 6:
                # print('log number 6')
                expertDepos.append({"main":arrays,"ID":ID,'ID_NUM':k})
                arrays = []
            # fram_Top.update()
        # print(number_bisc)
        number_bisc = insex

        canves.update_idletasks()
        canves.configure(scrollregion=canves.bbox("all"))
        


    def insert_lisnter(self,event,x,k_type=None):
        data = {}
        print(event.keysym,x)
        if event.keysym == 'Return':
            if k_type is not None:
                self.insert_data_print(self)
            else:
                self.insert_data_print()
    


    def Entry_automatuk(self,numbers,kind=None,c=None,ID=randomnumber()):
        global Frame_Tob_T
        global expertDepos
        global number_bisc
        number_bisc  = numbers  
        index = 0
        global arrays
        # user= get_item()
        # if findUser() == True and len(user) > 0: 
        for k in  range(number_bisc):
            index += 1
            if index <= 6:
                frame_experins = ttk.LabelFrame(fram_Top,text=a_Frame[index -1])
                frame_experins.grid(row=k // 6,column= k % 6)
            else:
                index = 1
                frame_experins = ttk.LabelFrame(fram_Top,text=a_Frame[index -1])
                frame_experins.grid(row=k // 6,column= k % 6)
            ex_data_T= ttk.Entry(frame_experins, width=23 ,justify='right',foreground='#000')
            ex_data_T.grid(row=k // 6 ,column= k % 6 )
            if kind is not None:
                for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                    ex_data_T.bind(key, lambda event, i=k: self.next_widget(self,event, i))
                ex_data_T.bind("<KeyRelease>", lambda event, p =k: self.insert_lisnter(self,event,p,'loding'))
                ex_data_T.insert(0,kind[k])
                # print(kind)
            else:
                for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                    ex_data_T.bind(key, lambda event, i=k: self.next_widget(self,event, i))
                ex_data_T.bind("<KeyRelease>", lambda event, p =k: self.insert_lisnter(event,p))
                if a_Frame[index -1] == "م":
                    print(randomnumber())
                    ex_data_T.insert(0,randomnumber())
            if a_Frame[index -1] == "العمر"  or a_Frame[index -1] == 'نوع الجنس' :
                    ex_data_T.config(width=10)
            if a_Frame[index -1] == "م" :
                    ex_data_T.config(width=6,state='disabled')
            if a_Frame[index -1] == 'البطاقة الشخصية' :
                    ex_data_T.config(width=15)
            if a_Frame[index -1] == "التهمة" :
                    ex_data_T.config(width=15)
            if responsebletUser()['Responsibilities'].replace(" ","") != 'المسؤل المباشر'.replace(" ","") :
                ex_data_T.config(state='disabled')
            data_arrays.append(ex_data_T)
            arrays.append(ex_data_T)
            if len(arrays) >= 6:
                # print('log number 6')
                expertDepos.append({"main":arrays,"ID":ID,'ID_NUM':k})
                arrays = []
            else:
                # print('smile number 6')
                pass

        canves.update_idletasks()
        canves.configure(scrollregion=canves.bbox("all"))



    def next_widget(self,event,index):
        # print(event)
        r = index // 6
        c = index % 6
        if event.keysym == "Left":
            c = (c-1) % 6
        elif event.keysym == "Right":
            c = (c+1) % 6
        elif event.keysym == "Up":
            r = (r-1) % number_bisc
        elif event.keysym == "Down":
            r = (r+1) % number_bisc
        entry = data_arrays[r * 6 + c]
        # print(entry)
        entry.focus_set()  # These three lines may be what you were looking for.  Take focus
        entry.select_range(0, 'end')  # Select contents
        entry.icursor('end')  # Place cursor




    def on_right_arrow(self,event):
        event.widget.tk_focusNext().focus()

    def on_left_arrow(self,event):
        event.widget.tk_focusPrev().focus()



    def King_Function(self,Framo, event,opation=None):
        # print(event)
        if opation is not None:
            if opation == 'ageWanted':
                on_KeyPress(Framo,event)
        if event.keysym == 'End'and user['Responsibilities'].replace(" ","") == 'المسؤل المباشر'.replace(" ","") :
            self.insert_data_print(opation)



    #  insert data and print
    def insert_data_print(self,type_opration=None):
        global expertDepos
        main_sub = []

        totle = []
        
        for item in expertDepos:
            for pic in item['main']:
                # print(pic,'hiiiiiiiiiii')
                if len(pic.get()) > 0:
                    main_sub.append(pic.get())   
                        
            if len(main_sub) >= 3 :
                totle.append({'main':main_sub,"ID":item['ID'],'ID_NUM':item['ID_NUM']})
            else:
                print(main_sub)
            main_sub = []
        # print(totle,'tootles')
        
        extra_end = []
        extra_object= {}
        # print(totle)
        #   
        data_pablic = StationMonthSqly.get_pablic_wanted()
        for items in totle:
            # print(items['main'])
            extra_object['name_wanted'] = items['main'][4]
            extra_object['Gender_wanted'] = items['main'][2]
            extra_object['age_wanted'] = items['main'][3]
            extra_object['number_cart'] = items['main'][1]
            extra_object['charge'] = items['main'][0]
            extra_object["ID"] =  items['main'][5]
            extra_object["Done_kind"] = next((ite for ite in data_pablic if ite['ID'] == items['main'][5] ),None)
            extra_end.append(extra_object)
            extra_object= {}
            
        for Trov in extra_end:
        
            # if type_opration is not None:
                # print('typesssssss')
                StationMonthSqly.Delete_Winted_Day(Trov['ID'])
                StationMonthSqly.insert_pablic_wanted(Trov)
        opration = {"kindopr":"تحدث ","Timeopr":str(datetime.now().time()),'nameusefly':" تحديث بيانات المطلوبين  "}
        InsertJson(opration)
        messagebox.showinfo(title='عملية ناجحة',message='تمت العملية بنجاح')
        # print(extra_end,'extral')



# lodes _open _Page
    def lodes_open(self):
        # global Drive_data
        global Frame_Tob_T
        global user
        global keys_M
        global number_bisc
        global arrays
        global data_arrays
        global expertDepos
        expertDepos= []
        totle = []
        data_arrays=[]
        index = 0
        keys_M =0
        # user = user_verfi
        user = get_item()
        if findUser() == True and len(user) > 0:
            Drive_data = StationMonthSqly.get_Arrest_wanted("all")
            # print(Drive_data)
            for item in Drive_data:
                index +=1
                for pic in item:
                    totle.append(str(pic))
            if len(totle) > 0:
                try:
                    self.resturt_Entry(self)
                except:
                    self.resturt_Entry()
            self.Entry_automatuk(self,len(totle),kind=totle,c=totle,ID=randomnumber())
            number_bisc = len(totle) 
            self.add_entry(self, number_bisc  + 102,num=len(totle))

# ***************************************************************
    # المضبوطين
    def veiw_data_Arrest(self):
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
        search_entry_1.insert(0,'ابحث هنا')
        search_entry_1.bind("<FocusIn>", lambda e: search_entry_1.delete(0,'end'))
        search_entry_1.bind("<KeyRelease>", lambda e : search_function(e))


        Frame_view = ttk.Frame(root_view)
        Frame_view.pack(side='top',padx=5,pady=5)

        scrolle_y = ttk.Scrollbar(Frame_view)
        scrolle_y.pack(side='right',fill='y')

        # coll = ("م","نوع المضبوط",'تاريخ الضبط','كمية المضبوط','اسم المهرب','جنس المهرب',"عمر المهرب")
        coll = ("التهمة",'البطاقة الشخصية','العمر','الجنس','اسم المضبوط','تاريخ الضبط','م')
        view_tree = ttk.Treeview(Frame_view, show='tree headings',
                                  yscrollcommand=scrolle_y.set,
                                  columns=coll
                                  )
        view_tree.pack(fill='both',expand=True)
        view_tree.column('م',anchor='center')
        view_tree.column('تاريخ الضبط',anchor='center')
        view_tree.column('اسم المضبوط',width=350,anchor='center')
        view_tree.column('الجنس',anchor='center')
        view_tree.column('العمر',anchor='center')
        view_tree.column('البطاقة الشخصية',anchor='center')
        view_tree.tag_bind('row',"<Button-3>",lambda e:on_tree_view_select(e))

        scrolle_y.config(command=view_tree.yview)
        imag_oop = {}
        
        def add_inseert_viewtree(pic):
            value = list(pic)
            # print(value)
            # value.reverse()

            view_tree.insert("",tk.END, values=value,tags=('event','row'))
            view_tree.configure(selectmode='extended')
     

        def loding_view_prohibited(kind= None):
            data_cash = StationMonthSqly.get_Arrest_wanted("view")

            tree_heading = list({"التهمة",'البطاقة الشخصية','العمر','الجنس','اسم المضبوط','تاريخ الضبط','م'})
            for items in tree_heading:
                view_tree.heading(items,text=items)

            for d in view_tree.get_children():
                    view_tree.delete(d)

            if kind is not None:
                for pic in data_cash:
                    # print(pic[2],'hhhh')
                    # if re.search(pic[4].replace(" ","").capitalize(),kind.replace(" ","").capitalize()):
                    if pic[4].lower().startswith(kind):
                        # print(search_entry_1.get()) 
                
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
            cashing = StationMonthSqly.get_pablic_wanted()

            data_Arrest = next((cash for cash in cashing if int(cash['ID']) == int(row_value[6])),None)
            
            # Main.add_command(label='تعديل',accelerator='Eidte', command=lambda:self.Edit_data(data_Arrest))
                
            Main.add_command(label='عرض',accelerator='view',command=lambda:self.view_data_Arrest(data_Arrest))
        
            Main.post(event.x_root,event.y_root)





    def view_data_Arrest(self,data_Arrest):
            self.OOp = {}
            global frame_trovle

            frame_trovle = Moudel(self,data_Arrest['name_wanted'])
            
            frame_window = ttk.Frame(frame_trovle)
            frame_window.pack(side="top", fill='both', pady=10,padx=10)

            
            for index in [0,1,2,3,4,5]:
                frame_window.columnconfigure(index=index,weight=1)
                frame_window.rowconfigure(index=index,weight=1)
            

            photo_care = veiw_image(io.BytesIO(data_Arrest['url_image_wanted']),new=450)
            self.OOp['Arrest'] = photo_care






            frame_label= ttk.LabelFrame(frame_window,text='بيانات المضبوط')
            frame_label.grid(row=0,column=1,padx=10,pady=10)
            label_personality = tk.Label(frame_label, image=self.OOp['Arrest'])
            label_personality.grid(row=0,column=0,padx=10,pady=10)
        
            label_name = tk.Label(frame_label, text=f"تاريخ الضبط: {data_Arrest['Time_Arrest']}")
            label_name.grid(row=1,column=0,padx=10,pady=10)
            
            # label_ID_numberCart = tk.Label(frame_label, text=f"البطاقة الشخصية:{data_Arrest['ID_numberCart']}")
            # label_ID_numberCart.grid(row=2,column=0,padx=10,pady=10)

            label_charge = tk.Label(frame_label, text=f"التهمة : {data_Arrest['charge']}")
            label_charge.grid(row=2,column=0,padx=10,pady=10)

            label_kind_care = tk.Label(frame_label, text=f"اسم المضبوط: {data_Arrest['name_wanted']}")
            label_kind_care.grid(row=3,column=0,padx=10,pady=10)
            
            label_color_care = tk.Label(frame_label, text=f"الجنس: {data_Arrest['Gender_wanted']}")
            label_color_care.grid(row=4,column=0,padx=10,pady=10)
            
            label_numberCart = tk.Label(frame_label, text=f"العمر: {data_Arrest['age_wanted']}")
            label_numberCart.grid(row=5,column=0,padx=10,pady=10)

            label_age_trafficker = tk.Label(frame_label, text=f"البطاقة الشخصية: {data_Arrest['ID_numberCart']}")
            label_age_trafficker.grid(row=6,column=0,padx=10,pady=10)




