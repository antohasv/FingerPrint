__author__ = 'anton'


class ExtractPoints:

    def __init__(self, skeletonArr):
        self.img = skeletonArr
        self.n = len(skeletonArr)
        self.m = len(skeletonArr[0])

        self.branchPoints = []
        self.endPoints = []


    def getCountOfBlackPoint(self, x, y):
        count = 0
        for i in range(x - 1, x + 2):
            for j in range(y - 1, y + 2):
                if self.img[i][j] == 0:
                    count += 1
        return count - 1

    def getBranchAndEndPoints(self):
        for i in range(1, self.n - 2):
            for j in range(1, self.m - 2):
                if self.img[i][j]:
                    continue
                nBlackPoint = self.getCountOfBlackPoint(i, j)
                if nBlackPoint == 1:
                    self.endPoints.append((i, j))
                if nBlackPoint == 3:
                    self.branchPoints.append((i, j))
        return (self.branchPoints, self.endPoints)