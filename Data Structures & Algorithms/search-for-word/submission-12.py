class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #run a bfs from every position, cannot be repeated

        #visited = set()
        #bounded by the boundary


        #expected to generate a boolean

        #why dont scan every letter, and explore only if the first letter of the word matches
        ROWS, COLS = len(board), len(board[0])

        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r not in range(ROWS) or
               c not in range(COLS) or
               word[i] != board[r][c] or
               (r,c) in visited):
               
               return False

            visited.add((r,c))
            res = (dfs(r+1, c, i+1) or
                   dfs(r-1, c, i+1) or
                   dfs(r, c+1, i+1) or
                   dfs(r, c-1, i+1)
            )

            visited.remove((r,c))
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        
        return False


            
            
            
        