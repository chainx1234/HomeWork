import cv2
import numpy as np
import mysql.connector as con

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);

def insertOrUpdate(Id,Name):
    mydb = con.connect(host="localhost", user="root", passwd="abc.123", database="mydb")
    cursor = mydb.cursor()
    cmd="SELECT * FROM People WHERE ID="+str(Id)
    cursor.execute(cmd)
    isRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(isRecordExist==1):
        cmd="UPDATE People SET Name='{}' WHERE ID={}".format(str(Name), str(Id))

    else:
        cmd="INSERT INTO People(ID,Name) Values({},'{}')".format(str(Id), str(Name))

    cursor.execute(cmd)

    mydb.commit()
    mydb.close()

Id=input('Enter User Id')
name=input('Enter User Name')

insertOrUpdate(Id,name)
sampleNum=0
while(True):
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        sampleNum=sampleNum+1;
        cv2.imwrite("C:\\Users\\abc\\PycharmProjects\\AI2\\Reconignise_face"
                    "\\data\\User."+str(Id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow("Face", img)

        cv2.waitKey(100)
    #cv2.imshow("Face",img);
    cv2.waitKey(1);
    if(sampleNum>20):
        break;
cam.release()
cv2.destroyAllWindows()