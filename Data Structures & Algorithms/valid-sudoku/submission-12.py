class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #we should use set to track dupes
        #they keys should be row
        #col and squares
        #we can figure out the square number but doing r//3, c//3
        #use dicionary to track positions as key, and set as value to track dupes
        colSet = defaultdict(set)
        rowSet = defaultdict(set)
        squareSet = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": continue

                if (
                    board[r][c] in colSet[c] or
                    board[r][c] in rowSet[r] or
                    board[r][c] in squareSet[(r//3, c//3)]
                ):
                    return False
                
                colSet[c].add(board[r][c])
                rowSet[r].add(board[r][c])
                squareSet[(r//3, c//3)].add(board[r][c])
        
        return True
        

