class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        N = len(edges)

        #every node is the parent of itself
        par = [i for i in range(N+1)]

        size = [1] * (N+1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False
            
            if size[p1] > size[p2]:
                size[p1] += size[p2]
                par[p2] = p1
            
            else:
                size[p2] += size[p1]
                par[p1] = p2
            
            return True
        
        for e1, e2 in edges:
            if not union(e1, e2):
                return [e1, e2]
        







