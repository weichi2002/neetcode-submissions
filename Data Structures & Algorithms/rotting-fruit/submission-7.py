class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #lets apply multisource bfs
        ROWS = len(grid)
        COLS = len(grid[0])
        q = deque()
        fresh  = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[0,1], [0,-1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r,c = q.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (
                        row in range(len(grid)) and
                        col in range(len(grid[0])) and
                        grid[row][col] == 1
                    ):
                        grid[row][col] = 2
                        q.append([row,col])
                        fresh -= 1
            time += 1

        return time if fresh == 0 else - 1       