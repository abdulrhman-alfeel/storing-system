from sqiltyFoun import StationMonthSqly
from datetime import datetime



def trovelPrint(subSo):
        index= 0
        html_string=""
        BringsTravelers =  StationMonthSqly.Brings_Travelers("search",Time=str(datetime.now().date()))
        count =  StationMonthSqly.Brings_Travelers("count",subSo['nameSorting'],Time=str(datetime.now().date()))
        countJson = StationMonthSqly.Brings_Travelers('countJSON',subSo['nameSorting'],Time=str(datetime.now().date()))
        countAll = StationMonthSqly.Brings_Travelers('countAll',subSo['nameSorting'],Time=str(datetime.now().date()))
        if countAll[0][0] > 0 :
            # print(maine_search)
            html_string =  f"""
                    <table style="width:95%;margin:20px">
                    <thead>
                    <th class="headerselect"  colspan="16">تقرير يومي بعمليات نقل المسافرين في  {subSo['nameSorting']} </th>
                    <tr>
                    <th>عدد الكوشنات اليوم</th>
                    <th>عدد العوائل اليوم</th>
                    <th>اجمالي عدد المسافرين اليوم</th>
                    </tr>
                    <tbody>
                    <tr>
                    <td style="display:flex;flex:1 0 200px">{count[0][0]}</td>
                    <td style="display:flex;flex:1 0 200px">{countJson[0][0]}</td>
                    <td style="display:flex;flex:1 0 200px">{countAll[0][0]}</td>
                    </tr>
                    </tbody>
                    </thead>
                    </table>
                    <table style="width: 95%;">
                    <thead>
                    <tr>
                        <thead>
                            <tbody>
                                <tr>
                                    <th scope="col" rowspan="2">المستخدم</th>
                                    <th scope="col" rowspan="2">الفرزة</th>
                                    <th scope="col" rowspan="2">التاريخ</th>
                                    <th scope="col" rowspan="2">جهة السفر</th>
                                    <th scope="col" rowspan="2">السواق</th>
                                    <th scope="col" rowspan="2">البطاقة الشخصية</th>
                                    <th scope="col" rowspan="2">السكن</th>
                                    <th scope="col" rowspan="2">العمل</th>
                                    <th scope="col" rowspan="2">العمر</th>
                                    <th scope="col" rowspan="2">الجنس</th>
                                    <th scope="col" rowspan="2">اسم المسافر</th>
                                    <th scope="col" colspan="3" rowspan="2" >المعرف</th>
                                    <th rowspan="2">م</th>        
                                    <!-- rowspan="2" هذه للدمج عمودي -->
                                </tr>
                            </tbody>
                        </thead>
                                </tr>         
                                <tbody> 
                    """
            for item in BringsTravelers:
                if subSo['nameSorting'] == item[12]:
                    index += 1
                    html_string += f"""
                        <tr>
                            <td>{item[13]}</td> 
                            <td>{item[12]}</td> 
                            <td>{item[10]}</td> 
                            <td>{item[9]}</td> 
                            <td>{item[8]}</td> 
                            <td>{item[7]}</td> 
                            <td>{item[6]}</td> 
                            <td>{item[5]}</td> 
                            <td>{item[4]}</td> 
                            <td>{item[3]}</td>  
                            <td colspan="3">{item[2]}</td>  
                            <td>{item[1]}</td>  
                            <td>{index}</td>  
                        </tr>"""
            html_string += f"""
            </tbody>
            </table>
            """
    
            return html_string 
        else:
             return False
