class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c):

            if(
                r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O"
            ):  return 

            board[r][c] = "T"

            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)


        for r in range(ROWS):
            for c in range(COLS):
                onTheBorder = (c in [0, COLS-1] or r in [0, ROWS-1])
                if onTheBorder and board[r][c] == "O":
                    dfs(r,c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"








        