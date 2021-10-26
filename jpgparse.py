import cv2
import numpy as np
from pprint import pprint

img1 = cv2.imread('img_1.png')
# new_img = np.zeros(img.shape[:2], dtype='uint8')
# newimg = np.zeros((350, 350), dtype='uint8')
# circle = cv2.circle(new_img.copy(), (250, 300), 120, 255, -1)
# square = cv2.rectangle(new_img.copy(), (550, 240), (630, 280), 255, -1)
# img = cv2.bitwise_and(img, img, mask=square)
img = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier('face.xml')  # вытягиваем натренированную модель для обучения из xml
result = faces.detectMultiScale(img, scaleFactor=3, minNeighbors=4)
for (x, y, w, h) in result:
    cv2.rectangle(img1, (x, y), (x + w, y + h), (0, 255, 0), 2)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)  # то же из одного слоя
# img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# r, g, b = cv2.split(img)
#
# img = cv2.merge([b, r, g])
# img = cv2.GaussianBlur(img, (5, 5), 0)
# img = cv2.Canny(img, 100, 100)  #

# далее ищем контуры в изображении
# con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# Запихиваем старую картинку в новую
# cv2.drawContours(new_img, con, -1, (230, 230, 148), 1)  # создали новую картинку

# kernel = np.ones((3, 3), np.uint8)
# img = cv2.dilate(img, kernel, iterations=1)
# print(img.shape)



# for i in (r, g, b):
#     cv2.imshow(f'Result {i}', i)
cv2.imshow(f'Result', img1)
cv2.waitKey(0)