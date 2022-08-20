class Solution:
    def search(self, nums, target) :
        if not nums:
            return -1
        l,r=0,len(nums)-1

        while(r>=l):
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            if nums[mid]>=nums[0]: #mid左边是有序的
                if  nums[0]<=target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:#mid右边是有序的
                if nums[mid]<target<=nums[len(nums)-1]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
print(Solution().search([4,5,6,1,2],0))