from sqiltyFoun import StationMonthSqly

def wantedprint(subWan):
    BringsWanted = StationMonthSqly.get_Arrest_wanted('allSearch')
    index = 0
    html_string =  f"""
    <table style="width: 95%;">
    <thead>
    <tr>
        <th class="headerselect"  colspan="12">تقرير عن المضبوطين من المطلوبين امنياً خلال اليوم في  {subWan['nameSorting']} </th>
        <thead>
            <tbody>
                <tr>
                    <th scope="col" rowspan="2">الفرزة</th>
                    <th scope="col" rowspan="2">المستخدم</th>
                    <th scope="col" rowspan="2"> تاريخ الضبط</th>
                    <th scope="col" rowspan="2">حالة الضبط</th>
                    <th scope="col" rowspan="2">التهمة/th>
                    <th scope="col" rowspan="2">رقم بطاقة المطلوب</th>
                    <th scope="col"  rowspan="2">عمر المطلوب</th>
                    <th scope="col"  rowspan="2">جنس المطلوب</th>
                    <th scope="col"  colspan="3" rowspan="2" >اسم المطلوب</th>
                    <th rowspan="3">م</th>        
                    <!-- rowspan="2" هذه للدمج عمودي -->
                </tr>
            </tbody>
        </thead>
            </tr>         
            <tbody> 
"""
    for item in BringsWanted:
        if item[8] == subWan['nameSorting']:
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