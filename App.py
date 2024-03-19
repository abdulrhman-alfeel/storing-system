from tkinter import *
from tkinter import ttk
import sqlite3
from PIL import Image,ImageTk
from convertcod.internal_Loginstorge import get_loginAll,get_item
from LoginPage import LoginPage
from convertcod.processor import resource_path
from convertcod.backup import culctiveActivate ,SerchActivate , SerchActivateLMIT
from datetime import datetime ,timedelta
from convertcod.internal_storage import *
from convertcod.internal_Loginstorge import *
from convertcod.view_image import veiw_image

# from multiprocessing import freeze_support
import pyglet
# C:\Program Files (x86)\الفرزة

class App(Tk):
    def __init__(self,*args,**kwargs):
        Tk.__init__(self,*args,**kwargs)
        self.title('نظام الفرزة')
        pyglet.font.add_file(resource_path("fount/Tajawal-Medium.ttf"))
        # pyglet.font.add_file(os.path.join("fount","Tajawal-Medium.ttf"))
        # img = Image.open(resource_path("assets\\uzarh.png"))
        # img.save(resource_path("assets\\uzarh2.png"))


        self.im = Image.open(resource_path("assets\\add.ico"))
        width , height = self.im.size
        aspect_ratio = width / height 
        new_width = 20
        new_height = int(new_width / aspect_ratio)
        
        resized_img = self.im.resize((new_width,new_height))

        self.bgbuttom=ImageTk.PhotoImage(file=resource_path('assets\\uzarh.png'))
        # for image in resized_img:
        # print(image[image])
        self.add=ImageTk.PhotoImage(resized_img)
        self.revshe = veiw_image(resource_path("assets\\synchronization-arrows-couple.PNG"),50)
        self.arrest = veiw_image(resource_path("assets\\arrest.PNG"),50)
        self.listarrest = veiw_image(resource_path("assets\\listarrest.PNG"),80)
        self.sorter = veiw_image(resource_path("assets\\sorter.PNG"),80)
        self.driver = veiw_image(resource_path("assets\\driver.PNG"),80)
        self.Travelers = veiw_image(resource_path("assets\\Travelers.PNG"),80)
        self.offices = veiw_image(resource_path("assets\\offices.PNG"),80)
        self.forbidden = veiw_image(resource_path("assets\\forbidden.PNG"),80)
        self.wanted = veiw_image(resource_path("assets\\wanted.PNG"),80)
        self.deportees = veiw_image(resource_path("assets\\deportees.PNG"),80)
        self.sentpyloud = veiw_image(resource_path("assets\\sentpyloud.PNG"),80)
        self.man = veiw_image(resource_path("assets\\playstore.PNG"),380)
        self.list_file = veiw_image(resource_path('assets\\list-min.png'),100)
        self.camera = veiw_image(resource_path('assets\\camera.png'),100)
        self.printer = veiw_image(resource_path('assets\\printer.png'),80)
        self.search = veiw_image(resource_path('assets\\search.png'),80)






        container = ttk.Frame(self,padding=(5,5))
        container.pack(side="top",fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.style = ttk.Style(self)
        self.tk.call('source',resource_path("azure.tcl"))
        self.tk.call("set_theme", "light")
        self.option_add("*tearOff", False)
        self.option_add("*Font",("Tajawal-Medium",15,"bold"))
        self.style.configure("Treeview", rowheight=40)
        Vierfy = 0
        self.thremn = 0

        self.aciton= StringVar(value='new')
        self.creat_databise()
        from StartPage import StartPage
        # from experimental import Experimental
        self.page1 = StartPage
        self.page2 = LoginPage
        # self.page3 = Experimental
        self.frames={}

        if get_loginAll() is not None or len(get_loginAll) > 0:
            self.usercount = get_loginAll()  
        else:
            self.usercount = []

        self.DataLoginNew=  get_item()

        for F in (self.page1,self.page2):
            frame= F(container,self)
            self.frames[F] = frame
            # frame.grid(row=0,column=0,sticky="nsew")
            frame.grid(row=0,column=0,pady=30,sticky="nsew")

        # if Vierfy > 0:
        #  countentr = self.page3
            
            
        if len(self.usercount) > 0 :
            countentr = self.page2 
        else:
            countentr = self.page1

        self.Show_frame(countentr)
    def Show_frame(self,context):
        # if context == self.page1:
        #     self.page1.chingepages(self=self.page1)
        frame = self.frames[context]
        frame.tkraise()
# Source: "D:\ppp\aldy\python\Sorting\output\azure.tcl"; DestDir: "{app}"; Flags: ignoreversion


#    انشاء جداول النظام
    def creat_databise(self):
            conn = sqlite3.connect(resource_path("assets\\backup\\dataSorte.db"))
            # conn = sqlite3.connect(resource_path(".\\assets\\backup\\data.db"))
            table_create_Station = '''CREATE TABLE IF NOT EXISTS sorting 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,nameSorting TEXT NOT NULL UNIQUE ,
            sortingSit TEXT NOT NULL ,Admin_sorting TEXT NULL,TimeInsert DATE NULL DEFAULT CURRENT_DATE, 
            IDsort INTEGER NULL UNIQUE,Arrayjson JSON NULL , destination_Json JSON NULL)
            '''    

            table_create_qureypablic = '''CREATE TABLE IF NOT EXISTS drive_pablic 
            (iDdrive INTEGER NOT NULL UNIQUE , namedrive TEXT NOT NULL ,ID_numberCart INTEGER NOT NULL,kind_care TEXT NULL,
            Color_care TEXT NULL,number_Care INTEGER NULL UNIQUE, Guarantee TEXT NULL,
            IDsort INTEGER NOT NULL,Time DATE NULL DEFAULT CURRENT_DATE,stating TEXT NULL DEFAULT "جاري",
            Arrayjson JSON NULL,url_Image_care BLOB NULL ,url_Image_drive BLOB NULL, url_image_license BLOB NULL)
            '''
            
            table_create_Office  = '''CREATE TABLE IF NOT EXISTS office 
            (iDoffice INTEGER NOT NULL UNIQUE , office_name TEXT NOT NULL , owner_name TEXT NULL,ID_numberCart INTEGER NOT NULL,
            employ_name JSON NULL,Licensig TEXT NULL ,stating TEXT NULL DEFAULT "جاري",IDsort INTEGER NOT NULL,Time DATE NULL DEFAULT CURRENT_DATE ,Arrayjson JSON NULL,
            url_image_licens BLOB NULL)
            '''

            table_create_TRIVERS_DAY = '''CREATE TABLE IF NOT EXISTS Travelers_DAY 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,process_ID INTEGER NULL,nameTrovel TEXT NOT NULL ,Gender TEXT NULL
            ,ageTrovel INTEGER NULL,workplace TEXT NOT NULL,
            Address TEXT NULL,ID_numberCart INTEGER NOT NULL,iDdrive_DAY TEXT NULL ,
            destination TEXT NULL,ِAttachments_Json JSON NULL,Time DATE NULL DEFAULT CURRENT_DATE,user TEXT NULL,sorting TEXT NULL)
            '''
                        # FOREIGN KEY(iDdrive_DAY) REFERENCES drive_pablic (iDdrive) ON DELETE RESTRICT ON UPDATE RESTRICT)


            table_create_THEGOODES_or_payload_DAY = '''CREATE TABLE IF NOT EXISTS Loads_today 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,type_payload TEXT NULL ,amount_payload INTEGER NULL,Sender TEXT NULL,
            ID_numberCart_SINDER INTEGER  NULL,sender_phone INTEGER NULL,Recipient TEXT NULL,phone_recipient INTEGER NULL,
            ID_numberCart_recipient INTEGER  NULL,
            name_office TEXT NULL, drive_name TEXT NULL,destination TEXT NULL,kind_oprtion TEXT NULL,user TEXT NULL,sorting TEXT NULL,Time DATE NULL DEFAULT CURRENT_DATE)
            '''

            table_create_Deportees_DAY = '''CREATE TABLE IF NOT EXISTS Deportees_DAY 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,namedeportees TEXT NOT NULL ,Gender TEXT NULL,agedeportees TEXT NULL
            ,ID_numberCart TEXT NULL,Imageurl BLOB NULL,iDdrive_DAY TEXT NOT NULL ,destination TEXT NULL,
            Time DATE NULL DEFAULT CURRENT_DATE,user TEXT NULL,sorting TEXT NULL,Fingerprint TEXT NULL)
            '''

            #   FOREIGN KEY(iDdrive_DAY) REFERENCES drive_pablic (iDdrive) ON DELETE RESTRICT ON UPDATE RESTRICT)
            table_create_Forbidding_things = '''CREATE TABLE IF NOT EXISTS Prohibited_items_list
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            name_Prohibited TEXT NOT NULL UNIQUE,amount TEXT NOT NULL ,Done TEXT NULL,ArrayCaught JSON NULL)
            '''
            table_create_cash_prohibited = '''CREATE TABLE IF NOT EXISTS Prohibited_items_cash
            (ID INTEGER PRIMARY KEY AUTOINCREMENT, TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            name_Prohibited TEXT NOT NULL,amount TEXT NOT NULL ,trafficker TEXT NULL ,Gender_trafficker TEXT NULL,
            AGE_trafficker TEXT NULL,url_prohibited BLOB NULL,url_trafficker BLOB NULL ,ArrayCaught JSON NULL,user TEXT NULL,sorting TEXT NULL)
            '''
            # arrayCaught == nameforbidding and namedrive and iddrive  and trafficker and namerecipient and time_day_caught  
    
            table_create_wanted = '''CREATE TABLE IF NOT EXISTS wanted 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,              
            TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            name_wanted TEXT NOT NULL UNIQUE, ID_numberCart TEXT NULL ,age_wanted TEXT NULL
            ,Gender_wanted TEXT NULL,charge TEXT NULL ,Done TEXT NULL DEFAULT "هارب",Time_Arrest DATE NULL ,url_image_wanted BLOB NULL
            ,ArrayCaught JSON NULL,user TEXT NULL,sorting TEXT NULL,fingerprint TEXT NULL)
            '''
            
            table_create_Sort_LIST_difference = '''CREATE TABLE IF NOT EXISTS list_vierfy 
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NULL , TimeInsert DATE NULL DEFAULT CURRENT_DATE,
            ID_numberCart INTEGER NOT NULL , type_difference TEXT NOT NULL ,count_difference INTEGER NOT NULL,
            kind_list TEXT NULL,user TEXT NULL,Arraydifference JSON NULL)
            '''

            try:
                conn.execute(table_create_Station)
                conn.execute(table_create_qureypablic)
                conn.execute(table_create_TRIVERS_DAY)
                conn.execute(table_create_Office)
                conn.execute(table_create_THEGOODES_or_payload_DAY)
                conn.execute(table_create_Forbidding_things)
                conn.execute(table_create_cash_prohibited)
                conn.execute(table_create_wanted)
                conn.execute(table_create_Sort_LIST_difference)
                conn.execute(table_create_Deportees_DAY)
                # private python or python specificWWW
                #private insert named credits pablic 
            except sqlite3.IntegrityError:
                print("couldn't add Python twice")
            conn.commit() 
            conn.close()
            conecticion = sqlite3.connect(resource_path("assets\\backup\\data_storng.db"))
            # conecticion = sqlite3.connect(resource_path(".\\assets\\backup\\data_storng.db"))
            try:
                tabelNavigetion = '''CREATE TABLE IF NOT EXISTS movement (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                userName TEXT NOT NULL,datamovement  DATE NULL DEFAULT CURRENT_DATE,
                kindMovement TEXT NULL , stayuser TEXT NOT NULL,dataExet DATE NULL, arrayMovement JSON NULL,Time DATE NULL DEFAULT CURRENT_DATE)'''
                tabelLogin = '''CREATE TABLE IF NOT EXISTS logtion (ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                userName TEXT NOT NULL UNIQUE, passwordUSER  TEXT NOT NULL,
                Responsibilities TEXT NOT NULL, jsonResponsibilities JSON NULL,
                datatim DATE NULL DEFAULT CURRENT_DATE) '''
                tabelLoginActivite = '''CREATE TABLE IF NOT EXISTS logtionActivite 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, userName TEXT NOT NULL , passwordUSER  TEXT NOT NULL,
                Responsibilities TEXT NOT NULL,activity TEXT NOT NULL,
                jsonResponsibilities JSON NULL ,datatim DATE NULL DEFAULT CURRENT_DATE) '''
                tableselecter = '''CREATE TABLE IF NOT EXISTS selectAdddir 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, dircarteAdd TEXT NOT NULL)'''
                table = '''CREATE TABLE IF NOT EXISTS selectPrinter 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, dircarteUsb TEXT NOT NULL)'''
                tableData = '''CREATE TABLE IF NOT EXISTS selectData 
                (ID INTEGER PRIMARY KEY AUTOINCREMENT, dirDatabase TEXT NOT NULL)'''
              
                conecticion.execute(tabelNavigetion)
                conecticion.execute(tabelLogin)
                conecticion.execute(tabelLoginActivite)
                conecticion.execute(tableselecter)
                conecticion.execute(table)
                conecticion.execute(tableData)
            except sqlite3.IntegrityError:
                print("couldn't add python twice")
            conecticion.close()




# لاستماع عند اغلاق النظام
def on_close():
    print('useer closed')
    try:
        empty = {"userName":""}
        getuser = get_item() if len(get_item()) > 0 else empty

        set_itemx(getuser['userName'],'اغلاق') 
        set_loguot()
    except:
        pass
    app.quit()
if __name__ == "__main__":
    app = App()
    # app.update()
    # app.attributes("-fullscreen",True)

    # app.overrideredirect(True)
    # app.state("zoomed")
    app.minsize(app.winfo_width(),app.winfo_height())
    x_continer = int((app.winfo_screenwidth() /2) - (app.winfo_width()/2))
    y_continer = int((app.winfo_screenheight()/2) - (app.winfo_height()/2))
    app.geometry("+{}+{}".format(x_continer,y_continer -20))
    
    app.eval('tk::PlaceWindow . center')
    app.update()
    app.protocol('WM_DELETE_WINDOW', on_close)
    app.mainloop()