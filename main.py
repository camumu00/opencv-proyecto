import cv2
import numpy as np

# Leer imagen
img = cv2.imread("foto.jpg")
if img is None:
    print("Error: no se encontró la imagen 'foto.jpg'")
    exit()

# Función que se llama cada vez que movemos el slider
def update_gray(val):
    factor = val / 100
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    adjusted = cv2.addWeighted(gray, factor, np.ones_like(gray)*255, 1-factor, 0)
    cv2.imshow("Escala de grises ajustable", adjusted)

cv2.namedWindow("Escala de grises ajustable")
cv2.createTrackbar("Nivel", "Escala de grises ajustable", 100, 100, update_gray)

update_gray(100)

cv2.waitKey(0)
cv2.destroyAllWindows()
