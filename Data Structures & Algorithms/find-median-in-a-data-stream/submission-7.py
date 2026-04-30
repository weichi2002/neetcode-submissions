class MedianFinder:

    def __init__(self):
        self.array = []

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        
        n = len(self.array)
        self.array.sort()
        mid = n//2

        if n % 2 == 1:
            return self.array[mid]
        else:
            return (self.array[mid] + self.array[mid-1])/2.0
        