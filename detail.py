import cv2

img = cv2.imread("./data/lena.jpg")

print(img.shape) #return a tuple of number of row, colums, and channels
print(img.size) #return total number of pixel is accessed
print(img.dtype)#return image datatype is obtained

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()