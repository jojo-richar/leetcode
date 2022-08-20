# class Solution:
#     def twoSum(self, nums, target):
#         a = len(nums)
#         result = []
#         i = 0
#         c = 0
#         for i in range(a):
#             if c<a:
#                 c= i+1
#             while(c<a):
#                 if (nums[i]+nums[c] == target) and c < a:
#                     result.append(i)
#                     result.append(c)
#                     c = c+1
#                 else:
#                     c = c+1
#             c = 0
#         return result
#
# A= Solution()
# ak = input()
# ap = ak.split('\n')
# a3 = eval(ap[0])  #将字符串形式的列表转换成列表
# b = int(ap[1])
#
# A.twoSum(a3,b)
class Solution:
    def twoSum(self, nums, target: int):
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i
        return []

A=Solution()
print(A.twoSum([1,2,3,3],6))
