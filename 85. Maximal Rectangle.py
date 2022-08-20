class Solution:
    #method-1 brute
    def maximalRectangle(self, matrix):
        # matrix=map(int,matrix)
        row=len(matrix)
        if row==0:
            return 0
        col=len(matrix[0])
        newmatrix=[[0]*col for _ in range(row)]
        res=0
        for i in range(row):  #给第一列赋值
            newmatrix[i][0]=int(matrix[i][0])
        for i in range(row):
            for j in range(col):
                matrix[i][j]=int(matrix[i][j])
                if j>=1:
                    if matrix[i][j]:
                        newmatrix[i][j]=newmatrix[i][j-1]+1
                    else:
                        newmatrix[i][j]=0
                width=newmatrix[i][j]
                for ni in range(i+1):
                    height=ni+1
                    width=min(width,newmatrix[i-ni][j])
                    area=height*width
                    res=max(res,area)
        return res









    #method-2 monostack
    # def maximalRectangle(self, matrix) :
    #     row=len(matrix)
    #     if row==0:
    #         return 0
    #     col=len(matrix[0])
    #     res=0
    #     heights = [0] * col
    #     for i in range(row):
    #         for j in range(col): #在每一行根据该列的1，0分布情况构建直方图
    #             if (matrix[i][j])=="1":
    #                 heights[j]=heights[j]+1
    #             else:
    #                 heights[j]=0
    #         res=max(res,self.largestRectangleArea(heights))
    #
    #     return res
    #
    #
    # def largestRectangleArea(self, heights):
    #     n=len(heights)
    #     left=[0]*n
    #     right=[0]*n  #存储左右两侧最近的小于此高度的柱子
    #
    #     lstack=[]
    #     for i in range(n):    #从左到右遍历找左侧边界
    #         while(lstack and heights[lstack[-1]]>=heights[i]):
    #             lstack.pop()
    #         if lstack:
    #             left[i]=lstack[-1]
    #             lstack.append(i)
    #         else:
    #             left[i]=-1
    #             lstack.append(i)
    #
    #     rstack=[]
    #     for i in range(n-1,-1,-1):  #从右到左遍历寻找右边界
    #         while(rstack and heights[rstack[-1]]>=heights[i]):
    #             rstack.pop()
    #         if rstack:
    #             right[i]=rstack[-1]
    #             rstack.append(i)
    #         else:
    #             right[i]=n
    #             rstack.append(i)
    #
    #     res=0
    #     for i in range(n):
    #         res=max(res,heights[i]*(right[i]-left[i]-1))
    #
    #     return res



if __name__ == '__main__':
    print(Solution().maximalRectangle( [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
    # print(Solution().maximalRectangle([] ))