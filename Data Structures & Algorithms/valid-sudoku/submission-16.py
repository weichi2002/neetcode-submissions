class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        #divide this up into a set
        #we can process the grid 

        

        ROWS = len(board)
        COLS = len(board[0])

        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == ".": continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in grids[(r//3, c//3)]
                ): 
                    return False
                
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                grids[(r//3, c//3)].add(board[r][c])
        
        return True
                
            
