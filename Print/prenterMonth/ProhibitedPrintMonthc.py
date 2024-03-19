from sqiltyFoun import StationMonthSqly
from .TimeMonth import TimeMonth
from datetime import datetime
from Print.viewpdf import switchWeek


def prohibitedPrintMonth(subPro):
        index = 0
        timeData = TimeMonth()
        arrayMonth = []
        listProhib = StationMonthSqly.get_list_prohibited()
        def SqlitSearch(kind,name,time,sorting):
            BringProhibited = StationMonthSqly.get_pablic_prohibited(kind,name,time,sorting)
            return BringProhibited

        def Oprtion(kind):
            for pic in timeData:
                count = SqlitSearch('count',kind,pic,subPro['nameSorting'])
                dayDate = datetime.strptime(str(pic),'%Y-%m-%d').strftime('%A')
                print(count,pic)
                if count is not None:
                    objectMonth = {'count':count[0][0],'day':switchWeek(dayDate),'oprtion':kind,"sort":subPro['nameSorting'],'DateTime':pic}
                    arrayMonth.append(objectMonth)

        html_string =  f"""
            <table style="width: 95%;">
            <thead>
            <tr>
            <th class="headerselect"  colspan="9"> تقرير عن المضبوطات الشهرية في {subPro['nameSorting']} </th>
            <thead>
            <tbody>
            <tr>
        """
        for li in listProhib:
            # print(li)
            Oprtion(li[2])
            html_string +=f"""
                        <th scope="col" rowspan="2">{li[2]}</th>
                        <!-- rowspan="2" هذه للدمج عمودي -->
                        """
        html_string +="""
                <th scope="col" rowspan="2">اليوم</th>
                </tr>
                </tbody>
                </thead>
                </tr>         
                <tbody> 
        """

        def vierfy(kind,days):
            datVerfy = next((ite for ite in arrayMonth if ite['oprtion'] == kind and ite['day'] == days),None)
            if datVerfy is not None:
                return datVerfy['count']
        print(arrayMonth)
        html_string +="""<tr>"""
        for pic in listProhib:
            for item in arrayMonth:
                index += 1
           
                if item['oprtion'] == pic[2]:
                    html_string += f"""
                        <td>{item['count']}</td> 
                       """
                else:
                    html_string += f"""
                        <td>0</td> 
                       """
                html_string +=f"""
                         <td>{item['day']}</td> 
                        </tr>
                        """
        html_string += f"""
                </tbody>
                </table>
                """
        return html_string ,index