class Solution:
    def permute(self, nums) :
        def backtrack(nums, n):
            if n == len(nums):
                result.append(temp[:])
                return
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    backtrack(nums, n + 1)
                    temp.pop()

        result = []
        temp = []
        backtrack(nums, 0)
        return result

print(Solution().permute([1,2,3]))

