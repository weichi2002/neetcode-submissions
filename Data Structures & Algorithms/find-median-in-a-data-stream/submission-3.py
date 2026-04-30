class MedianFinder:

    def __init__(self):
        self.array = []
        

    def addNum(self, num: int) -> None:
        self.array.append(num)

    def findMedian(self) -> float:
        self.array.sort()
        n = len(self.array)
        middle = n//2
        
        if n % 2 == 1:
            return self.array[middle]
        else:
            return (self.array[middle] + self.array[middle-1])/2

        
        