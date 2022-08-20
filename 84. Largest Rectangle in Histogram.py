class Solution:
    def largestRectangleArea(self, heights):
        n=len(heights)
        left=[0]*n
        right=[0]*n  #存储左右两侧最近的小于此高度的柱子

        lstack=[]
        for i in range(n):    #从左到右遍历找左侧边界
            while(lstack and heights[lstack[-1]]>=heights[i]):
                lstack.pop()
            if lstack:
                left[i]=lstack[-1]
                lstack.append(i)
            else:
                left[i]=-1
                lstack.append(i)
        
        rstack=[]
        for i in range(n-1,-1,-1):  #从右到左遍历寻找右边界
            while(rstack and heights[rstack[-1]]>=heights[i]):
                rstack.pop()
            if rstack:
                right[i]=rstack[-1]
                rstack.append(i)
            else:
                right[i]=n
                rstack.append(i)

        res=0
        for i in range(n):
            res=max(res,heights[i]*(right[i]-left[i]-1))

        return res



if __name__ == '__main__':
    print(Solution().largestRectangleArea([6,7,5,2,4,5,9,3]))