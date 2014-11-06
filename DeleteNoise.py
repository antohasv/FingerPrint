__author__ = 'anton'


class DeleteNoise:

    def __init__(self, branchPoints, endPoints):
        self.branchPoints = branchPoints
        self.endPoints = endPoints


    def removeDuplicates(self, points, tmp):
        arr1 = self.getUniqueArr(points, tmp)
        arr2 = self.getUniqueArr(tmp, points)
        return arr1 + arr2

    def getUniqueArr(self, points, tmp):
        uniqueArr = []
        for i in points:
            flag = True
            for j in tmp:
                if i == j:
                    flag = False

            if flag:
                uniqueArr.append(i)
        return uniqueArr


    def execute(self):
        tmpEnd = []
        tmpBranch = []

        for i in self.endPoints:
            x = range(i[0] - 5, i[0] + 5)
            y = range(i[1] - 5, i[1] + 5)
            for j in self.branchPoints:
                if j[0] in x and j[1] in y:
                    tmpEnd.append(i)
                    tmpBranch.append(j)

        return (self.removeDuplicates(self.branchPoints, tmpBranch), self.removeDuplicates(self.endPoints, tmpEnd))