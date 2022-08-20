class Solution:
    def singleNumber(self, nums) -> int:
        count = [0] * 32
        for num in nums:
            for i in range(32):
                count[i] += num & 1
                num = num >> 1
        res = 0
        for i in range(32):
            count[31 - i] = count[31 - i] % 2
            res = res << 1
            res = res | count[31 - i]

        return res if count[31] % 2 == 0 else ~(res ^ 0xffffffff)


if __name__ == '__main__':
    nums = [7,2,7,9,9]
    print(Solution().singleNumber(nums))
    print("ok")