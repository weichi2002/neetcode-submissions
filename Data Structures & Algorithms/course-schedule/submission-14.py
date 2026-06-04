class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #detect if there are any cycles, if there are return False, cycle means that we cant finish because prereqs contradict each other


        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        path = set()

        def dfs(crs):
            #base case
            if preMap[crs] == []:
                return True
            if crs in path:
                return False
            
            path.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            
            path.remove(crs)
            preMap[crs] = []
            return True

        for n in range(numCourses):
            if not dfs(n): return False
        
        return True



        

