from datetime import datetime

def TimeYars():
    timeData=[]
    iyrs = datetime.now().date().year
    month = [item for item in range(1,13)]  
    for keymon in month:
        if len(str(keymon)) == 1:
            datab =f"{iyrs}-0{keymon}"
        else:
            datab =f"{iyrs}-{keymon}"
        timeData.append(datab) 
    return timeData
