import cv2
from matplotlib import pyplot as plt
from .processor import resource_path
import uuid
# import keyboard
# import pynput 
def cameraCop():
    u4 = uuid.uuid4()
    # Open the camera
    cap = cv2.VideoCapture(0)
    url= f'assets/imges/{u4}.jpg'

    while True:
        # Read the frame
        ret, frame = cap.read()

        # Display the frame
        cv2.imshow('Camera', frame)

        # Stop if 'q' is pressed
        if cv2.waitKey(1) == ord('q') :
            cv2.imwrite(resource_path(url),frame)
            break
        # if keyboard.read_key('k'):
        #     print('hhhhhhhhhoooooooooo')
        #     cv2.imwrite(resource_path(url),frame)
        #     break
        else:
            pass

    # listenar = pynput.keyboard.Listener(on_press=on_press)
    # listenar.start()
            
    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
    return url
    



    

     # ad=['a','S','d','f','g','h','j','k','l',';','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p','{','}',',','.']
        # def on_press(key):
        #     for i in ad:
        #         if  keyboard.read_key(key) == i  :
                   
        #             print(key)
        #         else:
        #             print("adfa",key)
        #             # keyboard.remove_word_listener(key)
        # listener = pynput.keyboard.Listener(on_press=on_press)
        # listener.start()
       



# import cv2

# # Open the camera
# cap = cv2.VideoCapture(0)

# while True:
#     # Read the frame
#     ret, frame = cap.read()

#     # Display the frame
#     cv2.imshow('Camera', frame)

#     # Stop if 'q' is pressed
#     if cv2.waitKey(1) == ord('q'):
#         break

# # Release the camera and close the window
# cap.release()
# cv2.destroyAllWindows()