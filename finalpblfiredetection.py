
import cv2         # Library for openCV
import threading   # Library for threading -- which allows code to run in backend
import playsound   # Library for alarm sound

import os
from twilio.rest import Client

fire_cascade = cv2.CascadeClassifier('fire_detection_cascade_model.xml') # To access xml file which includes positive and negative images of fire. (Trained images)
                                                                         # File is also provided with the code.

vid = cv2.VideoCapture(0) # To start camera this command is used "0" for laptop inbuilt camera and "1" for USB attahed camera for pc
runOnce = False # created boolean

def play_alarm_sound_function(): # defined function to play alarm post fire detection using threading
    playsound.playsound("Alarm Sound.mp3",True) # to play alarm # mp3 audio file is also provided with the code.
    print("Fire alarm end") # to print in console

#client details
account_sid = "AC766879e6b6bb1913f3fb1e9958905e05"
auth_token = "c852a0b8dd9868dfb1c00c8fbd1d3b43"
client = Client(account_sid, auth_token)
def message () :
        client.messages.create(
          body="Hello from Twilio",
          from_="+14439410869",
          to="+917058801615"
        )
        print("message send ")

		
while(True):
    Alarm_Status = False
    ret, frame = vid.read() # Value in ret is True # To read video frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # To convert frame into gray color
    fire = fire_cascade.detectMultiScale(frame, 1.2, 5) # to provide frame resolution

    ## to highlight fire with square 
    for (x,y,w,h) in fire:
        cv2.rectangle(frame,(x-20,y-20),(x+w+20,y+h+20),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        print("Fire alarm initiated")
        threading.Thread(target=play_alarm_sound_function).start()  # To call alarm thread


    
        if runOnce == False:
             message = client.messages.create(
            body="Fire detected!",
            from_="+14439410869",
            to="+917058801615"
        )
        print("SMS sent!")
           
            


    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break