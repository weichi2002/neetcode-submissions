class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        visit = set()
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        #add every gate to the the q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))

        def addCell(r,c):
            if (
                r < 0 or c < 0 or
                r == ROWS or c == COLS or
                (r,c) in visit or
                grid[r][c] == -1
            ):
                return
            q.append([r,c])
            visit.add((r,c))


        
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                addCell(r-1,c)
                addCell(r+1,c)
                addCell(r,c+1)
                addCell(r,c-1)
            distance +=1

        