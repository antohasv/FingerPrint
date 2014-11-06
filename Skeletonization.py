__author__ = 'anton'

class Skeletonization:

    def __init__(self, binaryImg):
        self.img = binaryImg
        self.n = len(binaryImg)
        self.m = len(binaryImg[0])

    def getSkeletonImg(self):
        count = 1
        while count != 0:
            count = self.deleteExtremeElements()
            if count:
                self.deleteFringeElements()
        return self.img

    def deleteExtremeElements(self):
        count = 0
        for i in xrange(1, self.m - 1):
            for j in xrange(1, self.n - 1):
                if not self.img[j][i] and self.deleteExtremeElementsFromTable(j, i):
                    self.img[j][i] = 1
                    count += 1
        return count

    def deleteFringeElements(self):
        for i in xrange(1, self.m - 1):
            for j in xrange(1, self.n - 1):
                if not self.img[j][i] and self.deleteFringeElementsFromTable(j, i):
                    self.img[j][i] = 1

    def getArrayByIndex(self, arr, arrIndex):
        template = []
        for i in arrIndex:
            template.append(arr[i])
        return template

    def checkTemplate(self, arr):
        t123457 = [1,1,0,0,1,0]
        t013457 = [1,1,1,0,0,0]
        t134567 = [0,1,0,0,1,1]
        t134578 = [0,0,0,1,1,1]
        t0123457 = [1,1,1,0,0,0,0]
        t0134567 = [1,0,1,0,0,1,0]
        t1345678 = [0,0,0,0,1,1,1]
        t1234578 = [0,1,0,0,1,0,1]

        if t123457 == self.getArrayByIndex(arr, (1, 2, 3, 4, 5, 6)):
            return True

        if t013457 == self.getArrayByIndex(arr, (0, 1, 3, 4, 5, 7)):
            return True

        if t134567 == self.getArrayByIndex(arr, (1, 3, 4, 5, 6, 7)):
            return True

        if t134578 == self.getArrayByIndex(arr, (1, 3, 4, 5, 7, 8)):
            return True

        if t0123457 == self.getArrayByIndex(arr, (0, 1, 2, 3, 4, 5, 7)):
            return True

        if t1345678 == self.getArrayByIndex(arr, (1, 3, 4, 5, 6, 7, 8)):
            return True

        if t0134567 == self.getArrayByIndex(arr, (0, 1, 3, 4, 5, 6, 7)):
            return True

        if t1234578 == self.getArrayByIndex(arr, (1, 2, 3, 4, 5, 7, 8)):
            return True

    def checkOnFringe(self, arr):
        fringeTemplate = [
            [1,1,1,1,0,1,1,1,1],

           [1,1,1,1,0,1,1,0,0],
           [1,1,1,0,0,1,0,1,1],
           [0,0,1,1,0,1,1,1,1],
           [1,1,0,1,0,0,1,1,1],

           [1,1,1,1,0,1,0,0,1],
           [0,1,1,0,0,1,1,1,1],
           [1,0,0,1,0,1,1,1,1],
           [1,1,1,1,0,0,1,1,0],

           [1,1,1,1,0,1,0,0,0],
           [0,1,1,0,0,1,0,1,1],
           [0,0,0,1,0,1,1,1,1],
           [1,1,0,1,0,0,1,1,0]]

        for i in fringeTemplate:
            if i == arr:
                return True

    def getTemplate3x3(self, x, y):
        arrBlock = [] #Matrix 3x3
        for i in xrange(y - 1, y + 2):
            for j in xrange(x - 1, x + 2):
                arrBlock.append(self.img[j][i])
        return arrBlock

    def deleteExtremeElementsFromTable(self, x, y):
        arrBlock = self.getTemplate3x3(x, y)
        return self.checkTemplate(arrBlock)

    def deleteFringeElementsFromTable(self, x, y):
        arrBlock = self.getTemplate3x3(x, y)
        return self.checkOnFringe(arrBlock)
