class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.timeMap[key]

        l = 0
        r = len(values)-1

        while l <= r:
            m = (l+r)//2
            if values[m][0] <= timestamp:
                res = values[m][1]
                l = m + 1 
            else:
                r = m - 1
        return res
        
