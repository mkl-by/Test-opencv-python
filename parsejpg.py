import cv2
import pytesseract
from glob import glob
import os
import json


def pars_img(path):
    print(path)
    img = cv2.imread(path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #  немножко приблюрим
    img = cv2.medianBlur(img, 1)
    config = r'--oem 3 --psm 6'
    # теперь распознаем и вернем словарик
    dic = pytesseract.image_to_data(img, lang='rus', config=config, output_type=pytesseract.Output.DICT)
    # из словарика заберем список с текстом который достаем и делаем список с отдельными строками
    spis = []
    spis.append(" ".join(dic['text'][4:7]).lower().capitalize())
    k = 0  # счетчик пустых строк
    s = ''  # для сборки строк
    for j, i in enumerate(dic['text']):
        if j < 7:
            continue
        if i == '':
            k += 1
        if k == 2:
            spis.append(" ".join(dic['text'][7:j]).strip())
            k = 3
            continue
        if 3 <= k < 4:
            spis.append(i.strip())
        if k >= 4:
            if i.istitle() and not i.isupper() and s and not i.count('.'):
                spis.append(s.strip())
                s = ''
            s += (' '+i)

    d = {}
    for j, i in enumerate(range(0, len(spis), 2)):
        try:
            if j == 5:
                print(spis[i])
            d[spis[i]] = spis[i+1]
        except IndexError:
            d[spis[i]] = ''

    print(d)



    print(spis)



    # n = len(dic['text'])
    # out = dict()
    # k = ''
    # text = ''
    # for i in range(n):
    #     #print(list(map(sum, dic['text'][4:7])))
    #     if 4 <= i <= 6:
    #         k += dic['text'][i]+' '
    #
    #     if 1 <= dic['line_num'][i] < 3:
    #         text += dic['text'][i]+' '
    #
    #         out[k] = text
    #
    #     #print(out)
    #
    #     print(i,'->', dic['line_num'][i],'->', dic['par_num'][i], dic['text'][i], end='')
    #     print()
    # print(text)


    # data = pytesseract.image_to_data(img, config=config, lang='rus')
    # for i, el in enumerate(data.splitlines()):
    #     print(i, el)


if __name__ == '__main__':

    for path in glob(os.getcwd()+'/cv/'+'/*.jpg', recursive=True):

        pars_img(path)
