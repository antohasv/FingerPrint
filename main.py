# -*- coding: utf-8 -*-
__author__ = 'anton'

from PIL import Image
from Binarization import Binarization
from Skeletonization import Skeletonization

def getImage():
    imagePath = "../img/img1.png"
    return Image.open(imagePath)

def showImage(bImg):
    img = Image.new( 'RGB', (len(bImg), len(bImg[0])), "black")# create a new black image
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            val = bImg[i][j]
            pixels[i, j] = (val, val, val) # set the colour accordingly
    img.show()

def main():
    img = getImage()
    img.show()

    binaryAlg = Binarization(img)
    binaryImg = binaryAlg.getBinaryImg()
    showImage(binaryImg)

    #skeletonAlg = Skeletonization(binaryImg)
    #print(skeletonAlg.getSkeletonImg())

    pass

if __name__ == "__main__":
    main()