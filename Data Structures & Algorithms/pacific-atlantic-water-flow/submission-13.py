class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        #we reverse the dfs. We flow backward. Meaning that if the new > prev: we can flow
        #we use set to track what can be reached for pac and atl, and use intersection to solve
        pac = set()
        atl = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r,c, visit, prev):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visit or
                heights[r][c] < prev
                ):
                    return 
                
            visit.add((r,c))

            dfs(r+1,c,visit, heights[r][c])
            dfs(r-1,c,visit, heights[r][c])
            dfs(r,c+1,visit, heights[r][c])
            dfs(r,c-1,visit, heights[r][c])
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        return (list(pac & atl))







