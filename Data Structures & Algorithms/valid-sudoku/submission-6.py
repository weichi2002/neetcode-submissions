class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] == ".": continue
                if board[i][j] in seen: return False
                seen.add(board[i][j])

        for i in range(9):
                seen = set()
                for j in range(9):
                    if board[j][i] == ".": continue
                    if board[j][i] in seen: return False
                    seen.add(board[j][i])
                

        for grid in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    col = grid//3 * 3 + i
                    row = grid%3 * 3 + j
                    if board[row][col] == ".": continue
                    if board[row][col] in seen:
                        return False
                    seen.add(board[row][col])

        return True

        
        