class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)

        #process the most recurring, we camn use maxHeap

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        cooldown = deque() #[-count, time]
        
        time = 0

        while maxHeap or cooldown:

            time += 1

            if not maxHeap:
                time = cooldown[0][1]
            
            else:
                remaining = 1 + heapq.heappop(maxHeap)
                if remaining != 0:
                    cooldown.append([remaining, time + n])
            
            if cooldown and cooldown[0][1] == time: #time is up
                heapq.heappush(maxHeap, cooldown.popleft()[0])



        return time
        