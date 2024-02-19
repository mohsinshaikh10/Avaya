import detectAndRecognize.videoTester as frec
import cv2
import os
import numpy as np
import detectAndRecognize.newUser as nu
from chatBot import main
    
def predictName(label):
    with open('./assets/user.csv','r') as file:
        lines=file.read().split('\n')

    for line in lines:
        userlist=line.split(',')
        if int(userlist[0]) == label:
            return userlist[1]
    
    return "world"
    
def authentication():
    print('authentication')
    retryCount = 0;
    while retryCount <3:
        success_recgnition,label=frec.video_tester()
        if(success_recgnition == 1):
            print("Authentication Succesfull")
            predicted_name=predictName(label)
            print(f"Hello! {predicted_name}")
            return True
        else:
            print("Authentication failure!")
            retryInput=input("Do you want to retry? (Y/N): ")

        if (retryInput == 'Y' or retryInput == 'y'):
            retryCount=retryCount+1
            continue
        else:
            break
    if retryCount>=3 and (retryInput == 'Y' or retryInput == 'y'):
        newUserReg()
    else:
        return False


def newUserReg():
    registerUser=input("Do you want to register new user(Y/N)? : ")
    if(registerUser  == 'Y' or registerUser == 'y'):
        print("Admin authentication Required")
        success_recgnition,label=frec.video_tester()
        if(success_recgnition == 1 and label == 0):
            print("Authentication Succesfull")
            newUserIn=input("Do you want to allow new user regestration?")
            if (newUserIn == 'Y' or newUserIn == 'y'):
                status=nu.new_User()
                print("User registered succesfully")
            else:
                print("Admin permission Denied")
    else:
        print("Admin permission Denied")


    


if __name__ == "__main__":
    # success=authentication()
    # if success:
    main.wakeup()