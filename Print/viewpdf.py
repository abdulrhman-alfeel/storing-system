
import random
from tkinter import *
from tkinter import ttk
# from tkPDFViewer import tkPDFViewer as pdf
from tkinter  import filedialog ,messagebox
import os
import pdfkit
# import fitz
from Print.printdivce import Printdivec
from convertcod.processor import resource_path
img_object_li = []
def register(filename,id,htmls):
                screen1 = Toplevel()
                screen1.title("تقارير")
                screen1.geometry("600x700")
                # screen1
                screen1.overrideredirect(True)
                
                def Files():
                    num1 = "0123456789"
                    num2 = "0123456789"
                    number = num1 + num2
                    index = "".join(random.sample(number,3))
                    filename = filedialog.askdirectory(initialdir=os.getcwd(),title="select pdf file",mustexist=True)
                    # print(filename)
                    if len(filename) > 0:
                        url = f"{filename}/station{index}.pdf"
                        pdfkit.from_string(htmls,output_path= url,css=resource_path("assets\\table.css"),options={"enable-local-file-access": ""})
                        messagebox.showinfo(title="already",message='تم الحفظ بنجاح')
           
                CONVtenr = ttk.Frame(screen1)
                CONVtenr.pack(side="top",fill='both',expand=True)
                navber = ttk.Frame(CONVtenr)
                navber.pack(side="top",fill='none',expand=True,anchor='ne')
                button = ttk.Button(navber, text="اغلاق", command=lambda:screen1.destroy() )
                button.grid(row=0, column=8, padx=5, pady=15, sticky="nsew")
                button = ttk.Button(navber, text="طباعة",command=lambda:   Printdivec(screen1,urlFil=filename)  )
                button.grid(row=0, column=7, padx=5, pady=15, sticky="nsew")
            
                button = ttk.Button(navber, text="حفظ باسم",command=Files)
                button.grid(row=0, column=6, padx=5, pady=15, sticky="nsew")
 
                frame = ttk.Frame(CONVtenr)
                frame.pack(pady=(0,0))
                # frame.config(width=650)
                scroll_y = ttk.Scrollbar(frame,orient="vertical")
                scroll_x = ttk.Scrollbar(frame,orient="horizontal")
                scroll_x.pack(fill="x",side="bottom")
                scroll_y.pack(fill="y",side="right")
                text = Text(frame, yscrollcommand=scroll_y.set,xscrollcommand= scroll_x.set,width= 900,height= 600)
                text.pack(side="left",fill='both',expand=True)
                scroll_x.config(command=text.xview)
                scroll_y.config(command=text.yview)
                
                # def add_img():
                #     doc = fitz.open(open(filename,"rb"))
                #     matrix = fitz.Matrix(1500.0, 1500.0)
                #     for page in doc:
                #         img = page.get_pixmap()
                #         pix1 = fitz.Pixmap(img,0) if img.alpha else img
                #         img = pix1.tobytes("ppm")
                #         timg = PhotoImage(data= img)
                #         img_object_li.append({"id":id, "im":timg})
                #     for i in img_object_li:
                #         if i['id'] == id :
                #             text.image_create(END,image=i['im'])
                #             text.insert(END,"\n\n")
                # screen1.after(200,add_img)
              

def switchMonth(name_month):
    # print(name_month)
    if name_month.replace(" ","") == "January".replace(" ",""):
        return "يناير"
    elif name_month.replace(" ","") ==  "February".replace(" ",""):
        return "فبراير"
    elif name_month.replace(" ","") == "March".replace(" ",""):
        return "مارس"
    elif name_month.replace(" ","") == "April".replace(" ",""):
        return 'ابريل'
    elif name_month.replace(" ","") ==  "May".replace(" ",""):
        return 'مايو'
    elif name_month.replace(" ","") == "June".replace(" ",""):
        return "يونيو"
    elif name_month.replace(" ","") == "July".replace(" ",""):
        return "يوليو" 
    elif name_month.replace(" ","") == "August".replace(" ",""):
        return 'اغسطس'
    elif name_month.replace(" ","") ==   "September".replace(" ",""):
        return 'سبتمر'
    elif name_month.replace(" ","") == "October".replace(" ",""):
        return 'اكتوبر' 
    elif name_month.replace(" ","") == "November".replace(" ",""):
        return 'نوفمبر'
    else:
        return 'ديسمبر' 
        # "December" 
def switchWeek(name_days):
    if name_days.replace(" ","") == " Saturday".replace(" ",""):
        return 'السبت'
    elif name_days.replace(" ","") == "Sunday".replace(" ",""):
        return 'الاحد'
    elif name_days.replace(" ","") == "Monday".replace(" ",""):
        return 'الاثنين'
    elif name_days.replace(" ","") ==  "Tuesday".replace(" ",""):
        return 'الثلاثاء'
    elif name_days.replace(" ","") =="Wednesday".replace(" ",""):
        return 'الاربعاء'
    elif name_days.replace(" ","") == "Thursday".replace(" ",""):
        return 'الخميس'
    else:
        return 'الجمعة'
        # "Friday"
  