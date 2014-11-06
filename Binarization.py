__author__ = 'anton'

class Binarization:

    def __init__(self, img):
        self.img = img

    def getBinaryImg(self):
        binaryImg = []
        for i in xrange(self.img.size[0]):
            tmp = []
            for j in xrange(self.img.size[1]):
                pixel = self.img.getpixel((i, j))
                p = pixel[0]
                if p > 128:
                    p = 1
                else:
                    p = 200
                tmp.append(p)
            binaryImg.append(tmp)
        return binaryImg