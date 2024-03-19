from sqiltyFoun import StationMonthSqly
from .TimeMonth import TimeMonth
from datetime import datetime
from Print.viewpdf import switchWeek


def prohibitedPrintMonth(subPro,time):
        index = 0
        timeData = TimeMonth()
        arrayMonth = []
        BringProhibited = StationMonthSqly.get_pablic_prohibited('month',Time=time,Sorting=subPro['nameSorting'])
        html_string =  f"""
            <table style="width: 95%;">
            <thead>
            <tr>
                <th class="headerselect"  colspan="11"> تقرير عن المضبوطات اليومية في {subPro['nameSorting']} </th>
                <thead>
                    <tbody>
                        <tr>
                            <th scope="col" rowspan="2">الفرزة</th>
                            <th scope="col" rowspan="2">المستخدم</th>
                            <th scope="col" rowspan="2">عمر المهرب</th>
                            <th scope="col" rowspan="2">جنس المهرب</th>
                            <th scope="col" rowspan="2">اسم المهرب</th>
                            <th scope="col"  rowspan="2">الكمية المضبوطة</th>
                            <th scope="col"  rowspan="2">نوع المضبوط</th>
                            <th scope="col"  colspan="3" rowspan="2" >تاريخ الضبط</th>
                            <th rowspan="3">م</th>        
                            <!-- rowspan="2" هذه للدمج عمودي -->
                        </tr>
                    </tbody>
                </thead>
                    </tr>         
                    <tbody> 
        """
        for item in BringProhibited:
            # print( item[8])
            if item[8] == subPro['nameSorting']:
                index += 1
                html_string += f"""
                <tr>
                    <td>{item[8]}</td> 
                    <td>{item[7]}</td> 
                    <td>{item[6]}</td> 
                    <td>{item[5]}</td> 
                    <td>{item[4]}</td> 
                    <td>{item[3]}</td>  
                    <td >{item[2]}</td>  
                    <td colspan="3">{item[1]}</td>  
                    <td>{index}</td>  
                </tr>"""
          
        html_string += f"""
                </tbody>
                </table>
                """

        return html_string ,index