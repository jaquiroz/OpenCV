import cv2
#La funcion cv.imread(), es usada para leer la imagen 
# del directorio de trabajo
img = cv2.imread('logo.png')

#Para obtener las dimensiones de la imagen usamos img.shape
#esta funcion devuelve el numero de alto, ancho y canales en una variable tipo tupple
dimensions  = img.shape
print("Dimensiones: ", dimensions)
#Asignamos los valores a variables independientes 
(h,w,c)=img.shape
print("Dimensiones de la imagen - Alto: {}, Ancho: {}, Canales: {}".format(h,w,c))

#El total del numero de elementos is obtenida por la funcion .size
total_numbers_of_elements = img.size
print("Total number of elements: ", total_numbers_of_elements) 

#El numero de total de pixeles es igual a la multiplicacion de Alto, Ancho y Canales

#EL datatype de la imagen es obtenida por la funcion .dtype
#Es muy importante fijar el tipo correcto de .dtype
image_dtype = img.dtype
print("Tipo de imagen: ", image_dtype)

