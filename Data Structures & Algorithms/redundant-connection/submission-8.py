class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # we use union find to solve this problem

        N = len(edges)
        size = [1] * (N+1) 
        par = [i for i in range(N+1)]

        # the goal is to build a graph and flatten tree where possible

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p

        # the first edge that we see is not connected is the solution
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            if size[p1] > size[p2]:
                par[p2] = p1
                size[p1] += size[p2]
            else:
                par[p1] = p2
                size[p2] += size[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]

                