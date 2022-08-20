class Solution:
    def findKthLargest(self, nums, k) :
        # nums.sort()
        # return nums[len(nums)-k]

        def quickselect(left, right):
            pivot = nums[left]
            j = left+1
            for i in range(left + 1, right+1):
                if nums[i] < pivot:
                    nums[j], nums[i] = nums[i], nums[j]
                    j += 1
            j-=1
            nums[j], nums[left] = nums[left], nums[j]
            return j

        left = 0
        right = len(nums) - 1
        n = len(nums) - k  # in ascending ordered list, the kth largest element's index is len(nums)-k
        while (1):
            index = quickselect(left, right)
            if n == index:
                return nums[index]
            elif n < index:
                right = index-1
            else:
                left = index+1

if __name__ == "__main__":
    nums= [3,2,1,5,6,4]
    k=2
    print(Solution().findKthLargest(nums,k))