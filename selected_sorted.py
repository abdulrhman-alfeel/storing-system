from tkinter import ttk
import tkinter as tk
from sqiltyFoun import StationMonthSqly

class Selected_sorted(ttk.Frame):
   def __init__(self, parent,controller):
        ttk.Frame.__init__(self,parent)
        global IDdrive_entry
        global controll
        global arrays

        controll = controller
        arrays = []

        label_text = ttk.Label(self,text='اختر اسم الفرزة لدخول لصفحة الكوشن',font=('Tajawal',25))
        label_text.pack(padx=10,pady=10)
        
        frame_Right = ttk.LabelFrame(self,padding=(20,10))
        frame_Right.pack(padx=10,pady=30)
        
        IDdrive_entry = ttk.Combobox(frame_Right,width=40,justify='center')
        IDdrive_entry.pack(padx=5,pady=5)

        extra = ttk.Button(frame_Right,text='دخول',width=20,command=self.insert_coshen)
        extra.pack(padx=5,pady=25)
   

   def insert_coshen(self):
      
      if len(IDdrive_entry.get()) > 0:
        # brings databies
         row = next((pic for pic in Data if pic['nameSorting'].lower() == IDdrive_entry.get().lower()),None)
   
         controll.Show_frame(controll.page10,{'sort':IDdrive_entry.get(),'IDsort':row['IDsort'],"destination_Json":row['destination_Json']})


   
   def loding_sorted():
      global Data
      global arrays
      try:  
         arrays = []
         
         Data = StationMonthSqly.inComin_dataAll()
         for item in Data:
            arrays.append(item['nameSorting'])
         IDdrive_entry.config(values=arrays)
      except:
         pass

