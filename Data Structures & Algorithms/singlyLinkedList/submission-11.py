class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head

    
    def get(self, index: int) -> int:
        curr = self.head.next
        i= 0
        while curr:
            if i == index:
                return curr.val
            i+=1
            curr = curr.next

        return -1
        

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next:
            self.tail = newNode

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        #we want to stop at the index before
        while curr and i < index:
            curr = curr.next
            i+=1
        
        #if the next is removable
        if curr and curr.next:
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
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 
