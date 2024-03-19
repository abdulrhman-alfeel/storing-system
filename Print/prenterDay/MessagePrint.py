from sqiltyFoun import StationMonthSqly


def messgePrint(subMes):
        index = 0
        BringsMessage = StationMonthSqly.get_message()
        index = 0
        html_string =  f"""
                    <table style="width: 95%;">
                    <thead>
                    <tr>
                    <th class="headerselect"  colspan="17">تقرير عن الرسائل والودائع اليومية المرسلة في  {subMes['nameSorting']} </th>
                        <thead>
                            <tbody>
                                <tr>
                                    <th scope="col" rowspan="2">التاريخ</th>
                                    <th scope="col" rowspan="2">الفرزة</th>
                                    <th scope="col" rowspan="2">المستخدم</th>
                                    <th scope="col" rowspan="2">الوجهه</th>
                                    <th scope="col" rowspan="2">اسم السائق</th>
                                    <th scope="col" rowspan="2">اسم المكتب</th>
                                    <th scope="col" rowspan="2">البطاقة الشخصية للمستقبل</th>
                                    <th scope="col" rowspan="2">رقم جوال المستقبل</th>
                                    <th scope="col" rowspan="2">اسم المستقبل</th>
                                    <th scope="col" rowspan="2">رقم جوال الرسل</th>
                                    <th scope="col" rowspan="2">البطاقة الشخصية للمرسل</th>
                                    <th scope="col"  rowspan="2">اسم المرسل</th>
                                    <th scope="col"  rowspan="2">كمية الحمولة</th>
                                    <th scope="col" colspan="3" rowspan="2" >نوع الحمولة</th>
                                    <th rowspan='3'>م</th>        
                                    <!-- rowspan="2" هذه للدمج عمودي -->
                                </tr>
                            </tbody>
                        </thead>
                                </tr>         
                                <tbody> 
                    """
        for item in BringsMessage:
            if item[14] == subMes['nameSorting']: 
                    index += 1
                    html_string += f"""
                <tr>
                    <td>{item[15]}</td> 
                    <td>{item[14]}</td> 
                    <td>{item[13]}</td> 
                    <td>{item[11]}</td> 
                    <td>{item[10]}</td> 
                    <td>{item[9]}</td> 
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

        return html_string 