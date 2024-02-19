import cv2
import os
import csv
import numpy as np
import detectAndRecognize.faceRecognition as fr
import detectAndRecognize.trainer as tr

def getLabels(directory):
    max_label=0
    for path,subdirnames,filenames in os.walk(directory):
        for sname in subdirnames:
            if(int(sname) > max_label):
                max_label=int(sname)
    print(max_label)
    max_label=max_label+1
    os.mkdir(directory+'/'+str(max_label))
    return max_label    

def new_User():    
    with open('./assets/user.csv','r') as file:
        csvdata=file.read()
    csvlines=csvdata.split('\n')
    #if(len(csvlines) == 5):
    #    print("Cannot add more users.")
    #    return -1
    
    newUsername=input("Give me the name of the new user: ")
    cap= cv2.VideoCapture(0)
    i=0
    max_label=getLabels('./assets/trainingImg/')
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite('./assets/trainingImg/'+str(max_label)+'/frame'+str(i)+'.jpg',frame)
        i+=1
        
        resized_img=cv2.resize(frame,(1000,700))
        cv2.imshow("title",resized_img)
        if cv2.waitKey(10)==ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    
    csvlines.append(f'{max_label},{newUsername}')
    with open('./assets/users.csv','w',newline="") as file:
        writer=csv.writer(file)
        write.writerows(csvlines)
        
    tr.train()