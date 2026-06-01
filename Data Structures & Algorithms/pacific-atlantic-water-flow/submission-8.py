class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #we want to know what cell can flow both to pacific and atlantic
        #equal or lower

        ROWS = len(heights)
        COLS = len(heights[0])

        pac, atl = set(), set()

        #we know its pacific when r = 0 or c = 0
        # we know its atlantic when r = len(ROWS) and c = len(COLS)

        def dfs(r, c, visit, prevHeight):
            if ((r,c) in visit or
                r not in range(ROWS) or
                c not in range(COLS) or
                heights[r][c] < prevHeight
                ):

                return 

            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])


        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS-1])

        return list(pac & atl)
        

 