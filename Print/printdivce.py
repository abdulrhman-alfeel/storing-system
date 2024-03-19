import win32print
from tkinter  import *
from tkinter import ttk
from tkinter import messagebox
import os 
from Print.printdivceJob import PrintdivecJob
from pdf2image import convert_from_path
from convertcod.processor import resource_path

class Printdivec:
    def __init__(self,master,urlFil):
        self.selecters = []
        global boxselecter
        pinters = win32print.EnumPrinters(win32print.PORT_STATUS_TYPE_INFO,None,1)
        for item in pinters:
            if item[2] != 'Microsoft Print to PDF':
                 self.selecters.append(item[2])
        self.level = Toplevel(master)
        self.level.title('اختر طابعة')
        self.level.geometry('500x150')
        # frameall = ttk.Frame(level,width=500)
        # frameall.pack(fill="both",expand=True)
        labelText = ttk.Label(self.level,text='حدد نوع الطابعة المتوفرة', foreground='#ffffff',font=("29LT Baseet",15))
        labelText.pack(expand=True,side='top',anchor='n',fill='none',padx=10,pady=10)
        boxselecter = ttk.Combobox(self.level,values=self.selecters)
        boxselecter.pack()
        boxselecter.set(self.selecters[0])
        funcjop = ttk.Button(self.level,text='طباعة',command=lambda:self.startfunction(urlFil)) 
        funcjop.pack(side='bottom',fill='both',anchor='se')

    def startfunction(self,urlFil):
        kindprint = boxselecter.get()
        virfe = os.path.exists(urlFil)
        if virfe == True:
            self.level.destroy()
    # def close(self):
            images = convert_from_path(urlFil,fmt="png",poppler_path=resource_path("Library\\bin"))
            # print(images)
            for imag in images: 
                PrintdivecJob.startfunction(imag,kindprint)
        else:
            messagebox.showwarning(title="Error",message="الملف غير موجود")
        
          