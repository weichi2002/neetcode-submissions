class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i+=1
        return -1

    def insertHead(self, val: int) -> None:
        temp = Node(val)
        temp.next = self.head.next
        self.head.next = temp        

        if not temp.next:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        #stop right before the index to remove
        while i < index and curr:
            curr = curr.next
            i+=1
        
        if curr and curr.next: #if the current stop is valid
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
        
    def getValues(self) -> List[int]:
        res = []
        curr = self.head.next
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res


class Node:

    def __init__(self, val, nextNode = None):
        self.val = val
        self.next = nextNode


    
        
