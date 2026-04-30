# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        turtle, rabbit = head, head

        while rabbit and rabbit.next:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if turtle == rabbit:
                return True
        
        return False
        