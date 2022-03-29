import cv2
import matplotlib.pyplot as plt
#La funcion cv.imread(), es usada para leer la imagen 
# del directorio de trabajo
img = cv2.imread('logo.png')

#Corre una sesion de ipython
cv2.startWindowThread()

#La funcion .imshow () muestra una imagen por pantalla. 
#El primer parametro muestra el nombre asigando a la pantalla emergente. 
#El segundo parametro se asigna a la variable en la cual se encuentra almacenada la imagen.
cv2.imshow("Original image: ",img)

#La funcion .waitKey() espera en milisegundos por alguna entrada desde el teclado
#Si el valor asignado es cero, el programa continuara hasta una entrada por teclado
cv2.waitKey(0)
cv2.destroyAllWindows()