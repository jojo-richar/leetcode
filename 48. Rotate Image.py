class Solution:
    def rotate(self, matrix) :
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 水平翻转：
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n-1- i][j], matrix[i][j]

        # 对角线翻转：
        for i in range(n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        pass
                
Solution().rotate([[1,2,3],[4,5,6],[7,8,9]])