import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime

cred = credentials.Certificate("ismjcomp-firebase-adminsdk-5wsg0-7342b6cb63.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://ismjcomp-default-rtdb.firebaseio.com/",
    'storageBucket': "ismjcomp.appspot.com"
})


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/bg.png')

folderModePath = 'Resources/modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
print(len(imgModeList))


while True:
    success, img = cap.read()
    imgBackground[162:162 + 480, 55:55 + 640] = img
    # imgBackground[162:162 + 480, 55:55 + 640] = mode0
    cv2.imshow("Webacm", img)
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)