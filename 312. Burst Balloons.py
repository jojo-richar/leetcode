# 节点类
import inspect, sys , collections


class Solution:
    def maxCoins(self, nums):
        # if not nums:
        #     return 0
        # n = len(nums)
        # if n <= 2:
        #     if n == 1:
        #         return nums[0]
        #     else:
        #         minnum = min(nums)
        #         maxnum = max(nums)
        #         return (minnum * maxnum + maxnum)
        #
        # else:  # nums's length is more than 2
        #     minnum = min(nums[1:n - 1])
        #     index_min = nums.index(minnum)
        #     if index_min > 0:
        #         left = nums[index_min - 1]
        #     else:
        #         left = 1
        #
        #     if index_min < n - 1:
        #         right = nums[index_min + 1]
        #     else:
        #         right = 1
        #
        #     nums.remove(minnum)
        #     next_list=nums
        #     return (minnum * left * right + self.maxCoins(next_list))
        # nums首尾添加1，方便处理边界情况
        # nums首尾添加1，方便处理边界情况
        nums.insert(0, 1)
        nums.insert(len(nums), 1)

        store = [[0] * (len(nums)) for i in range(len(nums))]

        def range_best(i, j):
            m = 0
            # k是(i,j)区间内最后一个被戳的气球
            for k in range(i + 1, j):  # k取值在(i,j)开区间中
                # 以下都是开区间(i,k), (k,j)
                left = store[i][k]
                right = store[k][j]
                a = left + nums[i] * nums[k] * nums[j] + right
                if a > m:
                    m = a
            store[i][j] = m

        # 对每一个区间长度进行循环
        for n in range(2, len(nums)):  # 区间长度 #长度从3开始，n从2开始
            # 开区间长度会从3一直到len(nums)
            # 因为这里取的是range，所以最后一个数字是len(nums)-1

            # 对于每一个区间长度，循环区间开头的i
            for i in range(0, len(nums) - n):  # i+n = len(nums)-1

                # 计算这个区间的最多金币
                range_best(i, i + n)

        return store[0][len(nums) - 1]





if __name__ == '__main__':
    nums = [3,1,5,8]
    print(Solution().maxCoins(nums))
    print("ok")