class LRUCache:

    def __init__(self, capacity: int):
        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.capacity = capacity
        self.cache = {}
    
    def remove(self, node):
        l, r = node.prev, node.next
        l.next = r
        r.prev = l
    
    def insert(self, node):
        l = self.right.prev
        l.next = node
        node.prev = l
        node.next = self.right
        self.right.prev = node



    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        #check if the capcity is grrater than delete
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del(self.cache[lru.key])
        
class Node:

    def __init__(self, key, val):
        self.prev, self.next = None, None
        self.key = key
        self.val = val
