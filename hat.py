import cv2

class mask:

    def __init__(self):
        pass

    def camera(Self):
        face_cascade = cv2.CascadeClassifier('/Users/sakshi/Documents/GitHub/Filter_Trial09/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('/Users/sakshi/Documents/GitHub/Filter_Trial09/haarcascade_frontalface_default.xml')

        hat = cv2.imread('hat.png')

        original_hat_h,original_hat_w,hat_channels = hat.shape
        hat_gray = cv2.cvtColor(hat, cv2.COLOR_BGR2GRAY)
        ret, original_mask = cv2.threshold(hat_gray, 10, 255, cv2.THRESH_BINARY_INV)
        original_mask_inv = cv2.bitwise_not(original_mask)

        cap = cv2.VideoCapture(0)
        ret, img = cap.read()
        img_h, img_w = img.shape[:2]

        while True:   
            
            ret, img = cap.read()
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.5, 4)

            for (x,y,w,h) in faces:
                face_w = w
                face_h = h
                face_x1 = x
                face_x2 = face_x1 + face_w
                face_y1 = y
                face_y2 = face_y1 + face_h

                hat_width = int(1.5 * face_w)
                hat_height = int(hat_width * original_hat_h / original_hat_w)
                
                hat_x1 = face_x2 - int(face_w/2) - int(hat_width/2)
                hat_x2 = hat_x1 + hat_width
                hat_y1 = face_y1 - int(face_h*1.25)
                hat_y2 = hat_y1 + hat_height 

                if hat_x1 < 0:
                    hat_x1 = 0
                if hat_y1 < 0:
                    hat_y1 = 0
                if hat_x2 > img_w:
                    hat_x2 = img_w
                if hat_y2 > img_h:
                    hat_y2 = img_h

                hat_width = hat_x2 - hat_x1
                hat_height = hat_y2 - hat_y1

                hat = cv2.resize(hat, (hat_width,hat_height), interpolation = cv2.INTER_AREA)
                mask = cv2.resize(original_mask, (hat_width,hat_height), interpolation = cv2.INTER_AREA)
                mask_inv = cv2.resize(original_mask_inv, (hat_width,hat_height), interpolation = cv2.INTER_AREA)

                roi = img[hat_y1:hat_y2, hat_x1:hat_x2]

                roi_bg = cv2.bitwise_and(roi,roi,mask = mask)
                roi_fg = cv2.bitwise_and(hat,hat,mask=mask_inv)
                dst = cv2.add(roi_bg,roi_fg)

                img[hat_y1:hat_y2, hat_x1:hat_x2] = dst
                break

            cv2.imshow('img',img) 

            if cv2.waitKey(1) == ord('q'):  
                break;

    
    cv2.destroyAllWindows() 
