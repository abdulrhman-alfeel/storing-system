import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from convertcod.processor import on_KeyPress
from sqiltyFoun import StationMonthSqly
from convertcod.internal_storage import *
from Print.viewpdf import switchMonth
from convertcod.json_parse import randomnumber
from convertcod.userfind import responsebletUser

class SortedAdd(ttk.Frame):
    # def __init__(self,pags_labl,textnuberAllMonth,textnuberAll):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        self.pablicprosonl = []
    
        global name_sort
        global Admin_sort
        global loction_sort
        global treeview 
        global dates 
        global textStat
        global button
        global conter
        global upper_frame
        global canva


        self.Entry_Add = []

        conter = controller
        start_date = datetime.now()
        # start_date = datetime(2023, 9, 1)
        end_date = datetime(2028, 9, 30)
        dates = []
        

        for day in range((end_date - start_date).days + 1):
         datall = start_date + timedelta(days=day)
         dates.append(datall.date())
        #   load_data()
        ws = 1000
        hs= 600
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()
        x = (w/2) 
        y = (h/2) 
        treeFrame = ttk.Frame(self,width=ws,height=hs)
        treeFrame.grid(row=0,column=0, pady=15,padx=15)
        treeFrame.pack_propagate(0)
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        
        treeScroll_x = ttk.Scrollbar(treeFrame,orient='horizontal')
        treeScroll_x.pack(side='bottom', fill="x")

        cols= ("تاريخ الاضافة","موقع الفرزة","مسؤول الفرزة","اسم الفرزة","معرف الفرزة","م")
        treeview = ttk.Treeview(treeFrame,show='tree headings',yscrollcommand=treeScroll.set,xscrollcommand=treeScroll_x.set, columns=cols,height=hs,padding=(10,10))
        treeview.column("م",anchor='center')
        treeview.column("تاريخ الاضافة",anchor='center')
        treeview.column("موقع الفرزة",anchor='center')
        treeview.column("مسؤول الفرزة",anchor='center')
        treeview.column("اسم الفرزة",anchor='center')
        treeview.column("معرف الفرزة",anchor='center')
        treeview.tag_bind("row",'<Button-3>', lambda event: self.on_tree_view_select(event))
        treeview.pack()
        treeScroll.config(command=treeview.yview)
        treeScroll_x.config(command=treeview.xview)
        treeview.xview_moveto(100)




        oneFrame = ttk.LabelFrame(self,height=600)
        oneFrame.grid(row=0,column=1, pady=15,padx=25)

        # oneFrame.pack(anchor="center",fill='both')
        textStat = ttk.Label(oneFrame,text='لابد ادخال بيانات الفرز قبل البد باي عملية في النظام')
        textStat.grid_forget()
        # self.findmovement()
        fromClassify = ttk.Frame(oneFrame)
        fromClassify.grid(row=1,column=0,sticky='nsew')
    
        name_sort = ttk.Entry(fromClassify,width=22,justify='right')
        name_sort.grid(row=0, column=1,padx=5, pady=15, sticky="nsew")
        name_sort.insert(0, "اسم الفرزة")
        name_sort.bind("<FocusIn>", lambda e:  name_sort.delete('0', "end"))
        # name_sort.bind("<KeyRelease>",lambda e :on_KeyPress(name_sort,e))
        loction_sort = ttk.Entry(fromClassify,width=22,justify='right')
        loction_sort.grid(row=0, column=0,padx=5, pady=15, sticky="nsew")
        loction_sort.insert(0, "موقع الفرزة")
        loction_sort.bind("<FocusIn>", lambda e:  loction_sort.delete('0', "end"))
        # loction_sort.bind("<KeyRelease>",lambda e :on_KeyPress(loction_sort,e))
        Admin_sort = ttk.Entry(oneFrame,width=20,justify='right')
        Admin_sort.grid(row=4, column=0,padx=5, pady=15, sticky="nsew")
        Admin_sort.insert(0, "مسؤول الفرزة")
        Admin_sort.bind("<FocusIn>", lambda e:  Admin_sort.delete('0', "end"))
        # Admin_sort.bind("<KeyRelease>",lambda e :on_KeyPress(loction_sort,e))
     
        
        frameemploy = ttk.LabelFrame(oneFrame,text="وجهات السفر",height=10,width=300)
        frameemploy.grid(row=5,column=0,pady=15,padx=5)
        
        ButtonOn = tk.Button(frameemploy,image=controller.Add_png,border=0, underline=0 ,command=self.forEntry)
        ButtonOn.pack(side='top',anchor='ne',pady=5)
        # ButtonOn.grid(row=6,column=0)
        # ButtonOn.place(y=10,x=10)
        scrollbar = ttk.Scrollbar(frameemploy, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        # scrollbarhst = ttk.Scrollbar(frameemploy,orient='horizontal')
        # scrollbarhst.pack(side='bottom', fill='x')
        
        canva = tk.Canvas(frameemploy ,bg="#313131",height=150,yscrollcommand=scrollbar.set)
        canva.pack(fill='both',expand=True)

        canva.bind("<Configure>",lambda e: canva.configure(scrollregion=canva.bbox("all")))
        # scrollbarhst.config(command=canva.xview)
        scrollbar.config(command=canva.yview)
        
        upper_frame = ttk.Frame(canva)
        canva.create_window((0,0),window=upper_frame,anchor='nw')
        
        self.forEntry()
        

        FramBattom = ttk.Frame(oneFrame)
        FramBattom.grid(row=6,column=0,padx=15,pady=5,sticky='nsew')
        button = ttk.Button(FramBattom,text="اضافة", command=self.insert_row,width=15)
        button.grid(row=0, column=0,padx=15, pady=5, sticky="nsew")
        buttonrestrt = ttk.Button(FramBattom,text="تهيئة", command=self.Empty,width=15)
        buttonrestrt.grid(row=0, column=1,padx=15, pady=5, sticky="nsew")
        separator = ttk.Separator(oneFrame,orient="vertical")
        separator.grid(row=7, column=0, padx=10, pady=20, sticky="nsew")




        self.load_data()


#  Add Entry_json
    def forEntry(self,types=None):
        for k in range(3):
            frame_entry = ttk.Entry(upper_frame,justify='right',width=24)
                #    frame_entry.grid(row=rowin, column=0,padx=5, pady=10, sticky="ew")
            frame_entry.pack(padx=45,pady=15) 
            self.Entry_Add.append(frame_entry)
            canva.configure(scrollregion=canva.bbox("all"))
            canva.update()

# extry destination 
    def extry_destination(self,types):
        destination_Json = []
        Data = StationMonthSqly.inComin_dataAll()
        # brings databies
        for pic in Data:
            if int(pic['IDsort']) == int(types): 
                # print(pic['destination_Json'],'helllow')
                destination_Json= pic['destination_Json']
        return destination_Json



# Edit Entry_json
    def forEntry_Edite(self,types=None):

        self.Entry_Add = []
        
        # destory frames entry
        for item in upper_frame.winfo_children():
             item.destroy()
        
        upper_frame.update()
        destination_Json = self.extry_destination(types)
        
        # extra data bies 
        
        for k in range(len(destination_Json)):
            # print(k,"hhhhhhhhhhhhhi")
            frame_entry = ttk.Entry(upper_frame,justify='right',width=24)
            #frame_entry.grid(row=rowin, column=0,padx=5, pady=10, sticky="ew")
            # frame_entry.delete(0,'end')
            # if k <= len(destination_Json):
            frame_entry.insert(0,destination_Json[k])
            frame_entry.pack(padx=45,pady=15) 
            self.Entry_Add.append(frame_entry)
            canva.configure(scrollregion=canva.bbox("all"))
            canva.update()



    def findmovement(itemuser):
            # print(itemuser)
            if itemuser["kindMovment"].replace(" ","") == 'بداية تشغيل'.replace(" ",""):
                # print('بدء running')
                textStat.grid(row=0,column=0,padx=5,pady=5)

    def on_tree_view_select(self,event):
        id_row = treeview.identify_row(event.y)
        treeview.selection_set(id_row)
        row_value = treeview.item(id_row)["values"]
        # print(row_value)
        destination_Json = self.extry_destination(row_value[4])
        # print(destination_Json)
        Men = tk.Menu(treeview,tearoff=0)
        user= responsebletUser()
        if user['Responsibilities'].lower().replace(" ","") == 'المسؤل المباشر'.replace(" ",""):
            Men.add_command(label='تعديل',command=lambda:self.Eite(row_value))
        Men.add_command(label='كوشن',command=lambda:conter.Show_frame(conter.page10,{"sort":row_value[3],'IDsort':row_value[4],"destination_Json":destination_Json}))
        Men.post(event.x_root,event.y_root)
        
    def Eite(self,row_value):
        self.Empty()
        name_sort.delete(0,'end')
        name_sort.insert(0,row_value[3])
        loction_sort.delete(0,'end')
        loction_sort.insert(0,row_value[1])
        Admin_sort.delete(0,'end')
        Admin_sort.insert(0,row_value[2])
        self.forEntry_Edite(types=row_value[4])
        button.config(command=lambda:self.insert_row(type=row_value[4]),text='تعديل')
        
    def insert_row(self, type=None):      
            # global vierfiyDone
            # destination_Json
        # try:
            array= []
            loction = loction_sort.get()
            namesort = name_sort.get()
            AdminSort = Admin_sort.get()
            for pic in self.Entry_Add:
                if len(pic.get()) > 0:
                    array.append(pic.get())
            # print(array)
            destination_Json = json_stringify(array)
            IDsort = randomnumber()
            if len(loction) > 0  and loction != "موقع الفرزة" and len(namesort) > 0 and namesort != "اسم الفرزة" and len(AdminSort) > 0 and AdminSort !="مسؤول الفرزة" :
                if type is None:
                    StationMonthSqly.insert_Pablic_station(namesort,loction,AdminSort,IDsort,destination_Json,'insert')
                else: 
                    StationMonthSqly.insert_Pablic_station(namesort,loction,AdminSort,type,destination_Json)
                opration = {"kindopr":"تعديل" if type is not None else 'إضافة',"Timeopr":str(datetime.now().time()),'nameusefly':str(namesort),'nameusefly_1':str(AdminSort)}
                InsertJson(opration)
                
                Items = treeview.get_children()
                # Delete the item
                stat = StationMonthSqly.inComin_dataAll()
                if len(stat) > 0:       
                    # datatest = stat[len(stat) -1]
                    for item in Items:
                        treeview.delete(item)
                    treeview.update()
                    self.load_data()
                    chaking= get_virfe()
                    if chaking['kindMovment'] == 'بداية تشغيل' :
                            conter.Show_frame(conter.page4)
                    textStat.grid_forget()
                    try:
                        kindopr = "اضافة فرزة" if type is None else 'تعديل'
                        opration = {"kindopr":kindopr,"Timeopr":str(datetime.now().time()),'nameusefly':namesort ,'nameusefly_1':None }
                        InsertJson(opration) 
                    except:
                         pass
                    self.Empty()
                    # objectSum = {}     
                    # set_conv_imge(quantity)
            else:
                messagebox.showwarning(title="Erorr", message="يجب اكمال ادخال البيانات")
        # except:
        #     pass


    def Empty(self):
            loction_sort.delete(0,'end')
            loction_sort.insert(0,"موقع الفرزة")
            name_sort.delete(0,'end')
            name_sort.insert(0,"اسم الفرزة")
            Admin_sort.delete(0,'end')
            Admin_sort.insert(0,"مسؤول الفرزة")
            textStat.grid_forget()
            for item in upper_frame.winfo_children():
                item.destroy()
            self.Entry_Add = []
            self.forEntry()
            upper_frame.update()
            button.config(command=self.insert_row,text='إضافة')


    def load_data(self):
            global objectsall
            self.pablicprosonl = StationMonthSqly.inComin_dataAllwitch()
            lisvalues = list({"تاريخ الاضافة","موقع الفرزة","مسؤول الفرزة","اسم الفرزة","معرف الفرزة","م"})
        # #     print(list_values)
            index = 0
            items = treeview.get_children()
            for pic in items :
                treeview.delete(pic)
            for col_name in lisvalues:
                    treeview.heading(col_name, text=col_name)
            for value_tuple in self.pablicprosonl:
                    values = list(value_tuple)
                    # values.reverse()
                    index+= 1 
                    objectsall = (values[4],values[2],values[3], values[1],values[5],index )
                    treeview.insert('',tk.END,values=objectsall,tags=("event",'row'))
                    # if len(value_tuple[7])> 0 and value_tuple[7] != "null":    
                    #     for k in json_parse(value_tuple[7]):
                    #         # print(k)
                    #         v = list(k.values())
                    #         treeview.insert(parent=valu,index=tk.END,values=v)


    def verify_trovles(self):
         textStat.grid(row=0,column=0,padx=15,pady=15)