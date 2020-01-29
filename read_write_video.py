import cv2

cap = cv2.VideoCapture(0) #webcam

#si quiero crear un video
#fourcc = cv2.VideoWriter_fourcc("X", "V", "I", "D")
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480)) 

#cap = cv2.VideoCapture("name.avi") #video
#si usas un video validas con
#while(cap.isOpened()):

while (True):
    ret, frame = cap.read()

    if ret == True:
        w = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(w)
        print(h)

        #si vas a guardar video
        out.write(frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", gray) #escala de grises
        #cv2.imshow("frame", frame) #normal

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()

#si vas a guardar video
out.release()

cv2.destroyAllWindows()