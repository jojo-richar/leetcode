class Solution:
    # def maximalSquare(self, matrix):
    #     row = len(matrix)
    #     col = len(matrix[0])
    #     newmatrix = [[0 for _ in range(col)] for _ in range(row)]
    #     for i in range(row):
    #         newmatrix[i][0] = int(matrix[i][0])
    #     for i in range(row):
    #         for j in range(1, col):
    #             if int(matrix[i][j]) == 1:
    #                 newmatrix[i][j] = newmatrix[i][j - 1] + 1
    #             else:
    #                 newmatrix[i][j] = 0
    #
    #
    #     maxArea=0
    #     for i in range(row):
    #         for j in range(col):
    #             if newmatrix[i][j]>0:
    #                 height=1
    #                 k=i
    #                 minLength=  newmatrix[i][j]
    #                 while(newmatrix[k][j]>0 and k>=0):
    #                     minLength=min(minLength,newmatrix[k][j])
    #                     maxArea=max(maxArea,(min(height,minLength)**2))
    #                     height+=1
    #                     k-=1
    #
    #     return maxArea
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        row = len(matrix)
        col = len(matrix[0])
        maxside = 0
        dp = [[0 for _ in range(col + 1)] for _ in range(row + 1)]
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == "1":
                    dp[i + 1][j + 1] = min(dp[i +1][j], dp[i ][j ], dp[i][j + 1]) + 1
                    maxside = max(dp[i + 1][j + 1], maxside)

        return maxside * maxside



if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]

    print(Solution().maximalSquare(matrix))