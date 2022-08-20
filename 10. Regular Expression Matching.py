class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        def Match(i, j):  # 表示第i个字母，第j个字母
            if i == 0:
                return False
            if p[j - 1] == '.':
                return True
            return s[i - 1] == p[j - 1]

        for i in range(m + 1):
            for j in range(1, n + 1):  # i是空集还可能能配对上，j是空集绝对不可能配对上非空的i
                # if (i<0) +(j<0) == 1:
                #     dp[i][j]=False
                #     continue
                # if i<0 and j<0:
                #     dp[i][j]=True
                #     continue
                if p[j - 1] == '*':
                    # if Match(i,j-1):  #s的第i个和p的第j-1个匹配
                    #     dp[i][j] |= dp[i-1][j]
                    # else:
                    #     dp[i][j] |= dp[i][j-2]
                    # dp[i][j]|= dp[i][j-2]    #如匹配a和ab*a*，匹配aa和ab*a*,这里的或计算和逻辑是有意义的，无非就是换了种形式
                    # if Match(i,j-1):
                    #     dp[i][j]|= dp[i-1][j]
                    if Match(i, j - 1):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 2]
                    else:
                        dp[i][j] = dp[i][j - 2]
                else:
                    if Match(i, j):
                        dp[i][j] = dp[i - 1][j - 1]
                    else:
                        dp[i][j] = False
        return dp[m][n]


A = Solution()
print(A.isMatch('aaa', 'ab*a*c*a'))
