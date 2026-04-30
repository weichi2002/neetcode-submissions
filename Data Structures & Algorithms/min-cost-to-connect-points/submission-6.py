class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)

        adj = defaultdict(list)

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minH = [[0,0]]

        while len(visit) < N:
            cost, pt = heapq.heappop(minH)

            if pt in visit:
                continue

            visit.add(pt)
            res += cost

            for neighborCost, neighbor in adj[pt]:
                if neighbor not in visit:
                    heapq.heappush(minH, [neighborCost, neighbor])
        
        return res




        