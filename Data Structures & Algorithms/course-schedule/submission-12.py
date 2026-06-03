class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        preMap = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        
        #core idea is to detect if there are any cycles

        path = set()

        def dfs(crs):
            #base case 
            #no prereq
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
            if not dfs(n):
                return False
        
        return True
        





