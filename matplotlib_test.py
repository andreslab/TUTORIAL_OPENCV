import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('./data/lena.jpg', -1)
cv.imshow("image", img)

#ajusto los colores
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img)

#elimina la regla de medidas a los lados de la imagen
plt.xticks([]), plt.yticks([])
 
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()