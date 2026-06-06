class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #the intuition is to build a for preMap that stores all the prerequisites
        # we are trying to detect if there is a cycle

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        #we are detecting if there is a cycle
        path = set()
        def dfs(crs):
            if crs in path:
                return False
            
            if preMap[crs] == []:
                return True
            
            path.add(crs)
            for p in preMap[crs]:
                if not dfs(p): return False

            path.remove(crs)
            preMap[crs] = []

            return True
           
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True

        
        




