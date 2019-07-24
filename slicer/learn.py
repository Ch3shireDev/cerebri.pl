import os
import cv2
import numpy
import tempfile
from pdf2image import convert_from_path
from sklearn.svm import LinearSVC
from sklearn.datasets import make_classification
import tkinter
import PIL.Image
import PIL.ImageTk
from time import time
import pickle

dir_positive = './data/positive/'
dir_negative = './data/negative/'

H0 = 1040

def compress(data):
    '''takes 64x64 array and returns 16x16'''
    data = data.reshape(16,4,16,4).mean(axis=(1,3))
    return data

positive = []
negative = []

for x in os.listdir(dir_positive):
    img = cv2.imread(dir_positive + x, 0)
    img = -1 + img/255*2
    img = compress(img)
    img = img.reshape((1, -1))
    positive.append(img[0])

for x in os.listdir(dir_negative):
    img = cv2.imread(dir_negative + x, 0)
    img = -1 + img/255*2
    img = compress(img)
    img = img.reshape((1, -1))
    negative.append(img[0])

try:
    file = open('clf.pkl', 'rb')
    clf = pickle.load(file)
    file.close()
    print("Loaded clf from file")
except:
    clf = LinearSVC(random_state=0, tol=1e-5, max_iter=1000000)
    print("Created new clf object")

N = len(positive)
M = len(negative)

print("Learning... (%d positive examples, %d negative examples)" % (N, M))

numpy.random.shuffle(positive)
numpy.random.shuffle(negative)

X = [x for x in positive[:N] + negative[:M]]
y = [1]*N + [0]*M

t1 = time()
clf.fit(X, y)
t2 = time()

file = open('clf.pkl', 'wb')
pickle.dump(clf, file)
file.close()

print(t2-t1)

print("Learning complete")

def cover_data(img):
    H, W = img.shape

    for y in range(0, H, 64):
        for x in range(0, W, 64):
            data = img[y:y+64, x:x+64]
            if data.shape != (64,64):
                continue
            data = -1 + data/255*2
            data = compress(data)
            data = data.reshape((1, -1))
            p = clf.predict([data[0]])
            if p[0] == 0:
                img[y:y+64, x:x+64] //= 2

    return img

path = "./matury_mat/"


cv2.namedWindow('image')

for file in os.listdir(path):
    filename = path+file
    pages = convert_from_path(filename, 100)
    for page in pages[1:]:
        ff = tempfile.TemporaryFile()
        filename = ff.name + '.png'
        ff.close()
        page.save(filename, 'png')
        
        img = cv2.imread(filename, 0)

        H, W = img.shape
        if H != H0:
            H = H0
            W = int(W/H*H0)
            img = cv2.resize(img, (W, H))

        if W%64 != 0:
            img = img[:, :W//64*64]

        img = cover_data(img)
        cv2.imshow('image', img)
        
        while True:
            key = cv2.waitKeyEx()
            if key == -1:
                break
