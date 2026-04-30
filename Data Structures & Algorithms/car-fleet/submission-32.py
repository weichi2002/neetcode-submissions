class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        #sort by positions first, because cars cant pass the cars in fornt, this reduces the complexity
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        stack = []
        #we are intestesd in calcualting the time, if the time is shorter we know that the car would meet and would merge into one fleet
        for p, s in pairs:
            time = (target-p) / s
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)        