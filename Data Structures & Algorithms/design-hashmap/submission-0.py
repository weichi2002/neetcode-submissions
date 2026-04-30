class MyHashMap:

    def __init__(self):
        self.hashmap = ["$"] * 10000001
        

    def put(self, key: int, value: int) -> None:
        self.hashmap[key] = value
        

    def get(self, key: int) -> int:
        if self.hashmap[key] != "$":
            return self.hashmap[key]
        return -1
        

    def remove(self, key: int) -> None:
        if self.hashmap[key] != "$":
            self.hashmap[key] = "$"


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)