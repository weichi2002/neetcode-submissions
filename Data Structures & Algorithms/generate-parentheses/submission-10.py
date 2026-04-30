class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #how do we brute force this. At every index, there is one decision to end or not given if it is not the firs tone

        stack = []
        res = []


        def backtrack(open, close):
            if open == close == n:
                res.append("".join(stack))
                return
            
            if open < n:
                stack.append("(")
                backtrack(open + 1, close)
                stack.pop()
            
            if close < open:
                stack.append(")")
                backtrack(open, close + 1)
                stack.pop()

        backtrack(0, 0)
        return res