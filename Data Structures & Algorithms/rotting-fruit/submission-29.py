class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #multi source bfs, we collect rotten and start bfs
        #count all the number of fresh oranges, want it to be zero at the end else -1

        time = 0
        fresh = 0
        q = deque()

        ROWS = len(grid)
        COLS = len(grid[0])

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))


        directions = [[0,1], [0,-1], [1,0], [-1,0]]

        while fresh != 0 and q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if (
                        row in range(ROWS) and
                        col in range(COLS) and
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        fresh -= 1
                        q.append((row, col))

            time += 1



        return time if fresh == 0 else -1
        