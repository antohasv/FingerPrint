__author__ = 'anton'

class PointsMatcher:

    #firstArr - (branchPoints, endPoints)
    def __init__(self, firstArr, secondArr):
        self.fistArr = firstArr
        self.secondArr = secondArr
        self.all = 0
        self.match = 0

    def matcher(self, fPoints, sPoints):
        for i in sPoints:
            x = range(i[0] - 15, i[0] + 15)
            y = range(i[0] - 15, i[1] + 15)
            all += 1
            for j in fPoints:
                if j[0] in x and j[1] in y:
                    self.match += 1
                    break

    def execute(self):
        self.matcher(self.fistArr[0], self.secondArr[0])
        self.matcher(self.fistArr[1], self.secondArr[1])
        return (self.all, self.match)