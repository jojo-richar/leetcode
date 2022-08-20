class Solution:
    # brute method
    # def canJump(self, nums) :
    #     n=len(nums)
    #     dp=[False]*n
    #     dp[0]=True
    #     for i in range(0,n):
    #         temp=nums[i]
    #         a=i
    #         while(temp and dp[i] and a+1<n):
    #             dp[a+1]=True
    #             temp=temp-1
    #             a=a+1
    #     return dp[n-1]
    def canJump(self, nums):
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost,i + nums[i])
                if rightmost >= n - 1:
                    return True

        return False

print(Solution().canJump([3,2,1,0,4]))