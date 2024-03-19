from sqiltyFoun import StationMonthSqly
from datetime import datetime,timedelta

from Print.viewpdf import switchMonth
from .TimeYars import TimeYars
def trovelPrintYars(subSo):
        index= 0
        html_string=""
        koshin = 0
        subTrov = 0
        allTravel= 0 


        def countAlls(count,times):
            count =  StationMonthSqly.Brings_Travelers(count,subSo['nameSorting'],Time=times)
            return count

        # select data 
        timeData = TimeYars()
        # months=  datetime.now().month
        # years=  datetime.now().year
        # if months == 2:
        #     namberday = 28 
        # elif months != 1 and months != 3 and months != 5 and months != 7 and months != 8 and months != 10 and months != 12:
        #     namberday = 30 
        # else:
        #     namberday = 31 
        # start_data = datetime(years,months,1)
        # end_data = datetime(years,months,namberday)   
        # for day in range((end_data - start_data).days +1):
        #             timeArray = start_data + timedelta(days=day)
        #             timeData.append(timeArray.date()) 

        # if countAlls('countAll',datetime.now().date())[0][0] > 0 :
            # print(maine_search)
        html_string =  f"""
                <table style="width:95%;margin:20px">
                <thead>
                <th class="headerselect"  colspan="16">تقرير شهري بعمليات نقل المسافرين في  {subSo['nameSorting']} </th>
                <tr>
                <th>عدد الكوشنات الشهر</th>
                <th>عدد العوائل الشهر</th>
                <th>اجمالي عدد المسافرين الشهر</th>
                <th>الشهر</th>
                </tr>
                <tbody>
        """
        for days in timeData:
            print(days,datetime.now().date())
            count = countAlls('countMonth',days)
            countJson = countAlls('countJSONMonth',days)
            countAll = countAlls('countAllMonth',days)
            extract = datetime.strptime(str(days),'%Y-%m')
            extractData = extract.strftime('%B')
            print(extractData)
            koshin += count[0][0] 
            subTrov += countJson[0][0] 
            allTravel += countAll[0][0] 
            if count[0][0] > 0:
                html_string += f"""
                        <tr>
                        <td style="display:flex;flex:1 0 200px">{count[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{countJson[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{countAll[0][0]}</td>
                        <td style="display:flex;flex:1 0 200px">{switchMonth(extractData)}</td>
                        </tr>
                            """
        html_string += """
                <tr>
                <th>اجمالي عدد الكوشنات السنة</th>
                <th>اجمالي عدد العوائل السنة</th>
                <th colspan='2'>اجمالي عدد المسافرين السنة</th>
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
