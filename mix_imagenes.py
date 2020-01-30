import cv2

img = cv2.imread("./data/messi5.jpg")
img2 = cv2.imread("./data/opencv-logo.png")

print(img.shape) #return a tuple of number of row, colums, and channels
print(img.size) #return total number of pixel is accessed
print(img.dtype)#return image datatype is obtained

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

#copy the ball
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

#resize image
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

#mezclo imagenes, deben tener el mismo tamano
#dst = cv2.add(img, img2)
dst = cv2.addWeighted(img,.9, img2,.1,0) #dar peso a cada imagen para saber como predominan

cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 