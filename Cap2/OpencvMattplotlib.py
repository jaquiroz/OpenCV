import cv2
import numpy as np
import matplotlib.pyplot as plt

#Cargamos la imagen
img_OpenCV = cv2.imread('logo.png')

#Dividimos la imagen cargada en los tres canales b,g,r
b, g, r = cv2.split(img_OpenCV)

#Unimos los tres canales en el formato RGB
img_matplotlib = cv2.merge([r,g,b])

#Mostramos las imegnes de OPenCV y Matplolib usando Matplotlib
#Esta es la imagen con el color equivocado
plt.subplot(121)
plt.imshow(img_OpenCV)
plt.title('Img OpenCV')
#Esta es la imagen con el verdadero color
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.title('Img Matplotlib')
plt.show()

#Ahora mostramos ambas imagenes con usando OpenCV
#Mostramos la imagen con el verdadero color
cv2.imshow('bgr', img_OpenCV)
#Mostramos la imgen equivocada
cv2.imshow('rgb', img_matplotlib)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Colocamos las imagenes en posicion horizontal
img_concats = np.concatenate((img_OpenCV, img_matplotlib), axis=1)
#Ahora mostramos la imagen ocncatenada
cv2.imshow('bgr and rgb', img_concats)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Usando numpy podemos obtenr lo canales y reconstruir la imagen RGB
B = img_OpenCV[:, :, 0]
G = img_OpenCV[:, :, 1]
R = img_OpenCV[:, :, 2]

#Transformamos la imgane a BGR a RGB usando numpy
img_RGB = img_OpenCV[:, :, :: -1]
#Mostramos la imagen
cv2.imshow('img rgb',img_RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()




