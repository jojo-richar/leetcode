from collections import defaultdict
import  heapq
class Solution:
    def topKFrequent(self, nums, k: int) :
        priorDeque=[]
        # return res
        n=len(nums)
        res=[]
        hashmap = defaultdict(int)
        for i in range(n):
            hashmap[nums[i]] += 1
        for key, value in hashmap.items():
            if len(priorDeque)<k:
                heapq.heappush(priorDeque,(value,key))  #二元的话，堆默认比较第一个值的大小
            else:
                if priorDeque[0][0]<value:

                    heapq.heappop(priorDeque)
                    heapq.heappush(priorDeque,(value,key))


        return ([item[1] for item in priorDeque])


if __name__ == '__main__':
    nums = [1,1,1,1,3,3,5,5,3]
    k = 2
    print(Solution().topKFrequent(nums,k))