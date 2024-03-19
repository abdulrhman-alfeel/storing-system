from sqiltyFoun import StationMonthSqly
from datetime import datetime,timedelta

from Print.viewpdf import switchWeek
from .TimeMonth import TimeMonth


def trovelPrintMonth(subSo):
        index= 0
        html_string=""
        koshin = 0
        subTrov = 0
        allTravel= 0 


        def countAlls(count,times):
            count =  StationMonthSqly.Brings_Travelers(count,subSo['nameSorting'],Time=str(times))
            return count

        # select data 
        timeData = TimeMonth()
        # if countAlls('countAll',datetime.now().date())[0][0] > 0 :
            # print(maine_search)
        html_string =  f"""
                <table style="width:95%;margin:20px">
                <thead>
                <th class="headerselect"  colspan="16">تقرير شهري بعمليات نقل المسافرين في  {subSo['nameSorting']} </th>
                <tr>
                <th>عدد الكوشنات اليوم</th>
                <th>عدد العوائل اليوم</th>
                <th>اجمالي عدد المسافرين اليوم</th>
                <th>اليوم</th>
                </tr>
                <tbody>
        """
        for days in timeData:
            count = countAlls('count',days)
            countJson = countAlls('countJSON',days)
            countAll = countAlls('countAll',days)
            extract = datetime.strptime(str(days),'%Y-%m-%d')
            extractData = extract.strftime('%A')
            koshin += count[0][0] 
            subTrov += countJson[0][0] 
            allTravel += countAll[0][0] 
            if count[0][0] > 0:
                html_string += f"""
                        <tr>
                        <td style="display:flex;flex:1 0 200px">{count[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{countJson[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{countAll[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{switchWeek(extractData)}</td>
                        </tr>
                            """
        html_string += """
                <tr>
                <th>اجمالي عدد الكوشنات الشهر</th>
                <th>اجمالي عدد العوائل الشهر</th>
                <th colspan='2'>اجمالي عدد المسافرين الشهر</th>
                </tr>
        """
        html_string += f"""
                <tr>
                <td >{koshin}</td>
                <td >{subTrov}</td>
                <td colspan="2">{allTravel}</td>
                </tr>
                            """
        html_string += """
                </tbody>
                </thead>
                </table>
        """

        return html_string 
