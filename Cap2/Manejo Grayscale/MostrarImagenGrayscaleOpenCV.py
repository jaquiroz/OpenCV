import cv2 

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen del
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

#Corremos una sesion de ipython
cv2.startWindowThread()

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen del
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

#Desplegamos una ventana con la imagen almacenada
cv2.imshow("original image", gray_image)

#Esperamos una interrupcion para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()

