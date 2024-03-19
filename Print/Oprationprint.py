import tempfile
from tkinter  import *
import os
from Print.printdivceJob import PrintdivecJob
import pdfkit
from pdf2image import convert_from_path
from datetime import datetime
from Print.viewpdf import *
from convertcod.processor import resource_path
class Oprationprint:
    def startfunction(namberCash,nameusfly,namerecefd,cashAmount,classyfe,user,month):
        image1 = resource_path('assets\\cantry2.jpg')
        image2 = resource_path('assets\\textlogo2.png')
        submonth = datetime.strptime(str(datetime.now().date()), "%Y-%m-%d")
        # month = switchMonth(submonth.strftime("%B"))
        day = switchWeek(submonth.strftime('%A'))
        resced = namerecefd if namerecefd  != 'نفسه'  else nameusfly
        #  <link href="fatorh.css" rel="stylesheet"> 
        #   <link href="https://fonts.googleapis.com/css2?family=Libre+Barcode+128+Text&display=swap" rel="stylesheet">
        htmlstr =f"""
        <!DOCTYPE html>
        <html lang="ar">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>فاتورة المستفيد</title>
        </head>
        """
        htmlstr +=f"""
        <body>
        <img  src={image1} class="identification">
        <div class="rightcontiner">
        <img  src={image2} class="headerRight">
        <hr class="hrstyle" />
        </div>
        <div class="leftcontiner">
        <p>{namberCash}:الرقم</p>
        <p>من حمولة شهر:{month}</p>
        <p>{datetime.now().date()}:التاريخ</p>
        </div>
        <h1 class="title">الجهة المستفيدة</h1>
        <h1 class="title">{nameusfly}</h1>
        <div class="statmintD" style="border:1px solid #747474;"> 
            <P> المستلم:{resced}</P>
            <P class="cash"> المصروف:{cashAmount}لتر {classyfe}</P>
        <div class="days"> 
        <P >اليوم:{day}</P>
        <P class="cash">الوقت:{datetime.now().time().strftime('%H:%M:%S')}</P>
             </div>
        </div>
        <div class="statmintD"> 
            <P>...........................:التوقيع</P>
             <p style="text-align:left"> المستخدم:{user}</p>
        </div>
        </body>
        </html>
        """
   
        cssurl = os.path.abspath("assets\\fatorh.css")
        dir = tempfile.mkstemp()
        url = f"{dir[1]}.pdf"
        # print(url,namberCash,nameusfly,namerecefd,cashAmount,dir)
        pdfkit.from_string(str(htmlstr),output_path=url,css=cssurl ,options={"enable-local-file-access": None} , verbose=True)
        # subprocess.run(['wkhtmltopdf', "-", url], input=bytes(htmlstr,"UTF-8"))

        images = convert_from_path(url,fmt="png")
        # print(images)
        precentage_dicide = 0 
        for imag in images:
            precentage_dicide += 1 
            percentage_view = (float(precentage_dicide)/float(len(images))*float(100))
            # progress['value'] = percentage_view
            PrintdivecJob.startfunction(imag,'defult')
        return percentage_view

     
          