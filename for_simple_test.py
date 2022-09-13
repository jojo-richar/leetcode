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
from sortedcontainers import SortedList


class Solution:
    def getSkyline(self, buildings) :
        ans = []

        # 预处理所有的点，为了方便排序，对于左端点，令高度为负；对于右端点令高度为正
        ps = []
        for l, r, h in buildings:
            ps.append((l, - h))
            ps.append((r, h))
        # 先按照横坐标进行排序
        # 如果横坐标相同，则按照左端点排序
        # 如果相同的左/右端点，则按照高度进行排序
        ps.sort()

        prev = 0
        # 有序列表充当大根堆
        q = SortedList([prev])

        for point, height in ps:
            if height < 0:
                # 如果是左端点，说明存在一条往右延伸的可记录的边，将高度存入优先队列
                q.add(-height)
            else:
                # 如果是右端点，说明这条边结束了，将当前高度从队列中移除
                q.remove(height)

            # 取出最高高度，如果当前不与前一矩形“上边”延展而来的那些边重合，则可以被记录
            cur = q[-1]
            if cur != prev:
                ans.append([point, cur])
                prev = cur

        return ans


if __name__ == '__main__':
    buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    print(Solution().getSkyline(buildings))
