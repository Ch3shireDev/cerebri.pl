from pdf2image import convert_from_path
import cv2
import os
import glob
import sys
import tempfile


dir_positive = './data/positive/'
dir_negative = './data/negative/'

for directory in [dir_positive, dir_negative]:
    if not os.path.exists(directory):
        os.makedirs(directory)


H0 = 1040
dH = 65

drawing = False

from enum import Enum


class Keys(Enum):
    LEFT_ARROW = 2424832
    RIGHT_ARROW = 2555904
    ENTER = 13
    SPACE = 32
    Z = 122


xstart, ystart = 0, 0

def save(img, directory):
    n = len(os.listdir(directory))
    cv2.imwrite(directory+"%d.png" % n, img)


def mouse_events(event, x, y, flags, param):
    global img2, xstart, ystart
    if event == cv2.EVENT_LBUTTONDOWN:
        xstart, ystart = x, y
        # cv2.rectangle(img2,(x-32,y-32),(x+32,y+32),0,3)
    if event == cv2.EVENT_LBUTTONUP:
        if abs(xstart-x) < 64 or abs(ystart-y) < 64:
            aa = (x - 32, y - 32)
            bb = (x + 32, y + 32)
        else:
            aa = (xstart, ystart)
            bb = (x, y)

        cv2.rectangle(img2, aa, bb, 0, 3)
        data.append((*aa, *bb))
    else:
        return

    cv2.imshow('image', img2)


def slice_data(data, img):

    negatives = []

    for y in range(0, H//64*64, 64):
        for x in range(0, W//64*64, 64):
            negatives.append((x, y, x+ 64, y+64))

    for xa, ya, xb, yb in data:

        if xb < xa:
            xa, xb = xb, xa
        if yb < ya:
            ya, yb = yb, ya

        if (xb-xa) % 64 > 0:
            xb -= (xb-xa) % 64
        else:
            xb += 64 - (xb-xa) % 64

        negatives = [(a,b,c,d) for a,b,c,d in negatives if
            not (c >= xa and xb >= a and d >= ya and yb >= b)
        ]

        for y in range(ya, yb, 64):
            for x in range(xa, xb, 64):
                slice_img = img[y:y+64, x:x+64]
                save(slice_img, dir_positive)

    for xa, ya, xb, yb in negatives:
        slice_img = img[ya:yb, xa:xb]
        save(slice_img, dir_negative)

cv2.namedWindow('image')
cv2.setMouseCallback('image', mouse_events)

print("Press [ENTER] to confirm slices")
for file in os.listdir('./matury_mat/'):
    filenames = []
    filename = './matury_mat/' + file
    pages = convert_from_path(filename, 100)
    for page in pages[1:]:  # bez strony tytułowej
        ff = tempfile.TemporaryFile()
        filename = ff.name + '.png'
        page.save(filename, 'png')
        filenames.append(filename)

    if len(filenames) == 0:
        continue

    index = 0

    next_pdf = False


    while not next_pdf:
        filename = filenames[index]
        img = cv2.imread(filename, 0)
        H, W = img.shape

        if H != H0:
            H = H0
            W = int(W/H*H0)
            img = cv2.resize(img, (W, H))

        img2 = img.copy()

        cv2.imshow('image', img2)
        data = []
        while True:
            key = cv2.waitKeyEx()
            if key == -1:
                exit()
            if key == Keys.LEFT_ARROW.value and index > 0:
                index -= 1
                break
            if key == Keys.RIGHT_ARROW.value:
                if index < len(filenames) - 1:
                    index += 1
                    break
                else:
                    next_pdf = True
                    break

            if key == Keys.SPACE.value:
                next_pdf = True
                break
            if key == Keys.ENTER.value:
                print("Slicing...")
                slice_data(data, img)
                print("Slices complete")
cv2.destroyAllWindows()
