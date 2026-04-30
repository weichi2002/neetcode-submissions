class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #process the most occuring task first to minimize cool down
        #we dont really care about the letter itself

        count = Counter(tasks)

        time = 0

        #naive approach would be to have an list of task and sort every time (n log n)
        #maxHeap (log n)

        #we would also need a cooldown q

        cooldown = deque() #[remaining, time until can be picked up, time + n ]

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        while maxHeap or cooldown:
            time += 1

            if not maxHeap:
                time = cooldown[0][1]
            
            else:
                remaining = 1 + heapq.heappop(maxHeap)
                if remaining != 0:
                    cooldown.append([remaining, time + n])
            
            #check for completed cooldown
            if cooldown and time == cooldown[0][1]:
                heapq.heappush(maxHeap, cooldown.popleft()[0])

        return time




