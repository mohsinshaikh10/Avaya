import cv2
import os
import numpy as np
import detectAndRecognize.faceRecognition as fr
import time


def video_tester() :
    face_recognizer=cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read('./assets/models/trainingData.xml')
    frameCount=0
    print("Turning on camera")
    cap=cv2.VideoCapture(0)
    while True:
        frameCount+=1
        ret,test_img=cap.read()
        faces_detected,gray_img=fr.faceDetection(test_img)
        for face in faces_detected:
            (x,y,w,h)=face
            roi_gray=gray_img[y:y+h,x:x+w]
            label,confidence=face_recognizer.predict(roi_gray)
            if(confidence>=40):
                fr.draw_rect(test_img,face)
               
            else:
                cap.release()
                cv2.destroyAllWindows()
                print("FACE RECOGNIZED") 
                return 1,label
            #resized_img=cv2.resize(test_img,(1000,700))
            #cv2.imshow("title",resized_img)
        if frameCount == 100:
            break   
    cap.release()
    cv2.destroyAllWindows()
    return 0,-1
