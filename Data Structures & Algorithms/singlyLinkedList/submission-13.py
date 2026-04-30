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
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if not newNode.next: #if its an empty list, we want to update the tail
            self.tail = newNode
        

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        self.tail.next = newNode
        self.tail = self.tail.next
        

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while curr and i < index:
            curr = curr.next
            i+=1
        
        if curr and curr.next:
            #if we remove tail, we need to udpate it 
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True

        return False


    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        
        return res
        
class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
