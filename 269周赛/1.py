class Solution:
    def minimumDeletions(self, nums) :
        n = len(nums)
        maxnum = max(nums)
        minnum = min(nums)
        indexmax = nums.index(maxnum)
        indexmin = nums.index(minnum)
        medium = n / 2
        op = 1
        # if indexmin < medium:
        #     opmin = indexmin+1
        # else:
        #     opmin = n  - indexmin
        # if indexmax < medium:
        #     opmax = indexmax+1
        # else:
        #     opmax = n  - indexmax

        if indexmin < medium and indexmax < medium:
            op = max(indexmin+1,indexmax+1)
        elif indexmin >= medium and indexmax >= medium:
            op = max(n-indexmax,n-indexmin)
        elif indexmin < medium and indexmax >= medium:
            op = min(indexmax+1,n-indexmin,indexmin+1+n-indexmax)
        else:
            op = min(indexmin + 1, n - indexmax, indexmax + 1 + n - indexmin)

        return op


if __name__ == '__main__':
    nums= [-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]
    print(Solution().minimumDeletions(nums))