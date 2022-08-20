import heapq
import collections
class Solution:
    def maxSlidingWindow(self, nums, k) :
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)

        ans = [nums[q[0]]]
        for i in range(k, n):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            while q[0] <= i - k:
                q.popleft()
            ans.append(nums[q[0]])

        return ans


if __name__ == '__main__':
    nums = [4,2,3,5,6]
    k = 1
    print(Solution().maxSlidingWindow(nums,k))
