class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #process the most frequent letter to reduce wasting cooldown
        #count them and store the most frequent in a maxHeap 
        #put the cooldown in a queue
        #dont care about the letter itslef

        time = 0
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        cooldown = deque() #[-count, time + n]

        while maxHeap or cooldown:
            time += 1

            if not maxHeap:
                time = cooldown[0][1]
            
            else:
                remaining = 1 + heapq.heappop(maxHeap)
                if remaining != 0:
                    cooldown.append([remaining, time + n])
                
            if cooldown and cooldown[0][1] == time:
                heapq.heappush(maxHeap, cooldown.popleft()[0])


        return time