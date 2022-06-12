from token import LEFTSHIFT
import cv2
from cv2 import imread 
import face_recognition
import  cvzone
import numpy as np
import random, time

def sepiaFilter (image):
    # Convert to float to prevent loss
    sepiaFilter = np.array(image, dtype = np.float64)
    sepiaFilter = cv2.transform(sepiaFilter, np.matrix([[0.272, 0.543, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]]))
    sepiaFilter[np.where(sepiaFilter > 255)] = 255
    sepiaFilter = np.array(sepiaFilter, dtype = np.uint8)
    return sepiaFilter

def main():
    sung_glass = cv2.imread('sung.png', cv2.IMREAD_UNCHANGED)
    camera = cv2.VideoCapture(0) 
    face_locations = []
    sung = cv2.imread('sung.png', cv2.IMREAD_UNCHANGED)
    while True:
        ret, frame = camera.read()    #Capture frame
        face_locations = face_recognition.face_locations(frame) # Look for all faces in the camera
        #Draw a box around the face and show the results
        for top, right, bottom, left in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            sung = cvzone.overlayPNG(frame, sung_glass, [left,top])
            cv2.imshow('filter2', sung)

        sepia = sepiaFilter(frame)
        cv2.imshow('filter1', sepia)
        
        # if the 'q' key was hit, break from the loop
        if cv2.waitKey(1) == ord('1'):
            break

    # Release the video capture object
    camera.release()
    cv2.destroyAllWindows()

main()