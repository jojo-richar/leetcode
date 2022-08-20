class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        i, j = 0, 0
        if len(nums) == 1:
            return nums
        # 在尽量靠右的位置，把尽量小的大数和小数交换
        for a in range(len(nums) - 1, 0, -1):
            if nums[a] > nums[a - 1]:
                i = a - 1
                j = a
                break

        if i == 0 and j == 0:
            nums.reverse()

        else:
            for c in range(len(nums) - 1, j - 1, -1):
                if nums[c] > nums[i]:
                    k = c
                    break

            nums[k], nums[i] = nums[i], nums[k]
            templist=nums[j:len(nums)]
            nums[j:len(nums)]=templist[::-1]
            # nums[j:len(nums)]=nums[len(nums)-1:j-1:-1]
            pass
# class Solution:
#     def nextPermutation(self, nums) :
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         i = n - 2
#         while (i >= 0 and nums[i] > nums[i + 1]):
#             i = i - 1
#         if i >= 0:
#             j = n - 1
#             while (j > i and nums[j] <= nums[i]):
#                 j = j - 1
#             nums[i], nums[j] = nums[j], nums[i]
#
#         left, right = i + 1, n - 1
#         while (left < right):
#             nums[left], nums[right] = nums[right], nums[left]
#             left = left + 1
#             right = right - 1
#         pass


Solution().nextPermutation([1,3,2])