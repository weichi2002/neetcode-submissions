class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0, 0)
    

        self.head.next = self.tail
        self.tail.prev = self.head
        
    
    def insert(self, node):
        #we want to insert at the head
  
        nxt = self.head.next
        prev = self.head


        node.next = nxt
        node.prev = prev

        prev.next = node
        nxt.prev = node
        

    def remove(self, node):
        prev = node.prev
        nxt = node.next

        nxt.prev = prev
        prev.next = nxt


    def get(self, key: int) -> int:

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1
        
        
    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            #delete the lru
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
    
        


class Node:

    def __init__(self, key, val, next = None, prev = None):
        self.key = key
        self.val = val
