import cv2 as cv
import numpy as np


def start():
    readImage()


def readImage():

    img = cv.imread('Billie.jpg')

    stat = img.shape

    if len(stat) == 3:
        modifyPx(img)

    else:
        print("IMAGE CAN'T RELOAD")


def modifyPx(img):
    x = int(input("X: "))
    y = int(input("Y: "))
    z = int(input("COLOR ATTRIBUTES: "))

    cv.imshow("BEFORE ", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    px = img.item(x, y, z)
    print("IMAGE VALUE: ", x, y, z)
    print("PIXEL VALUE: ", px)

    img.itemset((x, y, z), 200)
    px = img.item(x, y, z)
    print("MODIFIED PIXEL VALUE: ", px)

    dimention(img)


def dimention(img):

    size = img.shape

    x = 1000
    y = 1000

    if size[0] > x and size [1] > y:
        print("INVALID IMAGE DIMENTION!!!!!")

    else:
        imageType(img)


def imageType(img):
    dtype = img.dtype
    print("IMAGE DATA TYPE: ", dtype)

    imagesize(img)


def imagesize(img):

    requiredsize = 1000000000
    size = img.size

    if size <= requiredsize:
        print("IMAGE SIZE VALIDATED!!!!!")
        cv.imshow("AFTER", img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    else:
        print("IMAGE SIZE INVALID!!!!")


start()
