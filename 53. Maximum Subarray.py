# class Solution:
#     def maxSubArray(self, nums):
#         n = len(nums)
#         ans = nums[0]
#         for i in range(n):
#             for j in range(i, n):
#                 ans = max(ans, sum(nums[i:j + 1]))
#
#         return ans


#分治法
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        return self.__max_sub_array(nums, 0, size - 1)

    def __max_sub_array(self, nums, left, right):
        if left == right:
            return nums[left]
        mid = (left + right) >> 1
        return max(self.__max_sub_array(nums, left, mid),
                   self.__max_sub_array(nums, mid + 1, right),
                   self.__max_cross_array(nums, left, mid, right))

    def __max_cross_array(self, nums, left, mid, right):
        # 一定包含 nums[mid] 元素的最大连续子数组的和，
        # 思路是看看左边"扩散到底"，得到一个最大数，右边"扩散到底"得到一个最大数
        # 然后再加上中间数
        left_sum_max = 0
        start_left = mid - 1
        s1 = 0
        while start_left >= left:
            s1 += nums[start_left]
            left_sum_max = max(left_sum_max, s1)
            start_left -= 1

        right_sum_max = 0
        start_right = mid + 1
        s2 = 0
        while start_right <= right:
            s2 += nums[start_right]
            right_sum_max = max(right_sum_max, s2)
            start_right += 1
        return left_sum_max + nums[mid] + right_sum_max

        

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
