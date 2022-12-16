import cv2
import math
import numpy as np
from cvzone.ClassificationModule import Classifier
from cvzone.HandTrackingModule import HandDetector


cap = cv2.VideoCapture(-1)
detector = HandDetector(maxHands=1)
classifier = Classifier("Model/keras_model.h5", 'Model/labels.txt')

offset = 20
imgSize=300
counter = 0

labels = ['A', 'B', 'C']

while True: 
    success, img = cap.read()
    if img is None:
        break
    imgOutput  = img.copy()
    hands, img = detector.findHands(img)
    if hands: 
        hand = hands[0]
        x, y, w, h= hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8)*255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        imgCropShape = imgCrop.shape


        aspectRatio = h/w

        try: 
            if aspectRatio > 1:
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize
                
                prediction, index = classifier.getPrediction(imgWhite, draw=False)
                print(prediction, index)

            else:
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

                prediction, index = classifier.getPrediction(imgWhite, draw=False)

            cv2.putText(imgOutput, labels[index], (x, y-20), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)

            cv2.imshow('ImageCrop', imgCrop)
            cv2.imshow('ImageWhite', imgWhite)
        except Exception as e: 
            print(str(e))
    else:
        print("Ne vidno vashih ruk")   

    cv2.imshow('Image', imgOutput)
    key = cv2.waitKey(30)
