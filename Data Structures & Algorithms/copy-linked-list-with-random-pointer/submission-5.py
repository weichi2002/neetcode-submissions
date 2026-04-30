"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {None: None}

        curr = head
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head
        while curr:
            copy = d[curr]
            copy.next = d[curr.next]
            copy.random = d[curr.random]
            curr = curr.next

    

        return d[head]