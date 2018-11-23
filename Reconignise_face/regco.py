import cv2
import cv2.face
import numpy as np
import mysql.connector as con
# from pygame import mixer
import playsound
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("C:\\Users\\abc\\PycharmProjects\\AI2\\Reconignise_face\\recognizer\\trainningData.yml")
font=cv2.FONT_HERSHEY_SIMPLEX

def getProfile(id):
    conn=con.connect(host="localhost", user="root", passwd="abc.123", database="mydb")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.cursor()
    cursor.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile

while(True):
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        print(conf)
        #set threadhold
        if conf < 50:
            profile = getProfile(id)
            if (profile != None):
                cv2.putText(img, "Name : " + str(profile[1]), (x, y + h + 20), font, 0.3, (0, 255, 0))
                # if str(profile[1]) == "CHainx":
                #     cv2.imwrite("C:\\Users\\abc\\Desktop\\nguyenxuanchai.jpg",gray[y:y+h,x:x+w])
        else:
            playsound.playsound('G:\\Media\\coiBaoDong.mp3', True)

    cv2.imshow("Face",img)
    if(cv2.waitKey(1)==ord('q')):
        break;
cam.release()
cv2.destroyAllWindows()