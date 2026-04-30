class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #start this problem by visualizing it on a graph
        #we plot on the lines the, the slope is the speed, and position is y axis I guess
        #if they intersect, we merge

        #we can do naively by simulating by the speed forward. direction, but this introduces complexity when its hard to determine the final car speed as multiple merges can happen.
        #but one thing we do know is that the car can never pass the car ahead, so we should approach this by reverse()
        
        pairs = [(p,s) for p,s in zip(position, speed)]
        pairs.sort(reverse=True)

        #we calculate the time to see if they will collide, they we use stack to keep track the distinct speed.
        #the logic is that when car becomes fast (by time) enough to merge, we pop the car fleet speed. At the end, we 
        #return the number of elements in the stack. this tells us the number of fleets

        stack = [] #[]
        for p, s in pairs:
            time = (target-p)/s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)




