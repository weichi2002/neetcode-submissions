class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        #the brute force method is to generate all possible combinations and eliminate working one. This will be 2^N work. We would probably run the valid parenthesis alogrithm to validsat this

        #we can use smart backtracking, stop when we needed to solve this problem

        #we have 2 variables that we are interested in, close and open. Condition is always true that close < open

        #when we have open == close == n, we can stop
        curr = []

        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(curr))
                return
            
            if openN < n:
                curr.append("(")
                backtrack(openN + 1, closeN)
                curr.pop()
            
            if closeN < openN:
                curr.append(")")
                backtrack(openN, closeN + 1)
                curr.pop()


        backtrack(0, 0)
        return res