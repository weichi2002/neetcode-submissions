class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0]) 
        q = collections.deque()
        fresh = 0
        time = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1

        directions = [[0, 1], [0,-1], [1, 0], [-1, 0]]
        while fresh > 0 and q:
            for i in range(len(q)):
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
                        q.append([row, col])
            time += 1

        return time if fresh == 0 else -1 
        