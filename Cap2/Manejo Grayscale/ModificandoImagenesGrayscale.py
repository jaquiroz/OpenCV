# -*- coding: utf-8 -*-
import cv2 
import matplotlib.pyplot as plt

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen del
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

#Almacenando una region de la imagen en una variable
top_left_corner = gray_image[0:50, 0:50]

#Copiamos la region de interes a otra region de la imagen
gray_image[20:70,20:70] = top_left_corner

#Modificamos el borde superio izquierdo con blanco
gray_image[0:50, 0:50] = 255

plt.imshow(gray_image, cmap='gray')
plt.show()