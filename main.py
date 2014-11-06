# -*- coding: utf-8 -*-
__author__ = 'anton'

from PIL import Image
from Binarization import Binarization
from Skeletonization import Skeletonization
from ExtractPoints import ExtractPoints
from DeleteNoise import DeleteNoise

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

    #binaryAlg = Binarization(img)
    #binaryImg = binaryAlg.getBinaryImg()
    #skeletonAlg = Skeletonization(binaryImg)
    #print(skeletonAlg.getSkeletonImg())

    skeletonResult = Skeletonization.defSkeletonResult
    for i in range(len(skeletonResult)):
        for j in range(len(skeletonResult[0])):
            if (skeletonResult[i][j] == 1):
                skeletonResult[i][j] = 200
    #showImage(skeletonResult)

    extractPoints = ExtractPoints(skeletonResult)
    extractPoints.getBranchAndEndPoints()

    deleteNoise = DeleteNoise(extractPoints.branchPoints, extractPoints.endPoints)
    deleteNoise.execute()


if __name__ == "__main__":
    main()