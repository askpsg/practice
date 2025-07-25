class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.data = matrix
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(cols):
                if row > 0 and col > 0:
                    self.data[row][col] += (
                        self.data[row - 1][col]
                         + self.data[row][col - 1]
                         - self.data[row - 1][col - 1]
                    )
                elif col > 0:
                    self.data[row][col] += self.data[row][col - 1]
                elif row > 0:
                    self.data[row][col] += self.data[row - 1][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.data[row2][col2]
        if row1 > 0:
            ans -= self.data[row1 - 1][col2]
        if col1 > 0:
            ans -= self.data[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            ans += self.data[row1 - 1][col1 - 1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)