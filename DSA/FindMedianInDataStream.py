class MedianFinder(object):

    def __init__(self):
        self.data = []

    def addNum(self, num):
        self.data.append(num)

    def findMedian(self):
        self.data.sort()
        l = len(self.data)
        if l % 2 != 0:
            return self.data[l // 2]
        i1 = (l // 2) - 1
        i2 = l // 2
        return (self.data[i1] + self.data[i2]) / 2.0

# TC: O(nlogn)
# SC: O(n)
