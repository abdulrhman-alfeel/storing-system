from datetime import datetime,timedelta



def TimeMonth():
    timeData=[]
    months=  datetime.now().month
    years=  datetime.now().year
    if months == 2:
        namberday = 28 
    elif months != 1 and months != 3 and months != 5 and months != 7 and months != 8 and months != 10 and months != 12:
        namberday = 30 
    else:
        namberday = 31 
    start_data = datetime(years,months,1)
    end_data = datetime(years,months,namberday)   
    for day in range((end_data - start_data).days +1):
                timeArray = start_data + timedelta(days=day)
                timeData.append(timeArray.date()) 
    return timeData
