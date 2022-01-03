import cv2

def take_snapShot():
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret, frame=videoCaptureObject.read()
        cv2.imwrite("newPicture.jpg",frame)
        result=False
    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapShot()