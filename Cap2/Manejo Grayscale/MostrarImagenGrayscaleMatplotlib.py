# -*- coding: utf-8 -*-
import cv2 
import matplotlib.pyplot as plt

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen 
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

plt.imshow(gray_image, cmap='gray')
plt.show()
