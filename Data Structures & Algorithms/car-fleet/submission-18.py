class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #intutition.

        #try to simulate the cars running at differnet speed and catching up to each other
        #but the problem is the fleet is going to merge and make it complicated
        #maybe we should sort by the postion in the array. See whos the closest./
        #the closest car


        #use some sort of dictionary to track which fleet ur at
    
        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i]))
        
        pairs.sort(reverse=True)
        stack = []

        for p, s in pairs:
            stack.append((target-p)/ s)

            if len(stack) >= 2 and stack[-1] <= stack[-2]: #need 2 to compare, and the current top stack is slower. so we are going to merge
                stack.pop()

        return len(stack)