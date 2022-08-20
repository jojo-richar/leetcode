class Solution:
    def coinChange(self, coins, amount: int) :
        dp=[-1]*(amount+1)
        tempmin=float("inf")
        dp[0]=0
        for i in range(1,amount+1):
            for j in coins:
                if j<=i and dp[i-j]>=0:
                    tempmin=min(tempmin,dp[i-j])
            dp[i]=1+tempmin
            tempmin=float("inf")

        return dp[amount]

if __name__ == '__main__':
    coins = [2]
    amount = 13
    print(Solution().coinChange(coins,amount))
