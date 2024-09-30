import cv2
import numpy as np
import time as t

dash = "-"
cap = cv2.VideoCapture(0)
reward = []

while 1:
    ret,frame = cap.read()
    screen = np.zeros((510,640,3), np.uint8)
    screen[30:510,0:640] = frame

    result = t.localtime()
    time = str(result.tm_mday) + dash + str(result.tm_hour) + dash + str(result.tm_min) + dash + str(result.tm_sec)
    cv2.putText(screen, time, (10, 20), cv2.FONT_HERSHEY_PLAIN,  1, (255, 255, 255), 1)

    for i in range(0,len(reward)):
        cv2.putText(screen, reward[i], ((i)*60+150, 20), cv2.FONT_HERSHEY_PLAIN,  1, (0, 255, 255), 1)

    cv2.imshow("screen",screen)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord(' '):
        name = 'C:\Python\Opencv\goal\picture\\'+time+'.jpg'
        cv2.imwrite(name,screen)
        reward.insert(0,str(result.tm_min) + dash + str(result.tm_sec))
        if len(reward) > 5:
            del reward[5]