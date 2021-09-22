import os
import numpy as np
import cv2
import copy
path = "C:/Users/icorr/OneDrive/Escritorio/repo/Taller3/Phantom-Cyto-Seq/Seq"

ImgOutPath = "C:/Users/icorr/OneDrive/Escritorio/repo/Taller3/ImgSalida"
if not os.path.exists(ImgOutPath):
    os.makedirs(ImgOutPath)



def Procesing(directory):
    imagesPath = directory
    filesNames = os.listdir(directory)
    count = 0
    for fileName in filesNames:
        imagePath = imagesPath + "/" + fileName

        image = cv2.imread(imagePath)
        if image is None:
            continue

        imageGris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(imageGris, (3, 3), 0)
        canny = cv2.Canny(gauss, 50,150)
        kernal = np.ones((5, 5), np.uint8)
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernal)
        (contornos, _) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("He encontrado {} objetos".format(len(contornos)))
        imgSave = cv2.drawContours(opening, contornos, -1, (0, 0, 255), 2)  #
        cv2.imshow("contornos", opening)

        cv2.waitKey(0)
        count += 1
        #cv2.imwrite(ImgOut_path + "/image" + str(count) + ".jpg", imgSave)
        cv2.waitKey(0)
    # return (contornos)

def Red(directory):
    imagesPath = directory
    filesNames = os.listdir(directory)
    count = 0

    for fileName in filesNames:
        imagePath = imagesPath + "/" + fileName
        print(imagePath)
        image = cv2.imread(imagePath)

        rB1 = np.array([0, 100, 20], np.uint8)
        rA1 = np.array([10, 255, 255], np.uint8)

        rB2 = np.array([170, 100, 10], np.uint8)
        rA2 = np.array([179, 255, 255], np.uint8)

        # Proceso para rojo
        imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        maskRed1 = cv2.inRange(imageHSV, rB1, rA1)
        maskRed2 = cv2.inRange(imageHSV, rB2, rA2)
        maskRed = cv2.add(maskRed1, maskRed2)
        onlyRed = cv2.bitwise_and(image, image, mask=maskRed)

        #cv2.imshow('Imagen', image)
        #cv2.imshow('Mod', maskRed)
        cv2.imshow('ModRed', onlyRed)
        imgR = cv2.cvtColor(onlyRed, cv2.COLOR_HSV2BGR)
        imageGris = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)
        gauss = cv2.GaussianBlur(imageGris, (3, 3), 0)
        canny = cv2.Canny(gauss, 50, 150)

        (contornos, ) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("He encontrado {} objetos".format(len(contornos)))
        imgSave = cv2.drawContours(image, contornos, -1, (0, 0, 255), 2)  #
        cv2.imshow("contornos", image)

        count += 1

        #cv2.imwrite(ImgOutPath + "/image" + str(count) + ".jpg", onlyRed)

        cv2.waitKey()


def Blue(directory):
    imagesPath = directory
    filesNames = os.listdir(directory)
    count = 0

    for fileName in filesNames:
        imagePath = imagesPath + "/" + fileName
        print(imagePath)
        image = cv2.imread(imagePath)

        bB1 = np.array([100, 100, 50], np.uint8)
        bA1 = np.array([140, 255, 255], np.uint8)


        imageHSV = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        maskBlue1 = cv2.inRange(imageHSV, bB1, bA1)

        #maskRed = cv2.add(maskRed1, maskRed2)
        onlyBlue = cv2.bitwise_and(image, image, mask=maskBlue1)

        # cv2.imshow('Imagen', image)
        # cv2.imshow('Mod', maskBlue)
        cv2.imshow('ModBlue', onlyBlue)

        count += 1

        # cv2.imwrite(ImgOutPath + "/image" + str(count) + ".jpg", onlyBlue)

        cv2.waitKey()

print(Procesing(path))