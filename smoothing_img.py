import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread('./data/opencv-logo.png')
img = cv2.imread('./data/lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones((5,5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0)
mediam = cv2.medianBlur(img, 5) #resuelve "salt and pepper noise"
bilaterialFilter = cv2.bilateralFilter(img, 9, 75, 75) #rresalta bordes

titles = ['image', '2D Convolution', 'blur', 'gaussian', 'median', 'bilateral filter']
images = [img, dst, blur, gblur, mediam, bilaterialFilter]

for i in range(5):
    plt.subplot(1,5,i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()