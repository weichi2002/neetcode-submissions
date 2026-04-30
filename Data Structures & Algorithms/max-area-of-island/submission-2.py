class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        maxArea = 0

        def dfs(r,c):

            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                grid[r][c] != 1
            ):
                return 0
            
            #if it didnt hit the base case, we know we found an isalnd
            grid[r][c] = 0

            return (
                1 + 
                dfs(r+1,c) +
                dfs(r-1,c) +
                dfs(r,c+1) +
                dfs(r,c-1) 
            )

        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, dfs(r,c))

        return maxArea
        