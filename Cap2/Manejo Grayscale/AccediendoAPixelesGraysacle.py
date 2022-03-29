# -*- coding: utf-8 -*-
import cv2 

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen 
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

#Se puede acceder a un pixel con los valore de fila y columna especificos
i = gray_image[6,40]
print("Pixel (6,40) - Intensidad ",i)


