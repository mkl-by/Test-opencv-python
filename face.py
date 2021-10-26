import cv2
# import numpy as np
# from pprint import pprint

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 24)  # Частота кадров
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 600) # Ширина кадров в видеопотоке.
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
faces = cv2.CascadeClassifier('face.xml')  # вытягиваем натренированную модель для обучения из xml
while True:
    ret, img = cap.read()
    img_new = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    result = faces.detectMultiScale(img_new, scaleFactor=1.3, minNeighbors=3)
    for (x, y, w, h) in result:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow(f'Camera', img)
    if cv2.waitKey(10) == 27:  # Клавиша Esc
        break

cv2.release()
cv2.destroyAllWindows()
