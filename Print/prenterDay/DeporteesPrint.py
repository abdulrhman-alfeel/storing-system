from sqiltyFoun import StationMonthSqly


def deporteesPrint(subDep):
        BringsDeportees = StationMonthSqly.get_Deportees("printer")
        index = 0
        html_string =  f"""
            <table style="width: 95%;">
            <thead>
            <tr>
                <th class="headerselect"  colspan="13"> تقرير عن المرحلين من  {subDep['nameSorting']} </th>
                <thead>
                    <tbody>
                        <tr>
                            <th scope="col" rowspan="2">الفرزة</th>
                            <th scope="col" rowspan="2">المستخدم</th>
                            <th scope="col" rowspan="2">التاريخ</th>
                            <th scope="col" rowspan="2">وجهة الترحيل</th>
                            <th scope="col" rowspan="2">السواق المرسل معه/th>
                            <th scope="col" rowspan="2">رقم بطاقة المرحل</th>
                            <th scope="col"  rowspan="2">عمر المرحل</th>
                            <th scope="col"  rowspan="2">جنس المرحل</th>
                            <th scope="col"  colspan="3" rowspan="2" >اسم المرحل</th>
                            <th rowspan="3">م</th>        
                            <!-- rowspan="2" هذه للدمج عمودي -->
                        </tr>
                    </tbody>
                </thead>
                    </tr>         
                    <tbody> 
        """
        for item in BringsDeportees:
            if item[8] == subDep['nameSorting']:
                index += 1
                html_string += f"""
        <tr>
            <td>{item[8]}</td> 
            <td>{item[7]}</td> 
            <td>{item[6]}</td> 
            <td>{item[5]}</td> 
            <td>{item[4]}</td> 
            <td>{item[3]}</td> 
            <td>{item[2]}</td>  
            <td >{item[1]}</td>  
            <td colspan="3">{item[0]}</td>  
            <td>{index}</td>  
        </tr>"""
            else:
                html_string += f"""
        <tr>
            <td>-</td> 
            <td>-</td> 
            <td>-</td> 
            <td>-</td> 
            <td>-</td> 
            <td>-</td> 
            <td>-</td>  
            <td >-</td>  
            <td colspan="3">-</td>  
            <td>{index}</td>  
        </tr>"""
        html_string += f"""
                </tbody>
                </table>
                """

        return html_string