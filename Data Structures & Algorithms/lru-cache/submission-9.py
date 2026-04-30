class LRUCache:


    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left


    def addToRight(self, node):
        left = self.right.prev
        left.next = node
        node.prev = left
        node.next = self.right
        self.right.prev = node
        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.addToRight(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.addToRight(self.cache[key])
        

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del(self.cache[lru.key])

        
class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.val = val
        self.key = key