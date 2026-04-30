class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            if s == "/":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(int(val1/val2))

            elif s == "*":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 * val2)
            elif s == "+":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1 + val2)
            elif s == "-":
                val2 = stack.pop()
                val1 = stack.pop()
                stack.append(val1-val2)
            else:
                stack.append(int(s))
        
        return stack[0]