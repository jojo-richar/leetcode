class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n<2:
            return 0

        dp=[0 for _ in range(n)]  #dp[i]表示以s[i]结尾的有效最长子串
        for i in range(n):
            if s[i]=='(':
                dp[i]=0
            elif s[i]==')':
                if s[i-1]=='(' and i>=2:
                    dp[i]=dp[i-2]+2
                if s[i-1]=='(' and i==1:
                    dp[i]=2

                elif s[i-1]==')'and s[i-dp[i-1]-1]=='(' and dp[i-1]>0 and i-dp[i-1]-1>=0:
                    dp[i]=dp[i-1]+2
                    if i-dp[i-1]-2>=0:
                        dp[i]=dp[i]+dp[i-dp[i-1]-2]

        return max(dp)

Solution().longestValidParentheses("(()))())(")