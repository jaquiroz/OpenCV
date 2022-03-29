import cv2
import matplotlib.pyplot as plt


#La funcion cv.imread(), es usada para leer la imagen del directorio de trabajo
img = cv2.imread('logo.png')
#NOTA: OpenCV maneja los canales en el orde BGR en cambio matplotlib maneja el orde RGB
img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Muestra la imagen asignada a la variable img
plt.imshow(img_RGB)
plt.show()
