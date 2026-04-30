class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for p in s:
            if p in pairs:
                stack.append(pairs[p])
            else:
                if stack and stack[-1] == p:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0