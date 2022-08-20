from collections import defaultdict


class Solution:
    def threeSum(self, nums) :
        n = len(nums)
        nums.sort()
        res = []
        for i in range(n):
            first = nums[i]
            if first > 0:
                break
            if i >= 1 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = n - 1
            while (l < r):
                if nums[l] + nums[r] + first == 0:
                    res.append([first, nums[l], nums[r]])
                    while (l < r and nums[l] == nums[l + 1]):
                        l += 1
                    while (l < r and nums[r] == nums[r - 1]):
                        r -= 1
                    l+=1
                    r-=1

                elif nums[l] + nums[r] + first > 0:
                    r -= 1
                else:
                    l += 1

        return res


# class Solution:
#     def threeSum(self, nums):
#         #先排序，再用双指针
#         n=len(nums)
#         result=[]
#         if len(nums)<3:
#             return[]
#         nums.sort()
#         for i in range(len(nums)):
#             if nums[i]>0:
#                 break
#             if nums[i]==nums[i-1] and i>0:  #前面多一个num[i-1]的情况都考虑过（num[i-1]元素出现至少两次），已经包含了只出现一次nums[i]的情况
#                 continue
#             left=i+1
#             right=n-1
#             while(left<right):
#                 if(nums[i]+nums[left]+nums[right]==0):
#                     if [nums[i],nums[left],nums[right]] not in result:
#                         result.append([nums[i],nums[left],nums[right]])
#                     while(left<right and nums[left]==nums[left+1] ):
#                         left+=1
#                     while (left<right and nums[right]==nums[right-1]):
#                         right-=1
#                     right-=1
#                     left+=1
#                 elif (nums[i]+nums[left]+nums[right]>0):
#                     right-=1
#                 else:
#                     left+=1
#         print (result)
#         return result


if __name__ == '__main__':
    A=Solution()
    print(A.threeSum([-1,0,1,2,-1,-4]))

  p