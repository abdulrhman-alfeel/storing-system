from tkinter import *
from tkinter import ttk
from Print.printdivce import Printdivec
from convertcod.internal_Loginstorge import *
from datetime import datetime, timedelta
from sqiltyFoun import *
from convertcod.internal_storage import *
from convertcod.userfind import responsebletUser
class QurySerch(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.Date = []
        start_data = datetime(2023,9,1)
        end_data = datetime(2030,9,1)
        for day in range((end_data - start_data).days +1):
                databis = start_data + timedelta(days=day)
                self.Date.append(databis.date())  
        self.DateMonth = []
        yars = [f"20{key}" for key in range(23,33)]
        month = [item for item in range(1,13)]  
        for iyrs in yars :
                for keymon in month:
                    datab =f"{iyrs}-{keymon}"
                    self.DateMonth.append(datab)            
        global spent_entry
        global newimport
        global newAddcrides
        global stopCrides
        global printstatmeent
        global treeview
        global select_entry
        global select_entryD
        global kind_oprtion
        global select_entryMonth
        global name_oprtionname
        # DataMonth =  []
        # DatatPablic_drive = []
                # What is the shortcut to return the specified data space in visual studio code?
        newimport = BooleanVar()
        newAddcrides= BooleanVar()
        stopCrides = BooleanVar()
        printstatmeent = BooleanVar()
        pachSpent = ttk.Frame(self)
        pachSpent.pack(expand=True)
        pach = ttk.Frame(pachSpent,width=200)
        pach.grid(row=0,column=0,padx=10,pady=5)
        # Spnlabltext = ttk.Label(pach,text="", font=("Tajawal",13),width=100)
        # Spnlabltext.grid(row=0,column=0,padx=5,pady=5)
        # Spnlabltext.anchor('ne')
        spent_entry= ttk.Entry(pach,width=70,justify='center')
        spent_entry.grid(row=0,column=0)
        spent_entry.insert(0,'عن ماذا تبحث ')
        spent_entry.bind('<FocusIn>',lambda e:spent_entry.delete(0,'end'))
        spent_entry.bind('<KeyRelease>',self.on_search)                          
        pachOprition = ttk.LabelFrame(pachSpent,text='خيارات البحث ',padding=10)
        pachOprition.grid(row=1,column=1,padx=3,pady=10,)
        select_Textentry = ttk.LabelFrame(pachOprition,text="حدد القسم الذي تريد البحث فيه ")
        select_Textentry.grid(row=0,column=0,pady=10)
        selct= ['المسافرين','السواقين','الرسائل','المضبوطات','المرحلين','المطلوبين']
        select_entry = ttk.Combobox(select_Textentry,values=selct)
        select_entry.grid(row=0,column=0,pady=10,padx=5,
                        #   sticky='nesw'
                          )
        select_entry.set(selct[0])

        selectKIND = ttk.LabelFrame(pachOprition,text="حدد نوعية واسلوب البحث ")
        selectKIND.grid(row=1,column=0,pady=10)
        self.column = ['الاسم وتاريخ الشهر واليوم','الاسم وتاريخ الشهر',"مجمل البيانات"]
        kind_oprtion = ttk.Combobox(selectKIND,values=self.column)
        kind_oprtion.grid(row=0,column=1,pady=10,padx=10)
        kind_oprtion.current(2)
        
        self.columnname = ["المستخدم","المودع",'الفرز',"كلي"]
        name_oprtionname = ttk.Combobox(selectKIND,values=self.columnname)
        name_oprtionname.grid(row=0,column=0,pady=10,padx=10)
        name_oprtionname.current(2)
                # findData = next((item for item in  self.Date if item.key() == datetime.now()))
        frame_month = ttk.LabelFrame(pachOprition,text="تاريخ الشهر")
        frame_month.grid(row=2,column=0,pady=10,
                        #  sticky='nesw'
                         )  
        select_entryMonthButton = ttk.Button(frame_month,text='مجمل',command=lambda:self.on_search("",'الاسم وتاريخ الشهر'))
        select_entryMonthButton.grid(row=0,column=1,pady=10,padx=10,
                                    #  sticky='nesw'
                                     )

        select_entryMonth = ttk.Combobox(frame_month,values=self.DateMonth)
        select_entryMonth.grid(row=0,column=0,pady=10,padx=10,
                            #    sticky='nesw'
                               )
        select_entryMonth.current(0)
        
        frame_day = ttk.LabelFrame(pachOprition,text='اليوم')
        frame_day.grid(row=3,column=0,padx=5,pady=10,
                    #    sticky='nesw'
                       ) 
        select_entryDButton = ttk.Button(frame_day,text='مجمل',command=lambda:self.on_search("",'الاسم وتاريخ الشهر واليوم'))
        select_entryDButton.grid(row=0,column=1,pady=10,padx=10)

        select_entryD = ttk.Combobox(frame_day,values=self.Date)
        select_entryD.grid(row=0,column=0 ,pady=10,padx=10)
        select_entryD.current(0)
                
        FarmTree = ttk.Frame(pachSpent,
                             width=1000,height=500
                             )
        FarmTree.grid(row=1,column=0,padx=15,pady=15,
                      sticky='nesw'
                      )
        FarmTree.pack_propagate(0)
        buttonCrdits = ttk.Button(FarmTree,text="طباعة",style="Accent.TButton",width=30,command=self.Printsearch)
        buttonCrdits.pack(side='bottom',anchor="n",pady=10,padx=10)
        
        treeScroll= ttk.Scrollbar(FarmTree)
        treeScroll.pack(side='right',fill='y')
        treeScrollButtom= ttk.Scrollbar(FarmTree,orient='horizontal')
        treeScrollButtom.pack(side="bottom",fill="x")
        cols=('#15',"#14","#13","#12","#11","#10","#9","#8","#7",'#6','#5','#4','#3',"#2",'#1')
                
        treeview = ttk.Treeview(FarmTree,show='headings', yscrollcommand=treeScroll.set,xscrollcommand=treeScrollButtom.set,columns=cols,height=400)
        treeview.column('#1',anchor='center')
        treeview.column('#2',anchor='center')
        treeview.column('#3', anchor='center')
        treeview.column('#4', anchor='center')
        treeview.column('#5', anchor='center')
        treeview.column('#6', anchor='center')
        treeview.column('#7', anchor='center')
        treeview.column('#8', anchor='center')
        treeview.column('#9', anchor='center')
        treeview.column('#10', anchor='center')
        treeview.column('#11', anchor='center')
        treeview.column('#12', anchor='center')
        treeview.column('#13', anchor='center')
        treeview.column('#14', anchor='center')
        treeview.column('#15', anchor='center')
        # treeview.bind('<<TreeviewSelect>>',self.on_selectuser)
        treeview.pack(side="right")
        treeScroll.config(command=treeview.yview)
        treeScrollButtom.config(command=treeview.xview)



    def loadqury():
        global BringsSorting
        # المسافرين
        # السواقين
        # الرسائل
        # المضبوطات
        # المرحلين
        # المطلوبين
        # الفرز
        BringsSorting = StationMonthSqly.inComin_dataAllwitch()
        #    وظيفة البحث حسب التاريخ 

    # وظيفة الفلتر
    def on_search(self,event,dopr=None):
            global oprtion 
            global special_select
            global Month_select
            global Day_select
            global maine_search
            global seaction_select

            if dopr is not None:
                print('hhhhhh')
                spent_entry.delete(0,'end')
            
            # مراد البحث فيه 
            maine_search = spent_entry.get()  
            # تحديد القسم المراد البحث فيه
            seaction_select = select_entry.get()
            # تخصيص نوعية البحث 
            oprtion= kind_oprtion.get() if dopr is None else dopr
            # تحديد بشكل مخصص اكثر 
            special_select = name_oprtionname.get()
            # تحديد تاريخ الشهر
            Month_select = select_entryMonth.get()
            # تحديد تاريخ اليوم
            Day_select = select_entryD.get()


            headerArray= list({'#15',"#14","#13","#12","#11","#10","#9","#8","#7",'#6','#5','#4','#3',"#2",'#1'})
            headerArray.reverse()
            for col_name in headerArray:
                treeview.heading(col_name,text=col_name)
            # print(kind_oprtion.get())
            for elemant in treeview.get_children():
                treeview.delete(elemant)
            match seaction_select:
                case 'المسافرين':
                    # print(maine_search)
                    self.Travelers()
                case 'السواقين':
                    self.Drive()
                case 'الرسائل':
                    self.Messag()
                case 'المضبوطات':
                    self.Prohibited()
                case "المرحلين":
                    self.Deportees()
                case 'المطلوبين':
                    self.Wanted()
            
    
    # المسافرين
    def Travelers(self):
        BringsTravelers =  StationMonthSqly.Brings_Travelers("search")
        # print(special_select)
        numberObject={
                    "keyName":'Travelers',
                    "key1":10,   # التاريخ
                    "key2":13,   #  المستخدم
                    'key3':12,   # الفرز
                    "key4":2,    # كلي 
                    "key5":11,   # المودع
                    "keyData":BringsTravelers}
        self.data_majore(numberObject)

    # السواقين
    def Drive(self):
        DatatPablic_drive = StationMonthSqly.inComin_Pablic_drive() 
        numberObject={
                    "keyName":'Drive',
                    "key1":8,   # التاريخ
                    "key2":1,   #  المستخدم
                    'key3':7,   # الفرز
                    "key4":1,    # كلي 
                    "key5":None,   # المودع
                    "keyData":DatatPablic_drive}
        self.data_majore(numberObject)

    # الرسائل 
    def Messag(self):
        BringsMessage = StationMonthSqly.get_message()
        numberObject={
                "keyName":'message',
                "key1":15,   # التاريخ
                "key2":13,   #  المستخدم
                'key3':14,   # الفرز
                "key4":3,    # كلي 
                "key5":None,   # المودع
                "keyData":BringsMessage}
        self.data_majore(numberObject)

    #  المضبوطات
    def Prohibited(self):
        BringProhibited = StationMonthSqly.get_pablic_prohibited('search')
        numberObject={
        "keyName":'prohibited',
        "key1":1,   # التاريخ
        "key2":7,   #  المستخدم
        'key3':8,   # الفرز
        "key4":4,    # كلي 
        "key5":None,   # المودع
        "keyData":BringProhibited}
        self.data_majore(numberObject)

    # المرحلين
    def Deportees(self):
        BringsDeportees = StationMonthSqly.get_Deportees()
        numberObject={
        "keyName":'Deportees',
        "key1":6,   # التاريخ
        "key2":7,   #  المستخدم
        'key3':8,   # الفرز
        "key4":0,    # كلي 
        "key5":None,   # المودع
        "keyData":BringsDeportees}
        self.data_majore(numberObject)

    # المطلوبين 
    def Wanted(self):
        BringsWanted = StationMonthSqly.get_Arrest_wanted('allSearch')
        numberObject={
        "keyName":'wanted',
        "key1":6,   # التاريخ
        "key2":7,   #  المستخدم
        'key3':8,   # الفرز
        "key4":0,    # كلي 
        "key5":None,   # المودع
        "keyData":BringsWanted}
        self.data_majore(numberObject)
    
    

#  تخصيص عمليات البحث
    def data_majore(self,numberObject):
        if oprtion.startswith('مجمل البيانات'):
            for item in numberObject['keyData']:
                self.Switch_search(item,numberObject)
        elif oprtion.startswith('الاسم وتاريخ الشهر واليوم'):
            for item in numberObject['keyData']:
                if datetime.strptime(item[numberObject['key1']],'%Y-%m-%d').day == datetime.strptime(select_entryD.get(),'%Y-%m-%d').day:
                    self.Switch_search(item,numberObject)
        else:    
            for item in numberObject['keyData']:
                if datetime.strptime(item[numberObject['key1']],'%Y-%m-%d').month == datetime.strptime(select_entryMonth.get(),'%Y-%m').month:
                    self.Switch_search(item,numberObject)


    # فلتر تغييرات اسلوب البحث
    def Switch_search(self,item,numberObject,Transaction=None):
        match name_oprtionname.get():
            case 'المستخدم':
                if Transaction is None:
                    if item[numberObject['key2']].startswith(maine_search):
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
                else:
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
            case 'الفرز':
                if Transaction is None:
                    if item[numberObject['key3']].startswith(maine_search):
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
                else:
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
            case 'كلي':
                if Transaction is None:
                    if item[numberObject['key4']].startswith(maine_search):
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
                else:
                        self.endSearchTravelers(item,nameKey=numberObject['keyName'])
            case 'المودع':
                if item[numberObject['key5']] is not None:
                    if Transaction is  None:
                        pic = json.loads(item[11])
                        if pic[5].startswith(maine_search):
                            self.endSearchTravelers(item,json.loads(item[11]),numberObject['keyName'])
                    else:
                        self.endSearchTravelers(item,json.loads(item[11]),numberObject['keyName'])

    def endSearchTravelers(self,item,Depositor=None,nameKey=None):
        if nameKey == "message":
            listObject = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[11],item[12],item[13],item[14],item[15])
        elif nameKey == 'Travelers':    
            listObject = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8],item[9],item[10],item[12],item[13])
        else:
            listObject = (item[0],item[1],item[2],item[3],item[4],item[5],item[6],item[7],item[8])
        
        # print(listObject)
        if Depositor is None:
            treeview.insert(parent='',index=END, values=listObject )
        else:
            Deposi =treeview.insert(parent='',index=END, values=listObject )
            list_Sub = (Depositor[3],Depositor[2],Depositor[5],Depositor[0],Depositor[1],Depositor[4])
            treeview.insert(parent=Deposi,index=END, values=list_Sub )
        treeview.configure(selectmode="extended")      
    
    
    #  طباعة عملية البحث
    def Printsearch(self):
        user = responsebletUser()
        if len(user) > 0 and user is not None  :
            if user['Responsibilities'].replace(" ","") == "المسؤل المباشر".replace(" ",""):
                arrays = []
                dataTreeview = treeview.get_children()
                for key in dataTreeview:
                    data = treeview.item(key)['values']
                    arrays.append(data)
                search = select_entry.get()
                # print(arrays)
                if len(arrays) > 0:
                    url= printSearch(arrays,kind_oprtion.get(),search,user['userName'])   
                    Printdivec(self,url)       
                else:
                     messagebox.showwarning(title='خطأ', message="عملية البحث فارغه لايمكن طباعتها")  
            else: 
                messagebox.showwarning(title='خطأ', message="ليس لديك الصلاحية الكافية لطباعة العملية")         
                
