class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        #use stack to keep track of the highest seen, if the current beats the highest, we pop the stack until it doesnt beat anymore, else we just add to the stack
        stack = [] #[temp, index]

        for i, t in enumerate(temperatures): #gives us access to index, and temp
            while stack and stack[-1][0] < t:
                #pop from the stack
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append([t,i])

        return res