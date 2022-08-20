class Solution:
    def findMaxForm(self, strs, m: int, n: int):
        len_n = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len_n + 1)]  # dp[i][j][k]前i个字母最多用到j个0和k个1的字母数量

        def countzerosandones(str):
            count = [0] * 2
            for ch in str:
                if ch == '0':
                    count[0] += 1
                else:
                    count[1] += 1
            return count

        for i in range(len_n):
            count = countzerosandones(strs[i])
            zeros = count[0]
            ones = count[1]
            for j in range(m + 1):
                for k in range(n + 1):
                    dp[i + 1][j][k] = dp[i][j][k]
                    if j >= zeros and k >= ones:
                        dp[i + 1][j][k] = max(dp[i][j][k], dp[i][j - zeros][k - ones] + 1)

        return dp[len_n][m][n]


if __name__ == '__main__':
    strs = ["10","0001","111001","1","0"]
    m = 5
    n = 3

    print(Solution().findMaxForm(strs,m,n))
