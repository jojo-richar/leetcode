class Solution:
    def minPathSum(self, grid):
        m=len(grid)
        n=len(grid[0])
        dp= [n*[0] for _ in range(m)]
        temprow0=0
        for i in range(n):
            dp[0][i]=temprow0+grid[0][i]
            temprow0=temprow0+grid[0][i]
        tempcol0=0
        for i in range(m):
            dp[i][0]=tempcol0+grid[i][0]
            tempcol0=tempcol0+grid[i][0]

        for a in range(1,m):
            for b in range(1,n):
                dp[a][b]=min((dp[a-1][b]+grid[a][b]),(dp[a][b-1]+grid[a][b]))

        return dp[m-1][n-1]
 

if __name__== '__main__':

    print(Solution().minPathSum( [[1,3,1],[1,5,1],[4,2,1]]))