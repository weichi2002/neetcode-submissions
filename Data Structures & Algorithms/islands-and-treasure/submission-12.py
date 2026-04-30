class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # we are intersted in the shortest distance possible from a cell to a treasure chest.
        # for that, we should probably use bfs to explore layer by layer
        # we can use the grid with the known treasure chest and flow out to uknown

        q = deque() #(r,c)
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def addCell(r,c):
            if (
                r not in range(ROWS) or
                c not in range(COLS) or
                (r,c) in visited or
                grid[r][c] == -1
            ):
                return 
            
            visited.add((r,c))
            q.append([r,c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))

       
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist      
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)

            dist += 1          


                

            


            
            
                

            
            


        


                


        
        