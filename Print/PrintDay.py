import pdfkit
import tempfile
from datetime import datetime
from convertcod.processor import resource_path
from sqiltyFoun import StationMonthSqly
from .prenterDay.TrovelPrint import trovelPrint 
from .prenterDay.MessagePrint import  messgePrint
from .prenterMonth.MessagePrintMonth import  messgePrintMonth
from .prenterDay.ProhibitedPrint import  prohibitedPrint
from .prenterDay.DeporteesPrint import  deporteesPrint
from .prenterDay.WantedPrint import  wantedprint
from .prenterMonth.TrovelPrintMonth import trovelPrintMonth
from .prenterYars.TrovelPrintYars import trovelPrintYars
import os
from .printdivce import Printdivec
from .prenterYars.MessagePrintYars import messgePrintYars
from .prenterMonth.ProhibitedPrintMonth import prohibitedPrintMonth
from .prenterMonth.DeporteesPrint import deporteesPrintMonth
from .prenterYars.DeporteesPrintYars import deporteesPrintYars
from .prenterMonth.WantedPrint import wantedPrintmonth
from .prenterYars.WantedPrintYars import wantedPrintYars
from .prenterYars.ProhibitedPrintYars import prohibitedPrintYars


#  <link rel="stylesheet" href="table.css" />
def printDay(search,user,freems,kind='view',TIme=None):
    index=0
    verify = True
    html_string = """ <!DOCTYPE html>
                        <html lang="ar">
                        <head>
                        <meta charset="UTF-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                        <title>Document</title>
                        </head>
                        <body>
                        """ 
    sort = StationMonthSqly.inComin_dataAll()
    match search:
        case 'المسافرين' | "Trovels":
            for subSo in sort:
                if TIme == 'day':
                    if  trovelPrint(subSo) == False:
                        verify=False 
                    else:
                        html_string += trovelPrint(subSo)
                elif TIme == 'month':
                    html_string += trovelPrintMonth(subSo)
                else:
                    html_string += trovelPrintYars(subSo)
        case 'الرسائل' | "Message":
            for subMss in sort:
                if TIme == 'day':
                    html_string += messgePrint(subMss)
                elif TIme == 'month':
                    html_string += messgePrintMonth(subMss)
                else:
                    html_string += messgePrintYars(subMss)
        case 'المضبوطات' | 'Prohibited':
            for subpro in sort:
                if TIme == 'day':
                    html , index = prohibitedPrint(subpro,time=datetime.now().date())   
                    if index > 0: 
                        html_string += html
                elif TIme == 'month':
                    month= str(datetime.now().month)  
                    if len(month) == 1 :
                        month = f"0{datetime.now().month}"
                    print("".join(str(datetime.now().year)+"-"+month))
                    html , index = prohibitedPrintMonth(subpro,time="".join(str(datetime.now().year) +"-"+ month))   
                    if index > 0: 
                        html_string += html
                else:
                    html , index = prohibitedPrintYars(subpro,time=datetime.now().year)   
                    if index > 0: 
                        html_string += html
        case "المرحلين" | "Deportees":
            for subdepor in sort:     
                if TIme == 'day':   
                    html_string += deporteesPrint(subdepor)
                elif TIme == 'month':
                    html_string += deporteesPrintMonth(subdepor)
                else:
                    html_string += deporteesPrintYars(subdepor)
        case 'المطلوبين' | "wanted":
            for subwant in sort:     
                if TIme == 'day':   
                    html_string += wantedprint(subwant)
                elif TIme == 'month':
                    html_string += wantedPrintmonth(subwant)
                else:
                    html_string += wantedPrintYars(subwant)
    html_string += f"""
        <div style='margin:15px;text-align:center'>
            <p> المستخدم:{user}</p>
        </div>
        </div>
        </body>
        </html>
        """
    # filepdf =tempfile.mkstemp()
    # url = f"{filepdf[1]}.pdf"
    try:
        if verify == True:
            url = resource_path("assets\\printerPdf\\semple.pdf")
            config=  pdfkit.configuration(wkhtmltopdf=resource_path("wkhtmltopdf\\bin\\wkhtmltopdf.exe"))
            # pdfkit.from_string(html_string,url, css=resource_path('assets\\table.css'),options={"enable-local-file-access": True},verbose=True,configuration=config)
            pdfkit.from_string(html_string,url, css=resource_path('assets\\table.css'),options={"enable-local-file-access": ""},verbose=False,configuration=config)
            if kind =='view':
                os.system(url)
                # register(url,filepdf[0],htmls=html_string)
            else:
                Printdivec(freems,urlFil=url)  
    except:
        pass
    