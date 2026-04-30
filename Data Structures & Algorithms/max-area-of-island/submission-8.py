class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        def dfs(r,c): #wwnat to return the area of an island here

            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != 1
            ):
                return 0

            grid[r][c] = 0 #mark as visited
            area = 1

            directions = [(0,1), (0,-1), (1,0), (-1,0)]

            for dr, dc in directions:
                area += dfs(r+dr, c+dc)
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r,c))

        return res