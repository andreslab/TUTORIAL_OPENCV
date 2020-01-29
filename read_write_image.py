import cv2

img = cv2.imread("./data/lena.jpg", 1)
#1 = color, 0 = escala de grises, -1 = color con alpha

cv2.imshow("imagen", img)
k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("lena2.jpg", img)
    cv2.destroyAllWindows()

