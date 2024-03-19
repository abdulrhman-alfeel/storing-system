from convertcod.internal_Loginstorge import get_loginAll,get_item

def findUser():
    if len(get_loginAll()) > 0:
        # if get_loginAll() is not None or len(get_loginAll()) > 0:
        usercount = True  
    else:
        usercount = False
    return usercount

def responsebletUser():
    user= get_item()
    # useractyle ={"Responsibilities":'',"مندوب فرزة":'',"مندوب رسائل":""}
    useractyle ={}
    if len(user) > 0:
        json = user["jsonResponsibilities"]
        useractyle= {"userName":user['userName'],"Responsibilities":user['Responsibilities'],"البحث والاستعلام":json["البحث والاستعلام"],
                "طباعة تقرير يومي": json["طباعة تقرير يومي"], 'اعادة طباعة الكوشن': json['اعادة طباعة الكوشن'], 'تعديل الكوشن': json['تعديل الكوشن'],
                "مندوب فرزة":json['مندوب فرزة'],'مندوب رسائل':json['مندوب رسائل'],
                # 'نوع الفرزة':json['نوع الفرزة']
                }
    else:
        useractyle = None

    return useractyle