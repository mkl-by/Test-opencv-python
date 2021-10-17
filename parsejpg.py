import cv2
import pytesseract
from glob import glob
import os
import json


def pars_img(path):
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
                pass
            d[spis[i]] = spis[i+1]
        except IndexError:
            d[spis[i]] = ''

    #  пишем в файлики jsonki
    path_out = os.path.basename(path).split('.')[0]  # берем название файла jpg
    with open(f'data{path_out}.txt', 'w') as out_file:
        json.dump(d, out_file, sort_keys=True, indent=4,
                  ensure_ascii=False)


if __name__ == '__main__':

    for path in glob(os.getcwd()+'/cv/'+'/*.jpg', recursive=True):
        pars_img(path)
