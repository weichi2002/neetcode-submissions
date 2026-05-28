class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #fill the land of the nearest treasure chest
        #multi source bfs from the treasure chest
        #time to mark the distance itereation
        #modify in place

        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        
        
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        while q:
            time += 1
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (
                        row not in range(ROWS) or
                        col not in range(COLS) or
                        grid[row][col] != 2147483647
                    ):
                        continue

                    grid[row][col] = time
                    q.append((row, col))
                




        
        