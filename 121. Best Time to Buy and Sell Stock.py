class Solution:
    def maxProfit(self, prices) :
        n = len(prices)
        profit = 0
        cost = prices[0]
        for i in range(n):
            get = prices[i]
            cost = min(cost, prices[i])
            profit = max(profit, get - cost)

        return profit



if __name__ == '__main__':

    print(Solution().maxProfit([7,1,5,3,6,4]))
