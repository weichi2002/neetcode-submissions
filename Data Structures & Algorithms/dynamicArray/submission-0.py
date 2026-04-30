class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.array = [] * capacity


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        self.size += 1
        if len(self.array) == self.capacity:
            self.resize()
        self.array.append(n)


    def popback(self) -> int:
        self.size -= 1
        return self.array.pop()
 

    def resize(self) -> None:
        self.capacity *= 2
        self.array.extend([] * self.capacity)

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity
