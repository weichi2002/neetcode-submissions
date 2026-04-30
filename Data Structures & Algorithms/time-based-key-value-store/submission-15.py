class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        #using naive approach
        res = ""
        values = self.timeMap[key]

        for value in values:
            if value[0] <= timestamp:
                res = value[1]

        return res
        
