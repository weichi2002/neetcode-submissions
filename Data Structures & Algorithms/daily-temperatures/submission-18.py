class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        #we can use stack to keep track of the highest element, append the element if its lower, pop the stack and update the index when its higher
        stack = [] #[t, index]

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                #pop the stack
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI

            
            stack.append([t,i])
        
        return res