class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        self.sum = [[0 for _ in range(n)] for _ in range(m)]
        # self.sum[i][j] will calculate sumRegion[0, 0, i-1, j-1]
        for i in range(1, m):
            for j in range(1, n):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] -self.sum[i-1][j-1] + matrix[i-1][j-1]
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: 0
        :type col2: int
        :rtype: int
        """
        output = self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1] + self.sum[row1][col1]
        return output


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)