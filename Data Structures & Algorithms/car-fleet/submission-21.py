class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(p,s) for p,s in zip(position, speed)]

        cars.sort(reverse=True)

        stack = []
        for p, s in cars:
            time = (target - p) / s
            stack.append(time)

            #determine if the car is going to merge, if the car ahead is slower, we are going to collide and merge
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            
        return len(stack)

        