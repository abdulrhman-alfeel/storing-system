from tkinter import ttk ,messagebox
import tkinter as tk
from sqiltyFoun import StationMonthSqly
from convertcod.json_parse import randomnumber
from convertcod.userfind import responsebletUser
from datetime import datetime 
from convertcod.internal_storage import InsertJson




class Deposits(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        global entry_1
        global entry_2
        global entry_3
        global entry_4
        global entry_5
        global entry_6
        global entry_7
        global entry_8
        global entry_9
        global entry_10
        global entry_11
        global FRAME_TOWE
        global FRAME_THREE
        global treeview
        global button_insert
        global arrays_offic

        arrays_offic = []


        FRAME_one = ttk.Frame(self)
        FRAME_one.pack()

        layuot = ttk.LabelFrame(FRAME_one)
        layuot.pack(side='top',padx=10,pady=10,expand=True) 
        BUTTON_ONE= ttk.Button(layuot,text='ارسال',width=20,command=lambda:self.swetch_data_page(typeng='إرسال'))
        BUTTON_ONE.pack(side='right',padx=10,pady=10,expand=True) 

        BUTTON_TOWE= ttk.Button(layuot,text='استقبال',width=20,command=lambda:self.swetch_data_page(typeng='إستقبال'))
        BUTTON_TOWE.pack(side='right',padx=10,pady=10,expand=True) 
        
        # BUTTON_THREE= ttk.Button(layuot,text='قائمة المرسلات')
        # BUTTON_THREE.pack(side='top',padx=10,pady=10,expand=True) 
     
        # BUTTON_THREE= ttk.Button(layuot,text='قائمة الاستقبال')
        # BUTTON_THREE.pack(side='top',padx=10,pady=10,expand=True) 

        
        FRAME_TOWE = ttk.LabelFrame(self)
        FRAME_TOWE.pack(side='right',padx=10)


        page_one = ttk.Frame(FRAME_TOWE)
        page_one.pack(side='top')

        # for index in [0,1]:
        #     page_one.columnconfigure(index,weight=1)
        #     page_one.rowconfigure(index,weight=1)

        frame_entry_1 = ttk.LabelFrame(page_one,text='نوع الحمولة')
        frame_entry_1.grid(row=0,column=1,padx=10,pady=2)
        entry_1 = ttk.Entry(frame_entry_1,justify='center',background='#007fff')
        entry_1.grid()
        entry_1.bind("<Right>",self.one_right_move)
        entry_1.bind("<Left>",self.one_right_move)

        
        frame_entry_2 = ttk.LabelFrame(page_one,text='كمية الحمولة')
        frame_entry_2.grid(row=0,column=0,padx=10,pady=2)
        entry_2 = ttk.Entry(frame_entry_2,justify='center',background='#007fff')
        entry_2.grid()
        entry_2.bind("<Right>",self.one_right_move)
        entry_2.bind("<Left>",self.one_right_move)
      

        frame_entry_3 = ttk.LabelFrame(page_one,text='اسم المرسل')
        frame_entry_3.grid(row=1,column=1,padx=10,pady=2)
        entry_3 = ttk.Entry(frame_entry_3,justify='center',background='#007fff')
        entry_3.grid()
        entry_3.bind("<Right>",self.one_right_move)
        entry_3.bind("<Left>",self.one_right_move)


        frame_entry_4 = ttk.LabelFrame(page_one,text='البطاقة الشخصية')
        frame_entry_4.grid(row=1,column=0,padx=10,pady=2)
        entry_4 = ttk.Entry(frame_entry_4,justify='center',background='#007fff')
        entry_4.grid()
        entry_4.bind("<Right>",self.one_right_move)
        entry_4.bind("<Left>",self.one_right_move)
    

        frame_entry_5 = ttk.LabelFrame(page_one,text='رقم جوال المرسل')
        frame_entry_5.grid(row=2,column=0,pady=2,padx=10,columnspan=30)
        entry_5 = ttk.Entry(frame_entry_5,justify='center',background='#007fff',width=30)
        entry_5.pack()
        entry_5.bind("<Right>",self.one_right_move)
        entry_5.bind("<Left>",self.one_right_move)
        

        frame_entry_6 = ttk.LabelFrame(page_one,text='المستقبل')
        frame_entry_6.grid(row=3,column=1,padx=10,pady=2)
        entry_6 = ttk.Entry(frame_entry_6,justify='center',background='#007fff')
        entry_6.grid()
        entry_6.bind("<Right>",self.one_right_move)
        entry_6.bind("<Left>",self.one_right_move)


        frame_entry_7 = ttk.LabelFrame(page_one,text='رقم جوال المستقبل')
        frame_entry_7.grid(row=3,column=0,padx=10,pady=2)
        entry_7 = ttk.Entry(frame_entry_7,justify='center',background='#007fff')
        entry_7.grid()
        entry_7.bind("<Right>",self.one_right_move)
        entry_7.bind("<Left>",self.one_right_move)      
   
        frame_entry_8 = ttk.LabelFrame(page_one,text='البطاقة الشخصية للمستقبل')
        frame_entry_8.grid(row=4,column=1,padx=10,pady=2)
        entry_8 = ttk.Entry(frame_entry_8,justify='center',background='#007fff')
        entry_8.grid()
        entry_8.bind("<Right>",self.one_right_move)
        entry_8.bind("<Left>",self.one_right_move)      



        frame_entry_9 = ttk.LabelFrame(page_one,text='اسم المكتب')
        frame_entry_9.grid(row=4,column=0,padx=10,pady=2)
        entry_9 = ttk.Combobox(frame_entry_9,justify='center',background='#007fff')
        entry_9.grid()
        entry_9.bind("<Right>",self.one_right_move)
        entry_9.bind("<Left>",self.one_right_move)


        frame_entry_10 = ttk.LabelFrame(page_one,text='اسم السائق')
        frame_entry_10.grid(row=5,column=1,padx=10,pady=2)
        entry_10 = ttk.Entry(frame_entry_10,justify='center',background='#007fff')
        entry_10.grid()
        entry_10.bind("<Right>",self.one_right_move)
        entry_10.bind("<Left>",self.one_right_move)
      

        frame_entry_11 = ttk.LabelFrame(page_one,text='الوجهه')
        frame_entry_11.grid(row=5,column=0,padx=11,pady=2)
        entry_11 = ttk.Entry(frame_entry_11,justify='center',background='#007fff')
        entry_11.grid()
        entry_11.bind("<Right>",self.one_right_move)
        entry_11.bind("<Left>",self.one_right_move)


        page_tow = ttk.Frame(FRAME_TOWE)
        page_tow.pack(side='top')

        button_insert = ttk.Button(page_tow,text='اضافة',command=self.insert_data_message)
        button_insert.grid(row=0,column=0,padx=5,pady=10)
        
        button_rest = ttk.Button(page_tow,text='تهيئة',command=self.Empty_data)
        button_rest.grid(row=0,column=1,padx=5,pady=10)

        FRAME_THREE = ttk.LabelFrame(self
                                    ,width=1100,height=500
                                    )
        FRAME_THREE.pack(side='left',padx=10)
        FRAME_THREE.pack_propagate(0)
        treeScroll = ttk.Scrollbar(FRAME_THREE,orient='vertical')
        treeScroll.pack(side="right", fill="y")
        
        treeScrollButtom = ttk.Scrollbar(FRAME_THREE,orient='horizontal')
        treeScrollButtom.pack(side='bottom', fill="x")
        cols= ('الوجهه',"اسم السائق","اسم المكتب","البطاقة الشخصية للمستقبل","رقم جوال المستقبل","المستقبل",
                "رقم جوال المرسل","البطاقة الشخصية للمرسل",'اسم المرسل',"كمية الحمولة","نوع الحمولة","م")
        
        treeview = ttk.Treeview(FRAME_THREE, show="headings",
                                yscrollcommand=treeScroll.set,xscrollcommand=treeScrollButtom.set, columns=cols,
                                height=500
                                )
        treeview.column("م",anchor="center",)
        treeview.column('نوع الحمولة',anchor='center')
        treeview.column('كمية الحمولة',anchor='center')
        treeview.column("اسم المرسل",anchor="center")
        treeview.column("البطاقة الشخصية للمرسل",anchor="center")
        treeview.column("رقم جوال المرسل",anchor="center")
        treeview.column("المستقبل",anchor="center")
        treeview.column("رقم جوال المستقبل",anchor="center")
        treeview.column("البطاقة الشخصية للمستقبل",anchor="center")
        treeview.column("اسم المكتب",anchor="center")
        treeview.column("اسم السائق",anchor="center")
        treeview.column("الوجهه",anchor="center")
        treeview.tag_bind("row",'<Button-3>', lambda event: self.on_tree_view_select(event))
        treeview.pack(side="right",pady=5)
        treeScroll.config(command=treeview.yview)
        treeScrollButtom.config(command=treeview.xview)
        treeview.xview_moveto(100)


        # self.swetch_data_page()




    #  التركيز على الادخال التالي
    def one_right_move(self,event):
        event.widget.tk_focusNext().focus()

    # التركيز على الادخال السابق 
    def one_left_move(self,event):
        event.widget.tk_focusPrev().focus()

    # ارسال وتعديل البيانات
    def insert_data_message(self,V=None):

        index = 0
        for item in (entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9,entry_10,entry_11):
            if len(item.get()) > 0:
                index += 1


        if index >= 11:
            # نوع الحمولة
            deposits_type = entry_1.get()
            # كمية الحمولة
            amount_deposits = entry_2.get()
            # اسم المرسل
            name_senders = entry_3.get()
            # البطاقة الشخصية
            ID_numberCarte_sender = entry_4.get()
            # رقم جوال المرسل
            phone_sender = entry_5.get()
            # المستقبل
            name_recipient = entry_6.get()
            # رقم جوال المستقبل
            phone_recipient = entry_7.get()
            # البطاقة الشخصية للمستقبل
            ID_numberCart_recipient = entry_8.get()
            # اسم المكتب
            name_office = entry_9.get()
            # اسم السائق
            name_drive = entry_10.get()
            # الوجهة
            destination = entry_11.get()
            # 
            # نوع العملية
            kind_oprtion = FRAME_TOWE.config('text')[4]

            office = next((pic for pic in dataOffic if pic['office_name'].lower() == name_office.lower()),None)

            if office is not None:
                user = responsebletUser()
                if V is None:
                    ID = randomnumber()
                    StationMonthSqly.insert_message(ID,deposits_type,amount_deposits,name_senders,ID_numberCarte_sender,
                                                    phone_sender,name_recipient,phone_recipient,ID_numberCart_recipient,
                                                    name_office,name_drive,destination,kind_oprtion,user["userName"],office['IDsort'])
                else:
                    ID = V
                    StationMonthSqly.insert_message(ID,deposits_type,amount_deposits,name_senders,ID_numberCarte_sender,
                                                    phone_sender,name_recipient,phone_recipient,ID_numberCart_recipient,
                                                    name_office,name_drive,destination,kind_oprtion,user["userName"],office['IDsort'],kind_opr='update')
                opration = {"kindopr":"تعديل" if V is not None else 'إضافة',"Timeopr":str(datetime.now().time()),
                            'nameusefly':str(deposits_type),'nameusefly_1':str(name_senders)}
                InsertJson(opration)      
                
                self.lodens_open_deposits()
            else:
                messagebox.showwarning(title='خطاء',message="يجب تحديد اسم المكتب")


    # تبديل الصفحات بين الارسال والاستقبال
    def swetch_data_page(self,typeng='إرسال'):
        FRAME_TOWE.config(text=typeng)
        FRAME_THREE.config(text=f'عرض بيانات {typeng}')
        try:
            self.lodens_open_deposits(self)
        except :
            self.lodens_open_deposits()
        
    # لتعحديد البيانات عرضها او تعديلها 
    def on_tree_view_select(self,event):
        id_row = treeview.identify_row(event.y)
        treeview.selection_set(id_row)
        row = treeview.item(id_row)["values"]
        selectClick = tk.Menu(treeview,tearoff=0)
        print(row[11],row)
        dataMath = next((ite for ite in data_view if int(ite[0]) == int(row[11])),None)
        if dataMath is not None:
            # print(driveData,row_value[8])
            selectClick.add_command(label='تعديل',accelerator='Edite',command=lambda:self.Edit(row))
            # selectClick.add_command(label='عرض',accelerator='view',command=lambda:self.view_data_drive(dataMath))
            # buttonInsert.config(text="تعديل", command=lambda:self.insert_row(v=dataMath['iDdrive']))
        # else:
        #     print('error',row_value[2])
        #     print('error',FerquntlyeDeay)
        selectClick.post(event.x_root,event.y_root)



    # إقؤاغ البيانات التي تريد التعديل إلى داخل المدخلات
    def Edit(self,items):
        entry_1.insert(0,items[10])
        entry_2.insert(0,items[9])
        entry_3.insert(0,items[8])
        entry_4.insert(0,items[7])
        entry_5.insert(0,items[6])
        entry_6.insert(0,items[5])
        entry_7.insert(0,items[4])
        entry_8.insert(0,items[3])
        entry_9.insert(0,items[2])
        entry_10.insert(0,items[1])
        entry_11.insert(0,items[0])
        button_insert.config(command=lambda:self.insert_data_message(V=items[11]))


    #  تحميل بيانات عرض الصفحة
    def lodens_open_deposits(self):
        global data_view
        global dataOffic
        arrays_offic = []
        try:
            self.Empty_data(self)
        except:
            self.Empty_data()

        headcolmn = list({'الوجهه',"اسم السائق","اسم المكتب","البطاقة الشخصية للمستقبل","رقم جوال المستقبل","المستقبل",
                "رقم جوال المرسل","البطاقة الشخصية للمرسل",'اسم المرسل',"كمية الحمولة","نوع الحمولة","م"})
        for pic in headcolmn:
            treeview.heading(pic,text=pic)

        data_view = StationMonthSqly.get_message()
        for item in data_view:
            print(item[12].lower() == FRAME_TOWE.config('text')[4].lower())
            if item[12].lower() == FRAME_TOWE.config('text')[4].lower():
                value = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11])
                list_value = list(value)
                list_value.reverse()
                treeview.insert('',tk.END,values=list_value,tags=('event','row'))
                treeview.configure(selectmode='extended')
        
        dataOffic  = StationMonthSqly.inCominOffice_Pablic()
        for r in dataOffic:
            arrays_offic.append(r['office_name'])
        entry_9.config(values=arrays_offic)


    def Empty_data(self):
        for pic in treeview.get_children():
            treeview.delete(pic)
        treeview.update()

        for item in (entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8,entry_9,entry_10,entry_11):
            item.delete(0,'end')