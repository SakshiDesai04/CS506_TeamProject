import cv2
import face_recognition
import  cvzone
import numpy as np

class anh:
    def __init__(self) -> None:
        pass
    

    def sepiaFilter (self, frame):
        # Convert to float to prevent loss
        sepiaFilter = np.array(frame, dtype = np.float64)
        # apply a transformation where we multiply each pixel channel
        # with the matrix for the sepia effect
        sepiaFilter = cv2.transform(sepiaFilter, np.matrix([[0.272, 0.543, 0.131], 
                                                            [0.349, 0.686, 0.168], 
                                                            [0.393, 0.769, 0.189]]))
        # normalize values greater than 255 to 255
        sepiaFilter[np.where(sepiaFilter > 255)] = 255
        sepiaFilter = np.array(sepiaFilter, dtype = np.uint8)
        return sepiaFilter

    def cartoonFilter (self, frame):
        # Transform the image
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 5)
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(frame, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        return cartoon

    def sep(self):
        camera = cv2.VideoCapture(0) 
        face_locations = []
    
        while True:
            ret, frame = camera.read()    #Capture frame
            face_locations = face_recognition.face_locations(frame) # Look for all faces in the camera
            #Draw a box around the face and show the results
            for top, right, bottom, left in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                
            sepia = self.sepiaFilter(frame)
            cv2.imshow('filter1', sepia)
            
            # if the 'q' key was hit, break from the loop
            if cv2.waitKey(1) == ord('1'):
                break

        # Release the video capture object
        camera.release()
        cv2.destroyAllWindows()
       

    def cartoon(self):
        camera = cv2.VideoCapture(0) 
        face_locations = []
    
        while True:
            ret, frame = camera.read()    #Capture frame
            face_locations = face_recognition.face_locations(frame) # Look for all faces in the camera
            #Draw a box around the face and show the results
            for top, right, bottom, left in face_locations:
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                
            cartoon = self.cartoonFilter(frame)
            cv2.imshow('filter2', cartoon)
            
            # if the 'q' key was hit, break from the loop
            if cv2.waitKey(1) == ord('q'):
                break

        # Release the video capture object
        camera.release()
        cv2.destroyAllWindows()



# def main():
#     camera = cv2.VideoCapture(0) 
#     face_locations = []
    
#     while True:
#         ret, frame = camera.read()    #Capture frame
#         face_locations = face_recognition.face_locations(frame) # Look for all faces in the camera
#         #Draw a box around the face and show the results
#         for top, right, bottom, left in face_locations:
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
            
#         cartoon = cartoonFilter(frame)
#         cv2.imshow('filter2', cartoon)
        
#         sepia = sepiaFilter(frame)
#         cv2.imshow('filter1', sepia)
        
#         # if the 'q' key was hit, break from the loop
#         if cv2.waitKey(1) == ord('1'):
#             break

#     # Release the video capture object
#     camera.release()
#     cv2.destroyAllWindows()

# main()
