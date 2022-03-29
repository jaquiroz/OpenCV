import cv2
#La funcion cv.imread(), es usada para leer la imagen 
# del directorio de trabajo
img = cv2.imread('logo.png')

#Obtenemos el valor del pixel x=40, y=6
(b,g,r) = img[6,40]
print("Valores del pixel (40,6) - Rojo: {}, Verde: {}, Azul: {}".format(r,g,b))

#Accedemos solo un canal a la vez del
b1 = img[6,40,0]
g1 = img[6,40,1]
r1 = img[6,40,2]
print("Verificando los valores del pixel (40,6) - Rojo: {}, Verde: {}, Azul: {}".format(r1,g1,b1))