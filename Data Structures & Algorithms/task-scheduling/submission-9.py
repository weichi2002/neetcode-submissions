class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        #if we process, we add it to a queue of minHeap, that is currTime + n
        #and then we go about processing it

        freq = Counter(tasks)
        maxHeap = [-cnt for cnt in freq.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() # pairs of [-cnt, idleTime]

        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1] #jump to the closest available time
            
            else:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
        