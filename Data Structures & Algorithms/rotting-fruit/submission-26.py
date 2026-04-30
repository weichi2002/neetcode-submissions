class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        #multisource bfs
        #we know its reachable if we the number of fresh fruit at the end equals 0

        #traverse thru the grid
        # add the fresh fruit
        #start the rotting process via bfs
        # check at the end if fresh == 0 or return -1

        fresh = 0
        time = 0 
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()

        #add the fresh fruit here
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r,c))
        
        directions = [[0,1], [0,-1], [1,0], [-1,0]]
        while fresh != 0 and q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()

                for dx, dy in directions:
                    row = r + dx
                    col = c + dy

                    if (
                        row in range(ROWS) and
                        col in range(COLS) and
                        grid[row][col] == 1
                    ):
                        fresh -= 1
                        grid[row][col] = 2 
                        q.append((row, col))
            
            time += 1


        return time if fresh == 0 else -1
