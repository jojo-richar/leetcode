class Solution:
    # def trap(self, height):
    #     n=len(height)
    #     downcenter=[]
    #     left_right_boundary=[]
    #     # for i in range(1,n-1):
    #     #     if height[i]<height[i-1] and height[i]<height[i+1]:
    #     #         downcenter.append(i)
    #     i=1
    #     while(i<n-1):
    #         if height[i]>=height[i+1]:
    #             i=i+1
    #         else:
    #             if i>0:
    #                 downcenter.append(i)
    #                 while( i+1<n and height[i]<=height[i+1]):
    #                     i=i+1
    #     for i in downcenter:
    #         a=b=i
    #         while(a>=1 and height[a-1]>=height[a]):
    #             a-=1
    #         while(b<n-1 and height[b+1]>=height[b]):
    #             b+=1
    #         left_right_boundary.append([a,b])
    #
    #     area=templ=tempr=0
    #     minusarea=0
    #     for i in range(len(left_right_boundary)):
    #         templ=left_right_boundary[i][0]
    #         tempr=left_right_boundary[i][1]
    #         for a in range(templ+1,tempr):
    #             minusarea=minusarea+height[a]
    #         area=area+min(height[templ],height[tempr])*(tempr-templ-1)-minusarea
    #         minusarea=0
    #     return area
    def trap(self, height):
# #按列来看
#         ans=0
#         n=len(height)
#         for i in range(1,n-1):
#             lmax=max(height[0:i])
#             rmax=max(height[i+1:n])
#             if min(lmax,rmax)>height[i]:
#                 ans=ans+min(lmax,rmax)-height[i]
#         return ans
#         area=0
#         n=len(height)
#         max_left=[0]*n
#         for i in range(1,n-1):
#             max_left[i]=max(max_left[i-1],height[i-1])
#         max_right=[0]*n
#         for i in range(n-2,0,-1):
#             max_right[i]=max(max_right[i+1],height[i+1])
#
#         for i in range(1,n-1):
#             area=area+max(min(max_left[i],max_right[i])-height[i],0)

        ans = 0
        stack = list()
        n = len(height)

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                currWidth = i - left - 1
                currHeight = min(height[left], height[i]) - height[top]
                ans += currWidth * currHeight
            stack.append(i)

        return ans



        


print(Solution().trap( [0,1,0,2,1,0,1,3,2,1,2,1]))
