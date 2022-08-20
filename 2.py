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
# class Solution:
#     def findMedianSortedArrays(self, nums1, nums2) :
#         def getKthElement(k):
#             """
#             - 主要思路：要找到第 k (k>1) 小的元素，那么就取 pivot1 = nums1[k/2-1] 和 pivot2 = nums2[k/2-1] 进行比较
#             - 这里的 "/" 表示整除
#             - nums1 中小于等于 pivot1 的元素有 nums1[0 .. k/2-2] 共计 k/2-1 个
#             - nums2 中小于等于 pivot2 的元素有 nums2[0 .. k/2-2] 共计 k/2-1 个
#             - 取 pivot = min(pivot1, pivot2)，两个数组中小于等于 pivot 的元素共计不会超过 (k/2-1) + (k/2-1) <= k-2 个
#             - 这样 pivot 本身最大也只能是第 k-1 小的元素
#             - 如果 pivot = pivot1，那么 nums1[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums1 数组
#             - 如果 pivot = pivot2，那么 nums2[0 .. k/2-1] 都不可能是第 k 小的元素。把这些元素全部 "删除"，剩下的作为新的 nums2 数组
#             - 由于我们 "删除" 了一些元素（这些元素都比第 k 小的元素要小），因此需要修改 k 的值，减去删除的数的个数
#             """
#
#             index1, index2 = 0, 0
#             while True:
#                 # 特殊情况
#                 if index1 == m:
#                     return nums2[index2 + k - 1]
#                 if index2 == n:
#                     return nums1[index1 + k - 1]
#                 if k == 1:
#                     return min(nums1[index1], nums2[index2])
#
#                 # 正常情况
#                 newIndex1 = min(index1 + k // 2 - 1, m - 1)
#                 newIndex2 = min(index2 + k // 2 - 1, n - 1)
#                 pivot1, pivot2 = nums1[newIndex1], nums2[newIndex2]
#                 if pivot1 <= pivot2:
#                     k -= newIndex1 - index1 + 1
#                     index1 = newIndex1 + 1
#                 else:
#                     k -= newIndex2 - index2 + 1
#                     index2 = newIndex2 + 1
#
#         m, n = len(nums1), len(nums2)
#         totalLength = m + n
#         if totalLength % 2 == 1:
#             return getKthElement((totalLength + 1) // 2)
#         else:
#             return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2
#
#
#
#
# A= Solution()
# print(A.findMedianSortedArrays([1,3],[3,5,6]))
# b=[]
# c=[]
# d=[]
# rk=0
# length=0
# a='ac'
# list_a=list(a)
# b=list(reversed(list_a))
# for i in range(len(list_a)):
#     if list_a[i]==b[i]:
#         c.append(1)
#     else:
#         c.append(0)
#
# if 1 not in c:
#     result=list_a[0]
#     length=1
#
# for t in range(len(c)):
#     rk=t
#     while(c[t]==1 and rk<=len(c)-1):
#         if (c[rk]==1):
#             d.append(list_a[rk])
#         rk = rk + 1
#     temp=''.join(d)
#     if len(d)>=length:
#         result=temp
#         length=len(d)
#     d.clear()
# print(result)

#TOP100-5 brute method
# class Solution:
#     def longestPalindrome(self, s):
#         fstr=''
#         def isPalindrome(s):
#             fstr = s[::-1]
#             if fstr == s:
#                 return True
#             else:
#                 return False
#
#         n=len(s)
#         # if n==1:
#         #     return s
#         max_len=0
#         for i in range(n):
#             j=i
#             while(j<n):
#                 temp=s[i:j+1]
#                 if isPalindrome(temp)==True:
#                     if len(temp)>=max_len:
#                         result=temp
#                         max_len=len(temp)
#                 j=j+1
#         print(result)
#         return result
#
# A=Solution()
# A.longestPalindrome('a')


#TOP100-5 extend from center
class Solution:
    def extendfromcenter(self,s,sl,sr):
        while sl>=0 and sr<len(s) and s[sl]==s[sr]:
            sl=sl-1
            sr=sr+1
        return sl+1,sr-1
    def longestPalindrome(self, s: str) -> str:
        maxlenpalin=0
        for i in range(len(s)):
            left1,right1=self.extendfromcenter(s,i,i)
            left2,right2=self.extendfromcenter(s,i,i+1)
            if right1-left1>=right2-left2:
                maxlen=right1-left1+1
                palins=s[left1:right1+1]
            else:
                maxlen=right2-left2+1
                palins=s[left2:right2+1]
            if maxlen>maxlenpalin:
                maxlenpalin=maxlen
                result=palins
        print(result)
        return result

A=Solution()
A.longestPalindrome('babad')





        