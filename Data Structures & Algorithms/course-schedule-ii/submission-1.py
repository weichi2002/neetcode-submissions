class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        res = []
        preMap = {i: [] for i in range(numCourses)}
        visit = set()
        cycle = set()

        #a course has three possible states: visited, visiting, unvisited


        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in cycle: return False
            if crs in visit: return True
            
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)
        
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res


            

        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res


