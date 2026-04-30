class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

        #head is just a dummy node
        #tail is actually pointing to the last node


class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
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
        
        #insert into an empty list, must also update our tail
        if not temp.next:
            self.tail = temp

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0

        while curr and i < index:
            i+=1
            curr = curr.next
        
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
        
