from os import access
import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("snapShotTaken") 
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def upload_file(imgName):
    access_token='VUQP-UxzovEAAAAAAAAAAb8JGfzSxmLC-Ob5XrjmbUEfwjLcP2qLPYLOg-KhzaJF'
    file=imgName
    file_From=file
    file_2="/testFolder/"+(imgName)
    dbx=dropbox.Dropbox(access_token)
    
    with open(file_From,'rb')as f:
        dbx.files_upload(f.read(),file_2,mode=dropbox.files.WriteMode.overwrite)
        print("fileUploaded")

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapShot()
            upload_file(name)

main()
 