import os

import cv2

images_path = "C:/Users/joses/OneDrive/Escritorio/ImgP"
files_names = os.listdir(images_path)

ImgSalida_path="C:/Users/joses/OneDrive/Escritorio/ImgSalida"
if not os.path.exists(ImgSalida_path):
    os.makedirs(ImgSalida_path)
    print("Directory Created", ImgSalida_path)

count = 0
for file_name in files_names:
    image_path = images_path + "/" + file_name
    print(image_path)
    image = cv2.imread(image_path)
    if image is None:
        continue
    cv2.imshow("image", image)
    imageGris = cv2.cvtColor(image, cv2.COLORBGR2GRAY)
    gauss = cv2.GaussianBlur(imageGris, (5,5), 0)
    cv2.imshow("Suavizado", gauss)

    canny = cv2.Canny(gauss, 50, 150)
    cv2.imshow("canny", canny)

    (contornos, ) = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Mostramos el número de monedas por consola
    print("He encontrado {} objetos".format(len(contornos)))

    imgSave = cv2.drawContours(image, contornos, -1, (0, 0, 255), 2)
    cv2.imshow("contornos", image)

    cv2.waitKey(0)
    count += 1
    cv2.imwrite(ImgSalida_path + "/image" + str(count) + ".jpg", imgSave)
    cv2.waitKey(0)