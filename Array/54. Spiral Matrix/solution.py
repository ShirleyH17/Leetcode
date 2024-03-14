class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        n = len(matrix[0])
        output = []

        startCol, endCol = 0, n-1
        startRow, endRow = 0, m-1
        while startCol < endCol and startRow < endRow:
            for j in range(startCol, endCol):
                output.append(matrix[startRow][j])
            for i in range(startRow, endRow):
                output.append(matrix[i][endCol])
            for j in range(endCol, startCol, -1):
                output.append(matrix[endRow][j])
            for i in range(endRow, startRow, -1):
                output.append(matrix[i][startCol])
            startCol += 1
            startRow += 1
            endCol -= 1
            endRow -= 1
        
        if startRow == endRow and startCol == endCol:
            output.append(matrix[startRow][startCol])

        elif startRow == endRow:
            for j in range(startCol, endCol+1):
                output.append(matrix[startRow][j])
        
        elif startCol == endCol:
            for i in range(startRow, endRow+1):
                output.append(matrix[i][startCol])

        return output