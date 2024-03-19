import sqlite3
from tkinter import ttk,messagebox
import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from sqiltyFoun import StationMonthSqly
from convertcod.processor import on_KeyPress ,resource_path
import time
from convertcod.json_parse import randomnumber
from convertcod.TOPlevel import  Moudel
import json
import qrcode
import tempfile
from convertcod.internal_storage import get_selectprinter
from Print.printes import printerNew
from convertcod.internal_storage import InsertJson
from convertcod.userfind import responsebletUser
import uuid

last_updated_at = time.time()
class Trovel(ttk.Frame):
    def __init__(self, parent,controller):
        ttk.Frame.__init__(self,parent)
        global fram_Top

        global destination_entry
        global IDdrive_entry 
        global data_Frame
        global a
        global keys
        global canves 
        global a_Frame
        global contro
        global verife 
        global workplace_defrent
        global Address_defrent
        global label_text
        global Frame_Tob_T
        global expertDepos
        global data_arrays
        global count
        contro= controller
        keys =0
        count = 0
        self.num = 10
        data_arrays = []


        verife = False
        workplace_defrent = False
        Address_defrent = False
        self.Fream_Verify = {}

        frame_button = ttk.Frame(self)
        frame_button.pack()
        frame_button.columnconfigure((0,1,2,3,4,5),weight=1)
        frame_button.rowconfigure(0,weight=1)


        
        Buttom_view = tk.Button(frame_button,text='عرض البيانات',border=0,command=lambda:controller.Show_frame(controller.page4))
            # Buttom_view.place(x=1600,y=25)
        Buttom_view.grid(row=0,column=1,padx=15)
        Buttom_Add = tk.Button(frame_button,text='جديد',border=0,command=lambda:self.Entry_automatuk(self.num + 1))
            # Buttom_Add.place(x=1600,y=25)
        Buttom_Add.grid(row=0,column=2,padx=15)
        
        Buttom_destory = tk.Button(frame_button,text='تهيئة',border=0,command=self.resturt_Entry)
            # Buttom_destory.place(x=1600,y=25)
        Buttom_destory.grid(row=0,column=3,padx=15)
        



        #lyatou
        fromButtom = ttk.Frame(self,height=10)
        fromButtom.pack(side='right',anchor="n",padx=10)

        

        # الجانب الايسر الخيارات الرئيسية
        frame_Right = ttk.Frame(fromButtom)
        frame_Right.pack(side='bottom',fill='y',padx=10,pady=10)


        label_text = ttk.Label(frame_Right)
            # label_text.place(x=1600,y=25)
        label_text.pack(padx=5,pady=5)

        destination_fram = ttk.LabelFrame(frame_Right,text='وجهة السفر')
        destination_fram.pack(padx=5,pady=5)

        destination_entry = ttk.Combobox(destination_fram,validate='all')
        destination_entry.pack()
        
        
        IDdrive_fram = ttk.LabelFrame(frame_Right,text='السائق')
        IDdrive_fram.pack(padx=5,pady=5)

        IDdrive_entry = ttk.Combobox(IDdrive_fram)
        IDdrive_entry.pack()

        extra = ttk.Button(frame_Right,text='اخراج',command=self.insert_data_print)
        extra.pack(padx=5,pady=5)
    



        FramesLeft = ttk.Frame(self,width=1300)
        FramesLeft.pack(side='left',anchor="n",padx=30)
        scrolle_y = ttk.Scrollbar(FramesLeft,orient='vertical')
        scrolle_y.pack(side='right',fill='y')

        scrolle_x = ttk.Scrollbar(FramesLeft,orient='horizontal')
        scrolle_x.pack(side='bottom',fill='x')
    
        canves = tk.Canvas(FramesLeft,yscrollcommand=scrolle_y.set,xscrollcommand=scrolle_x.set,width=1300,height=650)
        # canves.pack(side='right')
        canves.pack(fill='both',expand=True)

        scrolle_y.config(command=canves.yview)
        scrolle_x.config(command=canves.xview)
    
        canves.bind("<Configure>",lambda e: canves.configure(scrollregion=canves.bbox("all")))
        
        fram_Top = ttk.LabelFrame(canves,width=1300)
        canves.create_window((0,0),window=fram_Top,
                            anchor='ne'
                            )
        

        canves.moveto(150)
        expertDepos = []

    
        self.Frame_Tob_D = []        
        Frame_Tob_T = {}       

        data_Frame = [{"Address":"مكان السكن"},{"workplace_entry":'مكان العمل'},
                      {"ID_numberCart_entry":'البطاقة الشخصية'},{"ageTrovel":'العمر'},
                      {"Gender":'نوع الجنس'},{"nameTrovel_entry":'اسم المسافر'}]
 
        a_Frame = ("مكان السكن",'مكان العمل','البطاقة الشخصية','العمر','نوع الجنس','اسم المسافر')
        
        a = ("مكان السكن",'مكان العمل','البطاقة الشخصية','العمر','نوع الجنس','اسم المودع')
   

   
        self.Entry_automatuk(self.num)


    def resturt_Entry(self):
        global Frame_Tob_T
        global expertDepos
        global fram_Top

        for ite in expertDepos:
            for pic in  ite['main']:
                pic.delete(0,'end')
        for ite in canves.winfo_children():
            ite.destroy()

        

        fram_Top = ttk.LabelFrame(canves,width=1300)
        canves.create_window((0,0),window=fram_Top, anchor='ne')
        canves.moveto(150)
        canves.update()
        
        expertDepos = []
        Frame_Tob_T= {}
        self.num  = 10
        fram_Top.update_idletasks()
        self.Entry_automatuk(self.num)


    def Entry_automatuk(self,numbers,kind=None,Eidt=None):
            global expertDepos
            global Frame_Tob_T
            self.num  = numbers  
            for k in range(numbers):
                Frame_Tob_T[k+1] = ttk.Frame(fram_Top)
                Frame_Tob_T[k+1].pack(side='top')

                ID = randomnumber()
                Buttom_Add = tk.Button(Frame_Tob_T[k+1] ,image=contro.Add_png,border=0)
                Buttom_Add.grid(column=7,padx=5,rowspan=80)
                if Eidt is not  None:
                    Buttom_Add.config(command=lambda index =ID: self.Forget_dinmacl(self,index))
                    ex_data_T = self.Statyk(self,data_Frame,a_Frame,Frame_Tob_T[k+1],'T',kind,Eidt)
                else:
                    Buttom_Add.config(command=lambda index =ID: self.Forget_dinmacl(index))
                    ex_data_T = self.Statyk(data_Frame,a_Frame,Frame_Tob_T[k+1],'T',kind)
                expertDepos.append({"main":ex_data_T,'sub':None,"ID_NUM":k+1,'ID':ID,"frames":Frame_Tob_T[k+1]})
                if kind is not None: 
                    self.Forget_dinmacl(Frame_Tob_T[k+1])
            canves.configure(scrollregion=canves.bbox("all"))
            canves.update_idletasks()

    
    def Statyk(self,data,a_Frame=None,Top=None,k='T',chake=None,kind=None):
            index = 0
            global Frames
            global keys
            global data_arrays
            global count
            Abduls = []
            keys += 1
            Frames = {}
            for p in range(len(data)):
                # print(p,index)
                for t in  data[p].keys():
                    if t != "Gender" and t != 'ageTrovel':   
                            index += 1 
                            count += 1 
                            # print(a_Frame[index-1],t)
                            fram_ = ttk.LabelFrame(Top, text=a_Frame[index-1])
                            fram_.grid(row=keys  // 6, column=p % 6,padx=5)

                            Frames["".join(t+k+str(p))]= ttk.Entry(fram_, width=20 ,justify='right')
                            # print("".join(t+k)) 
                            Frames["".join(t+k+str(p))].grid(row=keys  // 6, column=p % 6,padx=5)

                            if chake is not None:
                                Frames["".join(t+k+str(p))].insert(0,chake[p])

                    elif t == "Gender" :
                        index += 1
                        count += 1
                        fram_cunder = ttk.LabelFrame(Top, text='نوع الجنس')
                        fram_cunder.grid(row=keys // 6, column=p % 6,padx=5)
                        # fram_cunder.pack(side='right')
                        val = ['ذكر','انثى','حدث']
                        Frames["".join(t+k+str(p))] = ttk.Combobox(fram_cunder,state="readonly",values=val,width=10)
                        Frames["".join(t+k+str(p))].grid(row=keys  // 6, column=p % 6,padx=5)
                        Frames["".join(t+k+str(p))].set(val[0])
                    else:
                        index += 1
                        count += 1
                        frame_Age = ttk.LabelFrame(Top, text='العمر')
                        frame_Age.grid(row=keys // 6, column=p % 6,padx=5)

                        Frames["".join(t+k+str(p))] = ttk.Spinbox(frame_Age, from_=1, to=100,width=10 )
                        Frames["".join(t+k+str(p))].grid(row=keys // 6, column=p % 6,padx=5)

                        if chake is not None:
                            Frames["".join(t+k+str(p))].insert(0, chake[p])
                            # Frames["".join(t+k+str(p))].bind('<Return>', self.on_enter_press)

                        Frames["".join(t+k+str(p))].bind("<KeyRelease>",
                            lambda e, key = t+k+str(p),index=Frames[t+k+str(p)]:on_KeyPress(index,key))
                        
                        
                    if kind is not None:
                        for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                            Frames["".join(t+k+str(p))].bind(key, lambda event, i=p,key=count : self.next_widget(self,event, i,key))
                        Frames["".join(t+k+str(p))].bind('<Right>', lambda e :self.on_right_arrow(self,e))
                        Frames["".join(t+k+str(p))].bind('<Left>', lambda e:self.on_left_arrow(self,e))
                        Frames["".join(t+k+str(p))].bind("<KeyRelease>",lambda e ,key=t,index=Frames["".join(t+k+str(p))]:self.King_Function(self,index,e,key))
                    else:
                        for key in ("<Up>", "<Down>", "<Left>", "<Right>"):
                            Frames["".join(t+k+str(p))].bind(key, lambda event, i=p,key=count: self.next_widget(event, i, key))
                        Frames["".join(t+k+str(p))].bind('<Right>', self.on_right_arrow)
                        Frames["".join(t+k+str(p))].bind('<Left>', self.on_left_arrow)
                        Frames["".join(t+k+str(p))].bind("<KeyRelease>",lambda e ,key=t,index=Frames["".join(t+k+str(p))]:self.King_Function(index,e,key))

                    data_arrays.append(Frames["".join(t+k+str(p))])
                    Abduls.append(Frames["".join(t+k+str(p))])
                    # Frames= {}
            return Abduls


    def next_widget(self,event,index,key):
        # r = index // 6
        if event.keysym == "Up":
            r = key - 7
        elif event.keysym == "Down":
            r = key+5
        entry = data_arrays[r]
        # print(entry,len(data_arrays),key)
        entry.focus_set()  # These three lines may be what you were looking for.  Take focus
        entry.select_range(0, 'end')  # Select contents
        entry.icursor('end')  # Place cursor


    def on_right_arrow(self, event):
        event.widget.tk_focusNext().focus()
        
        
    def on_left_arrow(self, event):
        event.widget.tk_focusPrev().focus()

    # def on_Mous_arrow(self, event):
    #     event.widget.tk_focusFollowsMouse()

    # def on_focus_in(self, event):
    #     event = event.widget


#    add depositor
    def Forget_dinmacl(self,k,kinding = None):
            global expertDepos
            da = expertDepos
            p = 0
            sub = False
            # print(expertDepos)
            
            if kinding is None:
                chack = next((key for key in expertDepos if key['ID'] == k and key['sub']  == None ),None)
            else:
                chack = next((key for key in expertDepos if key['ID'] == k  ),None)

            # print(chack)
            if chack is not None:
                try:
                    ex_data_D = self.Statyk(data_Frame,a,chack['frames'],'D',chack['sub'])
                except:
                    ex_data_D = self.Statyk(self,data_Frame,a,chack['frames'],'D',chack['sub'])
                
                expertDepos= []
                for key in da:
                    p +=1
                    if key['ID'] != k :
                        expertDepos.append(key)
                    else:
                        expertDepos.append({'main':key['main'],'sub':ex_data_D,"ID_NUM":p,"ID":key['ID'],"frames":key['frames']})
                sub = False
            # else:
     

            # print('hiiiiiiiiiiiiiiiii')
            fram_Top.update()
            canves.configure(scrollregion=canves.bbox("all"))
            canves.create_window((0,0),window=fram_Top,anchor='ne')
            canves.update()

            # self.Frame_Tob_D[k].update()
            # print(da)
            # fram_Top.update()


    #  insert data and print
    def insert_data_print(self):
        main_sub = []
        sub= []
        main= []
        totle = []
        if len(IDdrive_entry.get()) > 0 and len(destination_entry.get()) > 0:
            id_process = randomnumber() if len(str(fram_Top.config('text')[4])) <= 0 else fram_Top.config('text')[4]
            for item in expertDepos:
                if item['sub'] is not None:
                    for pic in item['main']:
                        # print(pic.get())  
                        main_sub.append(pic.get()) 
                                
                    for pic_sub in item['sub']:
                        # print(pic_sub.get())
                        if len(pic_sub.get()) > 0 :
                            sub.append(pic_sub.get())
                    if len(main_sub) >= 3 :
                        totle.append({'main':main_sub,'sub':sub,"ID":item['ID']})
                
                    sub = [] 
                    main_sub = []
                if item['sub'] is None  :
                    for Nonsub in item['main']:
                        # print(Nonsub.get())
                        if len(Nonsub.get()) > 0:
                            main.append(Nonsub.get())
                    if len(main) >= 3 :
                        totle.append({'main':main,'sub':None,"ID":item['ID']})
                    main= []
            # print(totle,'tootles')
            
            extra_end = []
            extra_object= {}
            user = responsebletUser()
            for items in totle:
                extra_object['nameTrovel'] = items['main'][5]
                extra_object['Gender'] = items['main'][4]
                extra_object['ageTrovel'] = items['main'][3]
                extra_object['workplace'] = items['main'][1]
                extra_object['Address'] = items['main'][0]
                extra_object['ID_numberCart'] = items['main'][2]
                extra_object['iDdrive_DAY'] = IDdrive_entry.get()
                extra_object['destination'] = destination_entry.get()
                extra_object['user'] = user['userName']
                if items['sub'] is not None:
                    extra_object['Attachments_Json'] = json.dumps(items['sub'])
                else:
                    extra_object['Attachments_Json'] = [] 
                extra_end.append(extra_object)
                extra_object= {}
            kindeopr = 'اضافة'
            if len(str(fram_Top.config('text')[4])) > 0 :
                StationMonthSqly.Delete_Travelers_Day(id_process)
                kindeopr= 'تحديث'
            try:   
                if len(extra_end) > 0:
                    for Trov in extra_end:
                        StationMonthSqly.insert_Troval_drive_day(Trov,id_process,label_text.config('text')[4])
                        opration = {"kindopr":kindeopr,"Timeopr":str(datetime.now().time()),'nameusefly':Trov['nameTrovel'] ,'nameusefly_1':Trov['iDdrive_DAY'] }
                        InsertJson(opration) 
                    self.resturt_Entry()
                    self.convert_data_barcod(extra_end)
                    messagebox.showinfo(title='نجاح العملية',message='تمت العملية بنجاح')
                else:
                    messagebox.showerror(title='خطاء',message='يجب اكمال البيانات')
            except:
                messagebox.showwarning(title='error',message='هناك خطاء')
        else:
            messagebox.showwarning(title='خطاء', message='يجب اكمال البيانات')
        # print(extra_end,'extral')


    def convert_data_barcod(self,arrays_data):
        # drive_name = IDdrive_entry.get()
        users =responsebletUser()
        drive_name = uuid.uuid4()
        drive_nametow = uuid.uuid4()
        text_data=""""""
        text_data_3=""""""
        if len(arrays_data) < 7:
            # try:
            # print(arrays_data,'virfyyyyyyyyyyyyyy')
            for pic in arrays_data:
                text_data += self.narrativeData(pic)
            print(text_data)
            url = self.qurcoding(text_data,drive_name)
            # except:
                # print('error__borcode')
            try:
                printerNew(kind_sort['sort'],users['userName'],destination_entry.get(),IDdrive_entry.get(),url)
            except:
                pass
        else:
            try:
                for item in arrays_data[0:7]:
                    text_data += self.narrativeData(item)
                url = self.qurcoding(text_data,drive_name)
                for item_sub in arrays_data[7:len(arrays_data)]:
                    text_data_3 += self.narrativeData(item_sub)
                urlDate = self.qurcoding(text_data_3,drive_nametow)
            except:
                print('error__borcode')
            try:
                printerNew(kind_sort['sort'],users['userName'],destination_entry.get(),IDdrive_entry.get(),url,url_2=urlDate)
            except:
                pass

    def narrativeData(self,pic):
        text = f"""
                الاسم: {pic['nameTrovel']}            
                الجنس :{pic["Gender"]}   
                العمر : {pic['ageTrovel']}    
                العمل: {pic['workplace']}
                البطاقة :{str(pic['ID_numberCart'])}
        ــــــــــــــــــــــــــــــــــــــــــــــ
                            """
        return text
        
    def qurcoding(self,text,drive):
        # print(drive)
        Q = qrcode.make(text)
        # temp = tempfile.gettempdir()
        # url =f"{temp}\\{drive_name}.py"
        url2 =f"assets\\imagebarcod\\{drive}.png"
        # print(url2)
        Q.save(resource_path(url2))
        # return url2


# lodes _open _Page
    def lodes_open(self,kind):
        global kind_sort
        kind_sort = kind
        IDdrive_entry.delete(0,'end')
        destination_entry.delete(0,'end')
        label_text.config(text=kind['sort'])
        try:
            Drive = []
            Drive_data = StationMonthSqly.brings_drive_Pablic()
            for item in Drive_data:
                if item['IDsort'] == kind['sort'] :
                    Drive.append(item['namedrive'])
            
            destination_entry.config(values=kind['destination_Json'])
            IDdrive_entry.config(values=Drive)
        except:
            pass


    def King_Function(self,Frame,e,kind):
        global verife 
        global workplace_defrent
        global Address_defrent
        

        search = Frame.get()
        data_Trovels = StationMonthSqly.Brings_Travelers("checking")
        
        data_wanted = StationMonthSqly.get_sub_wanted()

        if kind == 'nameTrovel_entry':
            for pic in data_wanted:
                if pic[1].lower().replace(" ","") == search.lower().replace(" ",""):

                        self.Moudel_view_wanted(pic)

        # ****************************
            # mathing data  
        for items in data_Trovels:
            if kind == 'nameTrovel_entry':
                # if items[2].lower().startswith(search):

                    if items[2].lower().replace(" ","") == search.lower().replace(" ",""):
                        verife = True
                        self.Fream_Verify = items
                        print(search)
                    # else:
                    #     verife = False
                        # workplace_defrent = False
                        # Address_defrent = False
            print(kind,verife)
            if kind == 'workplace_entry' and  verife == True or kind == 'Address' and  verife == True:
                if kind == 'workplace_entry':
                    # if items[5].lower().replace(" ","") == search.lower().replace(" ",""):
                    if items[5].lower().startswith(search) :
                        workplace_defrent = False
                    else:
                        print(items[5])
                        workplace_defrent = True
                
                if kind == 'Address':
                    if items[6].lower().startswith(search):
                        Address_defrent = False
                    else:
                        Address_defrent = True
                else:
                    print('hlllooooo',Address_defrent,workplace_defrent)
        if  kind == 'nameTrovel_entry' :
            if workplace_defrent == True or Address_defrent == True :
                self.Moudel_view(workplace_defrent,Address_defrent,self.Fream_Verify)
        
    def Moudel_view(self,workplace_defrent,Address_defrent,items):
        main = Moudel(self,'تنبيهات')
        
        def on_close():
            global verife 
            global workplace_defrent
            global Address_defrent
            verife = False
            workplace_defrent = False
            Address_defrent = False
            main.destroy()


        def export_list(types):
            name= items[2]
            ID_numberCart= items[7]
            if workplace_defrent == True and Address_defrent == True :
                type_difference= "مكان السكن -- العمل"
                count_difference= 2
            elif workplace_defrent:
                type_difference= "العمل"
                count_difference= 1
            else:
                type_difference= "مكان السكن"
                count_difference= 1
            user= responsebletUser()
            kind_list= 'الرمادية' if types == 'gray' else 'السوداء'
            StationMonthSqly.insert_verify(name,ID_numberCart,type_difference,count_difference,kind_list,user['userName'])
            on_close()

        label_title = ttk.Button(main,text=f' هناك اختلاف في بيانات المسافر {items[2]} ')
        label_title.pack(side='top',fill='both')
        
        label_name_data = ttk.Label(main,text=" وهي كالاتي")
        label_name_data.pack(side='top',padx=10,pady=10)
        
        Freams_leble = ttk.Frame(main)
        Freams_leble.pack(side='top',fill='both')
        if workplace_defrent == True and Address_defrent == True:
            label_text_workplace = ttk.Label(Freams_leble,text='اختلاف في بيانات العمل')
            label_text_workplace.pack(side='right',padx=10,pady=10)
            label_text_Address = ttk.Label(Freams_leble,text='اختلاف في بيانات السكن')
            label_text_Address.pack(side='right',padx=10,pady=10)
        elif workplace_defrent == True :
            label_text_workplace = ttk.Label(Freams_leble,text='اختلاف في بيانات العمل')
            label_text_workplace.pack(padx=10,pady=10)
        else:
            label_text_Address = ttk.Label(Freams_leble,text='اختلاف في بيانات السكن')
            label_text_Address.pack(padx=10,pady=10)
        
        Freams_Button = ttk.Frame(main)
        Freams_Button.pack(side='bottom',fill='both',padx=40,pady=20)
        label_Button_Gray = ttk.Button(Freams_Button,text='تصدير القائمة الرمادية',command=lambda:export_list('gray'))
        label_Button_Gray.grid(row=0,column=0,padx=10)
        
        label_Button_black = ttk.Button(Freams_Button,text='تصدير القائمة السوداء',command=lambda:export_list('black'))
        label_Button_black.grid(row=0,column=1,padx=10)

        main.protocol('WM_DELETE_WINDOW', on_close)


    def Moudel_view_wanted(self,items):
        global main
        main = Moudel(self,'تنبيه')
        
        label_title = ttk.Button(main,text=' تنبيه هام : المسافر من ضمن المطلوبين امنياً ')
        label_title.pack(side='top',fill='both')

        Freams_leble = ttk.Frame(main)
        Freams_leble.pack(side='top',fill='both')
        label_text_name = ttk.Label(Freams_leble,text=f'اسم المتهم:{items[1]}')
        label_text_name.pack(side='top',padx=10,pady=10)
        label_text_charge = ttk.Label(Freams_leble,text='التهمة')
        label_text_charge.pack(side='top',padx=10,pady=10)
        label_text_charge_kind = ttk.Label(Freams_leble,text=f'{items[5]}')
        label_text_charge_kind.pack(side='top',padx=10,pady=10)

        label_Button_black = ttk.Button(main,text='تحويل لعمليات الضبط',command=lambda:self.export_wanted(items))
        label_Button_black.pack(side='bottom',fill='both')


#   ترحيل المضبوط لعملية الضبط
    def export_wanted(self,items):    
        global verife 
        global workplace_defrent
        global Address_defrent
        verife = False
        workplace_defrent = False
        Address_defrent = False
        main.destroy()

        contro.Show_frame(contro.page14,items)
        self.resturt_Entry()



    # Edite data trivales 
    def Edit_data_travels(self,idproc):
        global Frame_Tob_T
        global expertDepos
        global fram_Top
        Frame_Tob_T = {}
        expertDepos= []
        for ite in canves.winfo_children():
            ite.destroy()
        
        fram_Top = ttk.LabelFrame(canves,width=1500,text=idproc)
        canves.create_window((0,0),window=fram_Top,anchor='nw')
        canves.update()

        Edit_array= []
        # fram_Top.config(text=idproc)
        pablicprosonl = StationMonthSqly.Brings_Travelers()
        for pic in pablicprosonl:
            if int(pic[1]) == int(idproc):
                # print(pic[0])
                Edit_array.append(pic)
        # print(Edit_array,'hhhhhhhhhhhhhiiiiiiii')
        if len(Edit_array) > 0:
            numver =len(Edit_array)
            # print(numver)
            # self.Entry_automatuk(numver,Edit_array)
            for k in range(numver):
                Frame_Tob_T[k+1] = ttk.Frame(fram_Top)
                Frame_Tob_T[k+1].pack(side='top')

                # print(Edit_array[k][11])
                Buttom_Add = tk.Button(Frame_Tob_T[k+1] ,image=contro.Add_png,border=0,command=lambda index =int(Edit_array[k][1]): self.Forget_dinmacl(self,index))
                                    
                Buttom_Add.grid(column=7,padx=5,rowspan=80)
                maping = [Edit_array[k][2],Edit_array[k][3],Edit_array[k][4],Edit_array[k][7],Edit_array[k][5],Edit_array[k][6]]
                maping.reverse()
                ex_data_T = self.Statyk(self,data_Frame,a_Frame,Frame_Tob_T[k+1],'T',maping,'Edite')
            #    expertDepos.append({"main":ex_data_T,'sub':None,"ID_NUM":k+1,'ID':ID,"frames":Frame_Tob_T[k+1]})
                expertDepos.append({"main":ex_data_T,'sub':Edit_array[k][11],"ID_NUM":Edit_array[k][0],
                                    'ID':Edit_array[k][1],"frames":Frame_Tob_T[k+1]})
                
                if Edit_array[k][11] is not None: 
                    self.Forget_dinmacl(self,Edit_array[k][0],kinding=Edit_array[k][11])
            
            destination_entry.delete(0,'end')
            destination_entry.insert(0,Edit_array[k][9])
            IDdrive_entry.delete(0,'end')
            IDdrive_entry.insert(0,Edit_array[k][8])
           

            self.Entry_automatuk(self,10,kind=None,Eidt='Edite')

