class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #have to find the root where the course starts

        prereqs = [0] * numCourses

        adj = [[] for i in range(numCourses)]

        for src, dst in prerequisites:
            prereqs[dst] += 1
            adj[src].append(dst)
        


        q = deque()
        for n in range(numCourses):
            if prereqs[n] == 0:
                q.append(n)
        
        finish = 0

        while q:
            node = q.popleft()
            finish += 1
            for nei in adj[node]:
                prereqs[nei] -= 1
                if prereqs[nei] == 0:
                    q.append(nei)

        return finish == numCourses