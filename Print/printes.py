#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Print an Arabic string to a printer.
# Based on example from escpos-php

# Dependencies-
# - pip install wand python-bidi python-escpos
# - sudo apt-get install fonts-hosny-thabit
# - download arabic_reshaper and place in arabic_reshaper/ subfolder
import subprocess
import tempfile
from datetime import datetime
# import os
# from convertcod.processor import resource_path
from Print.viewpdf import *
from convertcod.internal_storage import get_selectprinter
import uuid
# printer= printer.File(printFile)
def printerNew(sorte,user,destination,drive_name,url_barcode,url_2=None):
    arrayData = get_selectprinter()
    printFile = "/dev/usb/lp0"
    printWidth = 550
    # month_now = datetime.now().date().strftime('%B')
    # timse = datetime.now().time()
    timseC = datetime.now().time().strftime("%H:%M:%S")
    # print(month_now)
    from escpos import printer
        # <h3>الوقت:{str(timse)[:-6].replace(".","")}</h3>
            # <link rel="stylesheet" href="table.css" />
    try:
        diername = next((item[1] for item in arrayData ),None)
        if diername is not None:
            p = printer.File(diername)
        else:
            p = printer.File(printFile)
    except :
        print('hlooo')
    try:
        html_strins ="""
    <!DOCTYPE html>
    <html lang="ar">
    <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    </head>
    <style>
        body{
            width: 50%; 
            margin: 35px;
        }
        table {
        width: 100%; 
        color: #000;
        font-family: Arial, sans-serif;
        font-size: 8px;
        text-align: left;
        padding: 5px;
        border-radius: 5px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        margin: auto;
        border: 1px solid #000;
        # border-collapse: collapse;
    
        } 
        table th {
        background-color: #fff;
        color: #000000;
        font-weight: bold;
        font-family:'Tajawal';
        font-size: 24px;
        padding: 10px;
        
        text-transform: uppercase;
        /* letter-spacing: 1px; */
        text-align: center;
        # border-top: 1px solid #000;
        border: 1px solid #000;
        # border-collapse: collapse;
        }
        table tr:nth-child(even) td {
        background-color: #000;
        }
        table tr:hover td {
        background-color: #000;
        }
        table td {
        background-color: #fff;
        padding: 10px;
        text-align: center;
        font-family:'Tajawal';
        font-size: 24px;
        border: 1px solid #000;
        font-weight: bold;
        }
        .footer{
        height: 70px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 100px;
        
        }
        .namedata{
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        height:70%;
        padding: 5px;
        }
        h4{
        font-family:'Tajawal';
        }
        h5 {
    font-family:'Tajawal';
        text-align: center;
        }
        p{
        margin: 5px;
        font-family:'Tajawal';
        }
        span{
        height: 80%;
        margin: auto;
        margin-left: 5px;
        text-align: center;
        }
    .statmintD{
        position: relative;
        width:80%
        margint:auto;
        left: 100px;
        display:flex;
        justify-content:center;
        align-items:center
    }
    h3{
        font-family:'Tajawal';
        text-align: center;
    }
    h2{
        font-family:'Tajawal';
        text-align: center;
    }
    </style>
    <body>
    """
        html_strins += f"""
        <h2>فرزة:{sorte}</h2>
        <h2>  اتجاه السفر:{destination} </h2>
        <h3>الوقت:{timseC}</h3>
        <h3>سائق السيارة:{drive_name}</h3>

            """
        html_strins += f"""
        <div style='margin:15px;text-align:center'>
            <p> المستخدم:{user}</p>
            </div>
        </div>
        </body>
        </html>
        """
        #  <p class='barcod'>{barcodNumber}</p>
        # dirs = tempfile.mkstemp()
        # url = f"{dirs[1]}.png"
        url =f"assets\\imagebarcod\\{uuid.uuid4()}.png"
        # pdfkit.from_string(str(html_string),url,css=".\\assets\\table.css",options={"enable-local-file-access": ""},verbose=True)
        # subprocess.run(['wkhtmltoimage']  + ['-', url],shell=True, input=bytes(html_strins, 'utf-8'),env=resource_path("wkhtmltopdf\\bin\\wkhtmltoimage.exe"))
        subprocess.run([resource_path("wkhtmltopdf\\bin\\wkhtmltoimage.exe")]  + ['-', url],shell=True, input=bytes(html_strins, 'utf-8'))
        p.set(align='center')
        p.image(url)


        p.image(url_barcode)
        if url_2 is not None:
            p.image(url_2)
        # p.image(tmpImage)

    
        # p.barcode(barcodNumber,"EAN13",64,3,'','')
        p.cut()
        # p.close()
    except:
         p.cut()
        


    
    
    
