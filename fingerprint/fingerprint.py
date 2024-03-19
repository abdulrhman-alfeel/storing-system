# https://www.youtube.com/watch?v=0MiWOIb0GfQ&list=PLrUF5HNl_xIJfavQzcO_u-4glaR6MFT3x


import os 
import time 
# import mariadb

from AratekA600 import AratekA600class 
from termcolor import colored

os.system('color')

# set the prompt color to white 
promptColor = colored('white','white')


# set the input color to blue 
inputColor = colored('Blue', 'blue')
# Define the colored input function
def  colored_input(prompt, color):
    user_input = input(colored(prompt, color))
    
    # Return the user`s input with the same color 
    return colored(user_input,color)

def Aratek_A600_Initialize(aratekA600):
    # ARATEK DEVICE COUNT 
    devVount = 0 # COUNT OF CONNECTEO DEVICES
    devCount = aratekA600.GetCountOfConnectedDevices()


    if devCount == 1:
        # IF 1 (ONE) ARATEK A600 DEVICE IS CONNECTED, NOTIFY USER TO DISCONECT
        list_user_options(aratekA600)
    elif devCount > 1:
        # IF MORE THAN 1 ARATEK A600 DEVICE() ARE CONNECTED, NOTIFY USER TO DISCONECT
        print("ALERT:                THIS CODE CAN NOLY HANDLE 1 ARATEK A600 DEVICE AT A TIME ")
        return
    elif devCount == 0 :
        print("ALERT:         THERE IS NO ARATEK A600 DEVICE THAT IS CONNECTED")
        return
    else:
        print('ALERT:       1 DO NOT SEE HOW THIS CODE EXECUTION COULD END UP HERE!')
        return
    

def list_user_options(aratekA600):
    num_selected = 1000000    # AN ARBITRARY INT NUMBER

    print("")
    print("0   Get number of Connected ARATEK A600 fingerprint Scanners")
    print("1   Get Particulars for Connected Connected ARATEK A600  Device AT A TIME")
    print('2   power ON ARATEK A600 Fingerprint Scanner`s GREEN LED Light for some ')
    print("3   power ON ARATEK A600 Fingerprint Scanner`s GREEN LED Light for some")
    print("4   Capture and Display Fingerprint image using Connected ARATEK A600")
    print("5   Exit")
    print("")

    str_user_input = input("Select an Option to Proceed   :").strip()
    if str_user_input.isdigit():
        num_selected = int(str_user_input)
        process_user_selection(aratekA600, num_selected)
    else:
        print("PLEASE ENTER A NUMERICAL INT VALUE TO TRY OUT THE CONNECTED ARATEK A600")
        return
    
def clear_screen():
    # CLEAR THE SCREEN 
    if os.name == 'nt':
        # WINDOWS 
        os.system('cls')
    else:
        # LINUX & RASPBERRY PI BOOKWORM OS 
        os.system('clear')

