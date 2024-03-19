import json
import random
def json_parse(array_data):
    return json.loads(array_data)

def randomnumber():
    num1= '0123456789'
    num2 = '0123456789'
    len = 4
    number = num1 + num2
    numberIdusb = "".join(random.sample(number,len))
    return numberIdusb