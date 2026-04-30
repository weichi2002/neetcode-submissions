from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0

        # Step 1: Collect all initially rotten oranges and count fresh oranges
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1  # Count fresh oranges

        # If there are no fresh oranges, return 0 immediately
        if fresh == 0:
            return 0

        # Step 2: BFS to spread rotting
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        grid[nr][nc] = 2  # Mark as rotten
                        fresh -= 1  # Reduce count of fresh oranges
                        q.append((nr, nc))
            time += 1  # Increase time after each level of BFS

        # Step 3: If fresh oranges remain, return -1
        return time - 1 if fresh == 0 else -1
