from collections import defaultdict
class Solution:
    def maxSubArrayLen(self, nums, k: int) -> int:
        n = len(nums)
        presum_idx = defaultdict(int)
        res = 0
        presum = 0
        presum_idx[0] = 0  # 前0个，和为0   也决定了必须用虚指
        for i in range(n):
            presum += nums[i]
            if presum not in presum_idx:
                presum_idx[presum] = i + 1  #储存的是满足和条件最小的下标，这样后面重复的出现也不会存进去，因为需要的是最长的数组，最小的下标才能得到最长的数组
            #寻找presum-k的前缀和是否已经被储存，若有的话，从0开始累计和到presum、从0开始累计和到presum-k的元素的element都有了，；两个集合长度相减即可得到答案
            if (presum - k) in presum_idx:
                res = max(res, i - presum_idx[presum - k] + 1)

        return res



if __name__ == '__main__':
    nums = [1,-1,5,-2,3]
    k = 3
    print(Solution().maxSubArrayLen(nums,k))
