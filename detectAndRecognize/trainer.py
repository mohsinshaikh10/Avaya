import cv2
import os
import numpy as np
import detectAndRecognize.faceRecognition as fr

def train():
    faces,faceID,=fr.labels_for_training_data('./assets/trainingImg/')
    face_recognizer=fr.train_classifier(faces,faceID)
    face_recognizer.save('./assets/trainingData.xml')