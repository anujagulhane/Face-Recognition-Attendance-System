import cv2
import numpy as np
import sqlite3

# file to detect face features
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face_id = input('Enter your id')
face_name= input('Enter your name')
# opening webcam
cap = cv2.VideoCapture(0)

count = 0

def database(id, name):
	conn = sqlite3.connect("Attendance.db")
	cursor = conn.cursor()

	cursor.execute(""" CREATE TABLE IF NOT EXISTS Employee(ID TEXT, Name TEXT, Present TEXT, DD date, TT time)    """)

	# inserting name and id into database
	cursor.execute(""" INSERT INTO Employee(ID, Name) VALUES (?,?) """,(id,name))

	conn.commit()
	cursor.close()
	conn.close()

while True:
	# capturing images
	ret, frame = cap.read()
	# converting into gray scale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_classifier.detectMultiScale(gray, 1.3, 5)
	for(x,y,w,h) in faces:
		count+=1
		# adding images to folder with id
		file_name_path = 'data/user.'+str(face_id)+'.'+str(count)+'.jpg'
		cv2.imwrite(file_name_path,gray[ y:y+h,x:x+h])
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)
		cv2.putText(frame,str(count),(100,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),2)
	cv2.imshow('faces', frame)
	
	if cv2.waitKey(1)==13 or count>40:
		break

cap.release()
cv2.destroyAllWindows()
database(face_id,face_name)
print("Collecting samples complete!!!")