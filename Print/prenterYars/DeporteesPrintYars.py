from sqiltyFoun import StationMonthSqly
from .TimeYars import TimeYars
from datetime import datetime 
import time
from Print.viewpdf import switchMonth

def deporteesPrintYars(subDepor):
        index = 0
        arrayMonth = []
        timeData = TimeYars()
        # BringsMessage = StationMonthSqly.get_message()
        html_string = """
  <table style="width: 95%;">
                    <thead>
"""

        # create date month
        def Oprtion():
            for pic in timeData:
                # count = StationMonthSqly.get_message("month",pic,subDepor['nameSorting'])
                count = StationMonthSqly.get_Deportees("Yars",pic,subDepor['nameSorting'])
                dayDate = datetime.strptime(str(pic),'%Y-%m').strftime('%B')
                objectMonth = {'count':count[0][0],'month':switchMonth(dayDate),"sort":subDepor['nameSorting'],'DateTime':pic}
                arrayMonth.append(objectMonth)
            index = 0
        
            html = f"""
                <tr>
                    <th class="headerselect"  colspan="17">تقرير  سنوي عن المرحلين من  {subDepor['nameSorting']} </th>
                """
            html +=  f""" 
                            <thead>
                                <tbody>
                                
                                    <tr>
                                        <th scope="col" rowspan="2">التاريخ</th>
                                        <th scope="col" rowspan="2">الفرزة</th>
                                        <th scope="col" rowspan="2">عدد المرحلين</th>
                                        <th scope="col" colspan='3' rowspan="2">الشهر</th>
                                        <th rowspan='3'>م</th>        
                                        <!-- rowspan="2" هذه للدمج عمودي -->
                                    </tr>
                                </tbody>
                            </thead>
                                    </tr>         
                                    <tbody> 
                        """
            for item in arrayMonth:
                if item['sort'] == subDepor['nameSorting']: 
                        index += 1
                        html += f"""
                    <tr>
                        <td>{item["DateTime"]}</td>  
                        <td>{item["sort"]}</td>  
                        <td >{item['count']}</td>  
                        <td colspan="3">{item['month']}</td>  
                        <td>{index}</td>  
                    </tr>"""
            return html            
        html_string += Oprtion()
        html_string += f"""
                </tbody>
                </table>
                """

        return html_string 