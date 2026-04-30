class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in seen: return False
                seen.add(board[i][j])

        #col
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] == ".": continue
                if board[j][i] in seen: return False
                seen.add(board[j][i])

        #grids
        for grid in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    row = grid//3 * 3 + i
                    col = grid % 3 * 3 + j

                    if board[row][col] in seen: return False
                    if board[row][col] == ".": continue
                    seen.add(board[row][col])
        
        return True
        
        
        