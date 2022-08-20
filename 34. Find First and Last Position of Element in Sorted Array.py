# class Solution:
#     def searchRange(self, nums, target: int) :
#         if len(nums) == 0:
#             return [-1, -1]
#         rindex = lindex =index= -1
#         l, r = 0, len(nums) - 1
#         while (l <= r):
#             mid = (l + r) // 2
#             if nums[mid] == target:
#                 index = mid
#             if nums[mid] < target:
#                 l = mid + 1
#             else:
#                 r = mid - 1
#
#         rindex = lindex = index
#         if lindex == -1:
#             return [-1, -1]
#         else:
#             while (lindex - 1 >= 0 and nums[lindex - 1] == nums[lindex]):
#                 lindex = lindex - 1
#             while (rindex + 1 < len(nums) and nums[rindex + 1] == nums[rindex]):
#                 rindex = rindex + 1
#             return [lindex, rindex]
class Solution(object):
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_func(nums,target):
            n = len(nums)-1
            ans = n+1
            left = 0
            right = n
            while(left<=right):
                mid = (left+right)//2
                if nums[mid] >= target:    #找第一个>=target的下标
                    ans = mid
                    right = mid-1
                if nums[mid] < target:
                    left = mid+1
            return ans
        a =  left_func(nums,target)
        b = left_func(nums,target+1)
        if  b<1 or(a>len(nums)-1 and b>len(nums)-1) or nums[a] != target or a==-1 or a>b :
            return [-1,-1]
        else:
            return [a,b-1]
        pass

print(Solution().searchRange([2,2],3))


