import cv2 

#Cargamos la imagen, en el primer parametro colocamos el nombre de la imagen
#en el segundo parametro se coloca el flag de grayscale
gray_image = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)

#Para obtener la dimension de la imagen utilizamos la funcion img.shape()
#Esta devuelve un tuple con el numero de filas y columnas
dimensions = gray_image.shape
print("Dimensiones: ",dimensions)

#Apartir de la anterior funcion podemos calcular la altura y ancho
#de la imagen almacenada
(h,w) = gray_image.shape
print("Dimensiones de la imagen - Altura: {}, Ancho: {}".format(h,w))

#Calculo del numero total de elementos
total_number_of_pixels = gray_image.size
print("Numero total de elementos: ",total_number_of_pixels)

#Calculo del tipo de dato alamacenado
image_dtype = gray_image.dtype
print("Tipo de dato de la imagen: ",image_dtype)

