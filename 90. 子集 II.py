class Solution:
    def subsetsWithDup(self, nums) :
        res = []
        temp = []
        n = len(nums)
        used = [0] * n

        def backtrack(x, start):
            if x <= n:
                res.append(temp[::1])
            if x>n:
                return
            for i in range(start, n):
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                temp.append(nums[i])
                used[i] = 1
                backtrack(x + 1, i + 1)
                temp.pop()
                used[i] = 0

        nums = sorted(nums)
        backtrack(0, 0)
        return res

if __name__ == '__main__':
    nums = [1,1,2]
    print(Solution().subsetsWithDup(nums))
