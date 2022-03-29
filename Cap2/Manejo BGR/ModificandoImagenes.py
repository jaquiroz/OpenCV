import cv2
import matplotlib.pyplot as plt

#La funcion cv.imread(), es usada para leer la imagen del directorio de trabajo
img = cv2.imread('logo.png')
#NOTA: OpenCV maneja los canales en el orde BGR en cambio matplotlib maneja el orde RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Tomamos una seccion de la imagen
top_left_corner = img_RGB[0:50,0:50]

#Podemos pegar esta imagen recortada en otra region de la imagen original
img_RGB[20:70,20:70] = top_left_corner

#Convertimos toda una region en color Azul
img_RGB[0:50,0:50] = (0,0,255)


plt.imshow(img_RGB)
plt.show()