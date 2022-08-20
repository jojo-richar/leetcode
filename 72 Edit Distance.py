import collections
class Solution:
    def minDistance(self, word1, word2):
        m=len(word1)
        n=len(word2)
        dp=[[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1):
            dp[0][i]=i
        for i in range(m+1):
            dp[i][0]=i

        for i in range(1,m+1):
            for j in range(1,n+1):
                insert_word1=1+dp[i-1][j]
                insert_word2=1+dp[i][j-1]
                replace_cost=1+dp[i-1][j-1]
                if word1[i-1]==word2[j-1]:
                    replace_cost=replace_cost-1
                dp[i][j]=min(insert_word1,insert_word2,replace_cost)
        return dp[m][n]




if __name__== '__main__':

    print(Solution().minDistance('horse','ros'))