# Solution 1
# class Solution(object):
#     def rotate(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: None Do not return anything, modify matrix in-place instead.
#         """

#         n = len(matrix)
#         startCol = 0
#         endCol = n - 1

#         while startCol < endCol:
#             # matrix[i][j] should be moved to matrix[j][n-1-i]
#             # start with matrix[startRow][i] (startRow = startCol)
#             for i in range(startCol, endCol):
#                 temp1 = matrix[i][n-startCol-1]
#                 matrix[i][n-startCol-1] = matrix[startCol][i]
#                 temp2 = matrix[n-startCol-1][n-i-1]
#                 matrix[n-startCol-1][n-i-1] = temp1
#                 temp1 = matrix[n-i-1][startCol]
#                 matrix[n-i-1][startCol] = temp2
#                 matrix[startCol][i] = temp1
            
#             startCol += 1
#             endCol -= 1

# Solution 2
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            self.reverse(row)
        

    def reverse(self, row):
        left = 0
        right = len(row)-1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
        
