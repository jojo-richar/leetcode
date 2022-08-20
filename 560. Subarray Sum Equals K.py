class Solution:
    def subarraySum(self, nums, k: int):
        # dp[i][j]  前i个数中子数组为j的子数组个数
        n = len(nums)
        dp = [([1]+[0] * (k)) for _ in range(n + 1)]
        dp[1][nums[0]] = 1
        for i in range(2, n + 1):
            for j in range(k + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= nums[i - 1]:
                    dp[i][j] =dp[i - 1][j] + dp[i - 1][j - nums[i-1]]

        return dp[n][k]


if __name__ == '__main__':
    nums = [1,1,1]
    k = 2

    print(Solution().subarraySum(nums,k))
