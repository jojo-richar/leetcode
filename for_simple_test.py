# import re
#
#
# class Solution:
#     chunk_IPv4 = r'([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'
#     patten_IPv4 = re.compile(r'^(' + chunk_IPv4 + '+\.){3}' + chunk_IPv4 + r'$')
#
#     chunk_IPv6 = r'([0-9a-fA-F]{1,4})'
#     patten_IPv6 = re.compile(r'^(' + chunk_IPv6 + '\:){7}' + chunk_IPv6 + r'$')
#
#     def validIPAddress(self, IP: str) -> str:
#         if '.' in IP:
#             return "IPv4" if self.patten_IPv4.match(IP) else "Neither"
#         if ':' in IP:
#             return "IPv6" if self.patten_IPv6.match(IP) else "Neither"
#         return "Neither"

# class Solution:
#     def maxSubArray(self, nums) :
#         n = len(nums)
#
#         dp = [0] * n
#         dp[0] = nums[0]
#         for i in range(1, n):  # end
#             dp[i] = max(dp[i - 1], dp[i - 1] + nums[i])
#
#         return max(dp)
#
# def quicksort(nums,left,right):
#     if left<right:
#         pivot=nums[left]
#         i=left
#         j=right
#         while(i<j):
#             while(i<j and nums[j]>=pivot):
#                 j-=1
#             if i<j:
#                 nums[i]=nums[j]
#
#             while(i<j and nums[i]<=pivot):
#                 i+=1
#             if i<j:
#                 nums[j]=nums[i]
#         nums[i]=pivot
#         quicksort(nums,left,i-1)
#         quicksort(nums,i+1,right)
#
# nums=[0,0,1,2,4,2,2,3,1,4]
# quicksort(nums,0,len(nums)-1)
# print(nums)


# Solution().quicksort(nums,0,len(nums)-1)

# x = pd.DataFrame(np.random.rand(100, 8))
# # print(x.corr())
# # sns.heatmap(x.corr())
# # sns.pairplot(x)
# a=np.arange(0.01,0.1,0.01)
# print(a)
# plt.show()


# print(Solution().myPow(2.1,-2))


# rec_func(max_recursion_depth)
# fun()
# print(a)
#
# def singleton(cls):
#     # 单下划线的作用是这个变量只能在当前模块里访问,仅仅是一种提示作用
#     # 创建一个字典用来保存类的实例对象
#     _instance = {}
#
#     def _singleton(*args, **kwargs):
#         # 先判断这个类有没有对象
#         if cls not in _instance:
#             _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
#         # 将实例对象返回
#         return _instance[cls]
#
#     return _singleton
#
#
# @singleton
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x
#         print('这是A的类的初始化方法')
#
#
# a1 = A(2)
# a2 = A(3)
# print(id(a1), id(a2))
class Solution:
    def numDecodings(self, s: str) :
        n=len(s)
        dp=[0]*(n+1)
        dp[0]=1
        for i in range(1,n+1):
            if s[i-1]!='0':
                dp[i]=dp[i-1]
            if i>1 and s[i-2]=='1' or (s[i-2]=='2' and '0'<=s[i-1]<='6') :
                dp[i]+=dp[i-2]
        return dp[n]


if __name__ == '__main__':
    s = '2'
    print(Solution().numDecodings(s))
