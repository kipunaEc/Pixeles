#Importar librería cv2
import cv2
 
#Leer imagen
img = cv2.imread('pixeles.jpg')
 
#Conocer el valor del pixel (0 ,0) y (8,8)
print("Color posición 0,0: " + str(img[0,0]) )
print("Color posición 8,8: " + str(img[8,8]) )
 
#Mostrar imagen
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
