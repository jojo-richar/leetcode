class Solution:
    def lengthOfLIS(self, nums) :
        n=len(nums)
        dp=[0]*(1+n) #以第n个数字结尾的最长升序字串
        dp[1]=1
        maxtemp=0
        for i in range(2,n+1):
            for j in range(i-2,-1,-1):
                if nums[j]<nums[i-1]:
                    maxtemp=max(maxtemp,dp[j+1])
            dp[i]=maxtemp+1
            maxtemp=0

        return dp[n]


if __name__ == '__main__':
    nums =  [1,3,6,7,9,4,10,5,6]
    print(Solution().lengthOfLIS(nums))
    print("ok")