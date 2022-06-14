import cv2
import  cvzone

class DetectFace:
    def __init__(self,filePath):
        self.filePath = filePath

    def camera(self):   
            
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +self.filePath)
        cap = cv2.VideoCapture(0)
        overlay = cv2.imread('filter_images/cool.png', cv2.IMREAD_UNCHANGED)

        while True:
            _,img =cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.1, 4)

            for (x,y,w,h) in faces:
                # cv2.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
                 overlay_resize = cv2.resize(overlay, (w, h))
                 img = cvzone.overlayPNG(img, overlay_resize, [x+14, y-64])
            
            cv2.imshow('img',img) 
            if cv2.waitKey(1) & 0xFF == ord('q'):  
                break;

        cap.release()
