import win32print
from tkinter  import *
import win32ui
from PIL import ImageWin

class PrintdivecJob:
  

    def startfunction(bmp,print_name):
        HORZRES = 8
        VERTRES = 10
        PHYSICALWIDTH = 110
        PHYSICALHEIGHT = 111
        PHYSICALOFFSETX = 12
        PHYSICALOFFSETY = 13
        # print(print_name)
        name_print =  win32print.GetDefaultPrinter ()
        defultname = print_name if print_name != "defult" else name_print
        hdc = win32ui.CreateDC()
        # hdc.CreatePrinterDC(defultname)
        if defultname == "XP-80C":
            hdc.CreatePrinterDC("EPSON L850 Series")
        else:
            hdc.CreatePrinterDC(defultname)
        printable_area = hdc.GetDeviceCaps(HORZRES), hdc.GetDeviceCaps(VERTRES)
        printer_size = hdc.GetDeviceCaps(PHYSICALWIDTH), hdc.GetDeviceCaps(PHYSICALHEIGHT)
        printer_margins = hdc.GetDeviceCaps(PHYSICALOFFSETX), hdc.GetDeviceCaps(PHYSICALOFFSETY)
        # for item in bmp:
        #     bmps = item
        ratios = [1.0 * printable_area[0] / bmp.size[0],1.0 * printable_area[1] / bmp.size[1]]
        scale = min (ratios) 
        hdc.StartDoc("EPSON L850 Series")
        hdc.StartPage() 
        dib = ImageWin.Dib(bmp)
        scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
        x1 = int((printer_size[0] - scaled_width) / 2)
        y1 = int((printer_size[1] - scaled_height) / 2)
        x2 = x1 + scaled_width 
        y2 = y1 + scaled_height 
        # x2 = x1 + scaled_width - printer_margins[0]
        # y2 = y1 + scaled_height - printer_margins[1]
        dib.draw(hdc.GetHandleOutput (), (x1, y1, x2, y2))
        hdc.EndPage ()
        hdc.EndDoc ()
        hdc.DeleteDC ()
        # messagebox.showwarning(title="Error",message="جاري الطباعة")
        
