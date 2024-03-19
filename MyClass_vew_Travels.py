import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime, timedelta
from sqiltyFoun import StationMonthSqly
# from escpos.printer import Serial
from convertcod.processor import on_KeyPress
from convertcod.userfind import *
from convertcod.internal_storage import *
from convertcod.insertSelectprinter import SelectPrinter

# import asyncio
# from convertcod.ImageWriter import ImageWriter
# from wand.image import Image as wImage
# from wand.drawing import Drawing as wDrawing
# from wand.color import Color as wColor
# from PIL import Image,ImageDraw,ImageFont
# from snapshottest import TestCase, snapshot

    

class MyClass_vew_Travels(ttk.Frame):
    def __init__(self,parent,controller):
        ttk.Frame.__init__(self,parent)
        self.combo_list = ["Subscribed", "Not Subscribed", "Other"]
        start_date = datetime.now()
        # start_date = datetime(2023, 9, 1)
        global controll

        controll = controller


        end_date = datetime(2028, 9, 30)
        self.dates = []
        for day in range((end_date - start_date).days + 1):
         datall = start_date + timedelta(days=day)
         self.dates.append(datall.date())
        
        
        self.data = dict()
        self.Statimnt()
        
        # create radom
        

    def Statimnt(self):
        global treeview
        # global treeFrame


        treeFrame = ttk.Frame(self,width=1400,height=700)
        # treeFrame.grid(row=0,column=0, pady=5,padx=5)
        treeFrame.pack(side='left',anchor='n',expand=True)
        treeFrame.pack_propagate(0)
        
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        
        treeScroll_x = ttk.Scrollbar(treeFrame,orient='horizontal')
        treeScroll_x.pack(side="bottom", fill="x",anchor='e')
# nameTrovel,Gender,ageTrovel,workplace,Address,ID_numberCart,iDdrive_DAY,destination,Time,ِAttachments_Json
        cols= ("التاريخ","جهة السفر","السواق","البطاقة الشخصية","السكن","العمل", "العمر","الجنس","اسم المسافر","المعرف",'م')
        treeview = ttk.Treeview(treeFrame, show='tree headings',yscrollcommand=treeScroll.set,xscrollcommand=treeScroll_x.set, columns=cols,height=800)
        treeview.column("م",anchor="center")
        treeview.column("المعرف",anchor="center")
        treeview.column("اسم المسافر",width=300,anchor="center")
        treeview.column("الجنس",anchor="center")
        treeview.column("العمر",anchor="center")
        treeview.column("العمل",anchor="center")
        treeview.column("السكن",anchor="center")
        treeview.column("البطاقة الشخصية",anchor="center")
        treeview.column("السواق",anchor="center")
        treeview.column("جهة السفر",anchor="center")
        treeview.column("التاريخ",anchor="center")
        treeview.tag_bind("row", "<Button-3>", lambda event: self.founction(event))
        treeview.pack()
        treeScroll.config(command=treeview.yview)
        treeScroll_x.config(command=treeview.xview)
        treeview.xview_moveto(100)
        #   function  Edite 
    def keypresslisn(self,num,event):
        on_KeyPress(num,event)
        if event.keysym == 'Return':
               self.awiating()

    
    def upTreeview(self):
          get_it = treeview.get_children()
          for item in get_it:
            treeview.delete(item)
          treeview.update()
          self.load_data()           


    def founction(self,event):
        id_row = treeview.identify_row(event.y)
        treeview.selection_set(id_row)
        row_value = treeview.item(id_row)['values']
        for item in treeview.get_children(id_row):
            rows = treeview.item(item)["values"]
            print(rows)
        controll.Show_frame(controll.page10,row_value[9])
        print(row_value[9])

    
    
    
    def load_data(self):
        global pablicprosonl
        # if creditsKind2 == 'down':
        get_it = treeview.get_children()
        for item in get_it:
                treeview.delete(item)
        treeview.update()
        pablicprosonl =StationMonthSqly.Brings_Travelers()
        lisvalues = list({"التاريخ","جهة السفر","السواق","البطاقة الشخصية","السكن","العمل", "العمر","الجنس","اسم المسافر","المعرف",'م'})
        lisvalues.reverse()
        for col_name in lisvalues:
                treeview.heading(col_name, text=col_name)
        for pi in pablicprosonl:
            # values = (pi['ID'],pi['nameTrovel'],pi['Gender'],pi['ageTrovel'],pi['workplace'],pi['Address'],pi['ID_numberCart'],pi["iDdrive_DAY"],pi['destination'],pi['Time'])
            values = (pi[10],pi[9],pi[8],pi[7],pi[6],pi[5],pi[4],pi[3],pi[2],pi[1],pi[0])
            # values.reverse()
            prant = treeview.insert(parent='', index=tk.END, values=values,tags=('event', 'row'))
            print(pi,'hhhhhhhhhhhhhhhhhhhh')
            if pi[11] is not None:
                pic = json_parse(pi[11])
                print(pic)
                values_sub = ('',"","",pic[2],pic[0],pic[1],pic[3],pic[4],pic[5],"","")
                treeview.insert(parent=prant, index=tk.END, values=values_sub,tags=('event', 'row')) 
            treeview.configure(selectmode="extended")    


