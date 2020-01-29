import cv2
import datetime
cap = cv2.VideoCapture(0)#webcam
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

cap.set(3, 700) #3 = CAP_PROP_FRAME_WIDTH
cap.set(4, 700) #4 = CAP_PROP_FRAME_HEIGHT

print(cap.get(3))
print(cap.get(4))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_COMPLEX
        text = "w: " + str(cap.get(3)) + " h: " + str(cap.get(4))
        d = str(datetime.datetime.now())
        frame = cv2.putText(frame, text, (10,50), font, 1, (0,255,255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, d, (10,100), font, 1, (0,255,255), 2, cv2.LINE_AA)
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()