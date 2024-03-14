# Solution 1
# class Solution(object):
#     def generateMatrix(self, n):
#         """
#         :type n: int
#         :rtype: List[List[int]]
#         """
#         output = [[0 for _ in range(n)] for _ in range(n)]
#         startRow, endRow = 0, n-1
#         startCol, endCol = 0, n-1
        
#         input = 1

#         while startCol < endCol and startRow < endRow:
#             for j in range(startCol, endCol):
#                 output[startRow][j] = input
#                 input += 1
#             for i in range(startRow, endRow):
#                 output[i][endCol] = input
#                 input += 1
#             for j in range(endCol, startCol, -1):
#                 output[endRow][j] = input
#                 input += 1
#             for i in range(endRow, startRow, -1):
#                 output[i][startCol] = input
#                 input += 1
#             startCol += 1
#             startRow += 1
#             endCol -= 1
#             endRow -= 1
        
#         if startRow == endRow and startCol == endCol:
#             output[startRow][startCol] = input

#         elif startRow == endRow:
#             for j in range(startCol, endCol+1):
#                 output[startRow][j] = input
#                 input += 1
        
#         elif startCol == endCol:
#             for i in range(startRow, endRow+1):
#                 output[i][startCol] = input
#                 input += 1
            
#         return output

# Solution 2
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        output = [[0 for _ in range(n)] for _ in range(n)]
        upper_bound, lower_bound = 0, n-1
        left_bound, right_bound = 0, n-1
        
        input = 1

        while input <= n ** 2:
            if upper_bound <= lower_bound:
                for j in range(left_bound, right_bound+1):
                    output[upper_bound][j] = input
                    input += 1
                upper_bound += 1
            if right_bound >= left_bound:
                for i in range(upper_bound, lower_bound+1):
                    output[i][right_bound] = input
                    input += 1
                right_bound -= 1
            if lower_bound >= upper_bound:
                for j in range(right_bound, left_bound-1, -1):
                    output[lower_bound][j] = input
                    input += 1
                lower_bound -= 1
            if left_bound <= right_bound:
                for i in range(lower_bound, upper_bound-1, -1):
                    output[i][left_bound] = input
                    input += 1        
                left_bound += 1
        
        return output