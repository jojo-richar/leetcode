# count=0
# class Solution(object):
#
#     def findTargetSumWays(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         def backtrack(n, target):
#             global  count
#             if n == len(nums):
#                 if target == 0:
#                     count += 1
#                 return
#
#
#             backtrack(n + 1, target - nums[n])
#             backtrack(n + 1, target + nums[n])
#
#         global count
#         backtrack(0, target)
#         return count

class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # def backtrack(n,target):
        #     if n==len(nums):
        #         if target==0:
        #             ans.append(1)
        #         return

        #     backtrack(n+1,target-nums[n])
        #     backtrack(n+1,target+nums[n])

        # ans=[]
        # backtrack(0,target)
        # return sum(ans)
        n = len(nums)
        num_sum = sum(nums)
        if (num_sum - target) % 2 != 0:
            return 0
        neg = (num_sum - target) // 2
        if neg<0:
            return 0
        dp = [[0] * (neg + 1) for _ in range(n + 1)]  # dp[i][j] 使得nums前i个数的和为j，共有几种情况
        dp[0][0] = 1
        for i in range(n):
            for j in range(neg + 1):
                if nums[i] > j:
                    dp[i + 1][j] = dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j - nums[i]] + dp[i][j]

        return dp[n][neg]
if __name__ == '__main__':
    nums = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
    target = 1000

    print(Solution().findTargetSumWays(nums,target))
