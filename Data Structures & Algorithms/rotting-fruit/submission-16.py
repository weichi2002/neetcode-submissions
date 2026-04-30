class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        

        q = deque() #append the coordinates
        time = 0
        fresh = 0

        #we use bfs to get the min time, because dfs we have to explore every rot and compare the minuimum. With bfs we can track all of them at once
        #mutli source 
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))

        directions = [[1, 0], [-1,0], [0, 1], [0,-1]]
        
        while fresh > 0 and q:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (row in range(ROWS) and
                        col in range(COLS) and
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append((row, col))
                        fresh -= 1
            
            time += 1



        return time if fresh == 0 else -1


