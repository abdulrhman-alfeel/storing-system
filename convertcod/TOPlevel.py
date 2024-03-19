from tkinter import *
from tkinter import ttk
from .view_image import veiw_image
from .processor import resource_path
def Moudel(master,titel):
    level = Toplevel(master)
    level.title(titel)
    level.minsize(level.winfo_width(),level.winfo_height())
    x_continer = int((level.winfo_screenwidth()/2) - (level.winfo_width()/2))
    y_continer = int((level.winfo_screenheight()/2) - (level.winfo_height()/2))
    level.geometry('+{}+{}'.format(x_continer,y_continer -20))
    
    return level





def select_custom(masters,title,select,file,camer):
    min = Moudel(masters,title)
    global selected
    selected= ''
    label_titel = ttk.Label(min , text='اختر الطريقة الذي تريد اخذ الصوره بها ',font=('Tajawal',25))
    label_titel.pack(side='top',pady=30,padx=50)
    label_select = ttk.Label(min , text='إذا اخترت التصوير عبر كاميرة الجهاز ',font=('Tajawal',13))
    label_select.pack(side='top',pady=10,padx=50)
    label_select_2 = ttk.Label(min , text='لاخذ الصورة واغلاق الاطار (q) انقر ',font=('Tajawal',13))
    label_select_2.pack(side='top',pady=10,padx=50)
    framtitle = Frame(min,pady=20,width=600)
    framtitle.pack(anchor='center',expand=True)
    label_select1 = ttk.Button(framtitle,image=file,command=lambda :select("files"),width=250)
    label_select1.grid(row=0,column=0,padx=30,pady=20)
    label_select2 = ttk.Button(framtitle,image=camer,command=lambda :select('camera'),width=250)
    label_select2.grid(row=0,column=2,padx=30,pady=20)
    return min
