class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        #initalize with extra row and col of zero first to add padding
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.mat = [[0] * (COLS+1) for r in range(ROWS+1)]

        #you dont iterate rows+1 b/c then original will go out of bound, so you shift one in custom array to compromise
        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.mat[r][c+1]
                self.mat[r+1][c+1] = prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1 = row1+1
        r2 = row2+1
        c1 = col1+1
        c2 = col2+1

        bottomRight = self.mat[r2][c2]
        left = self.mat[r2][c1-1]
        above = self.mat[r1-1][c2]
        overlap = self.mat[r1-1][c1-1]

        return bottomRight + overlap - left -above

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)