def process_user_selection(aratekA600, user_selection):
    # LED CONTROLS
    redLED = 1 # RED LED
    greenLED = 0 #Green LED
    onLED = 1 # POWER ON LED
    offLED = 0 # power oFF LED

    # OPENING ARATEK A600 DEVICE
    valcountDevices = aratekA600.GetCountOfconnectedDevices()
    connectedDeviceIndex = valcountDevices -1 
    valretOpenDevice = aratekA600.OpenDevice(connectedDeviceIndex)
    print("")
    if valretOpenDevice == 0 : # OPENING DEVICE WAS SUCCESSFUL
        print("SUCCESS:      ARATEK A600 WAS OPENED")
    elif valretOpenDevice == -106:
        print("INFO:    ARATEK A600 IS ALREADY OPENED")
    elif valretOpenDevice == -108:
        print("ERROR:        FAILED TO OBTAIN ARATEK A600 DEVICE INFDRMATION")
        return
    elif  valretOpenDevice == -109:
        print('ERROR:    ARATEK A600 FAILED TO OPEN')
    elif valretOpenDevice == -104:
        print('ERROR: FAILED TO INITALIZE ARATEK A600 FINGERPRINT ALGORITHM')
        return
    else:
        print('UNKNOWN ERROR AT OpenDevice : ', valretOpenDevice)
        return
    
    
    print('')
    match user_selection:
        case 0:
            print("0: Selected - To Get Number of Connected ARATEK A600 Fingerprint")
            #  valcountDevices = aratekA600.GetCountDfConneccedDevices()
            print("Number of Connected ARATEK A600 Devices is :", valcountDevices,"\n")
        case 1:
            print('1:   Selected   - To Get Particulars for Connected Connected ARATEK')
            AratelA600DevDesc =  aratekA600.GetDeviceDescription(connectedDeviceIndex)
            print("********************************************************")
            print("my Device Name                     : ", aratekA600.GetDevInfoText(AratelA600DevDesc.productName))
            print("my Device Model                     : ", aratekA600.GetDevInfoText(AratelA600DevDesc.productModel))
            print("my Device Manufacturer Name                     : ", aratekA600.GetDevInfoText(AratelA600DevDesc.manufacturer))
            print("*******************************************")
        case 2: 
            print("2:   Selected   -  To Power on ARATEK A600 Fingerprint Scanner`s")
            str_led_seconds = input("Enter Time in Seconds to Display Red LED   :").strip()
            print(" ")
            if str_led_seconds.isdigit():
                num_selected = int(str_led_seconds)
                aratekA600.FlashLEDLight(redLED, onLED, num_selected)
                print("")
            else:
                print('Please Enter a Numeric Value for Seconds to Display RED LED \n')
        case 3: 
            print("3:   Selected   - To Power ON ARATEK A600 Fingerprint Scanner`s ")
            str_led_seconds = input("Enter  Time in Seconds to Display Green LED   :   ").strip()
            if str_led_seconds.isdigit():
                num_selected = int(str_led_seconds)
                aratekA600.FlashLEDLight(greenLED, onLED, num_selected)
            else:
                print("Please Enter a Numeric Value for Seconds to DISPLAY green LED \n")
                return
        case 4: 
            print("4:   Selected   -  To Capture and Display Fingerprint image ")
            print('START FINGERPRINT CAPTURE NOW  \n')
            valretCaptureFpImg = aratekA600.CaptureFinger()
            if valretCaptureFpImg == 0:
                print('ERROR:       Fingerprint Raw Image Captured')
            elif valretCaptureFpImg == 10 :
                print("ERROR:    FAILED to Allocate Memory  during Fingerprint Raw")
                return
            elif valretCaptureFpImg == -100:
                print("ERROR :      the ARATEK A600 dose not exist the ARATEK A600 may ")
                return
            elif valretCaptureFpImg == -113:
                print("INFO:     FINGER WAS NOT Presented for Gapture on ARATEK A600")
            elif valretCaptureFpImg == -103:
                print("ERROR:    the ARATEK A600 DID NOT OPEN\n")
                return 
            elif valretCaptureFpImg == -104:
                print("ERROR:    The ARATEK A600 Failed to Capture Image\n")
                return 
            elif valretCaptureFpImg == -110:
                print("INFO:     Fingerprint Image Capture Timed Dut\n")
            elif valretCaptureFpImg == -900:
                print('ERROR:      invalid Parameter\n')
                return 
            elif valretCaptureFpImg == -905:
                print("ERROR:    THE ARATEK A600 API has NOT BEEN INITIALIZED\n")
            else:
                print('UNKOWN ERROR AT CaptureFinger  : ', valretCaptureFpImg)
        case 5 :
            # FIRST CLEAR SCREEN
            clear_screen()
            print("5:  Selected  -   To Register Useer\n")
            finger1 = ""
            finger2 = ""
            statusEnrollingFinger1= 'FINGERPRINT 1'
            statusEnrollingFinger2 = "FINGERPRINT 2"

            #  ARATEK BIOMETRICS GREEN COLOR CODE
            aratekColorCodeSTART = "\033[92m"
            aratekColorCodeEND = '\033[0m'

            #  CAPTURE CONTRACTOR PARTICULARS 
            print("|-------------------------------------------------|")
            print('REGISTER CONTRACTOR PARTICULARS AND BIOMETRICS')
            firstName = input(f'Enter First Name \t\t: {aratekColorCodeSTART}').strip()
            print(aratekColorCodeEND, end='')
            secondName = input(f'Enter Second name \t\t: {aratekColorCodeSTART}').strip()
            print(aratekColorCodeEND, end='')
            profession = input(f"Profession\t\t:{aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND,end='')
            email= input(f"Contact E-mail Address\t\t: {aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND,end='')
            biometricScanner = input(f"computing Platform?\t\t: {aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND, end='')
            computingPlatform = input (f"computing platform?\t\t:{aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND,end='')
            computingPlatformOS = input (f"computing platform OS?\t\t:{aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND,end='')
            rdbmsName = input(f"RDBMS used?\t\t\t:  {aratekColorCodeSTART}").strip()
            print(aratekColorCodeEND,end='')
            print("|------------------------------------------------------|")
            print('\n')

            # ENROLLINO FINGERPRINT 1
            finger1 = PromptFingerEnrollment(aratekA600, statusEnrollingFinger1)

            time.sleep(1)

            finger1 = PromptFingerEnrollment(aratekA600, statusEnrollingFinger2)

            print(f"FINGER 1:  {finger1}")
            print('\n')
            # return finger
        
def captureFinger(aratekA600, statusfingerEnroll):
    print(f"NOW CAPIURING {statusfingerEnroll} ......................")
    time.sleep(1)
    return aratekA600.GetCapturedISOFinger()

if __name__ == "__main__":
    print('\nJSOEPH MWEMA | BIOMETICS ENGINEER | EMAIL: biometrices@jomutech.com')

    aratekA600Api = AratekA600class()

    Aratek_A600_Initialize(aratekA600Api)

    aratekA600Api.FreeGlobalResourcee()
    print('FREEING UP GLOBAL RESOURCE ALLOCATIONS IS COMPLETE')


    



