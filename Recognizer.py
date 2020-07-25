
import cv2, numpy as np
import datetime
import sqlite3
from tkinter import *
from tkinter import messagebox

window=Tk()
window.withdraw()
now= datetime.datetime.now()
dd=now.strftime("%y-%m-%d")
time=now.strftime("%H:%M:%S")

face_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def getName(id):
    conn = sqlite3.connect("Attendance.db")
    cursor = conn.cursor()
    # get name for detected id from database
    cr=cursor.execute(""" SELECT Name FROM Employee where ID=(?);""",(id,))
    name = cursor.fetchone()

    conn.commit()
    cursor.close()
    conn.close()
    return name


def markAttendance(id):
    conn = sqlite3.connect("Attendance.db")
    cursor = conn.cursor()
    temp=0
    cursor.execute(""" SELECT DD FROM Employee where ID=(?);""",(id,))
    dd = str(cursor.fetchone())
    curr=str("('"+now.strftime("%Y-%m-%d")+"',)")
    
    # add attendance with time if not present for current date
    if dd!=curr:
        cursor.execute("""UPDATE Employee SET Present="Yes", DD = date('now'), TT= time('now') WHERE ID=(?);""",(id,))
    
    conn.commit()
    cursor.close()
    conn.close()
  
cap = cv2.VideoCapture(0);
recognizer = cv2.face.LBPHFaceRecognizer_create();
recognizer.read('recognizer/trainer.yml');

id=0;

font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, img = cap.read();
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    faces = face_cas.detectMultiScale(gray, 1.3, 7);
    for (x,y,w,h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        id,conf=recognizer.predict(roi_gray)
        namee = getName(id)
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);

        try:
            id,conf=recognizer.predict(roi_gray)
            namee = getName(id)
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2);

            if conf < 500:
                confidence = int(100*(1-(conf)/300))
                display_string = str(namee)+ str(confidence)+'% Confidence'
            
            if confidence > 60:
                cv2.putText(img,display_string,(x,y+170), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                cv2.imshow('Face Cropper', img)
                markAttendance(id)
    
            else:
                cv2.putText(img,"face not match",(x,y-20), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
                cv2.imshow('Face Cropper', img)


        except:
            cv2.putText(img, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
            cv2.imshow('Face Cropper', img)
            pass
        
    k =  cv2.waitKey(30) & 0xff
    if k==13:
        break

cap.release();
cv2.destroyAllWindows();
