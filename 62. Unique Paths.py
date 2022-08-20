class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def backtrack(srow, scol, frow, fcol):
            global ans
            if srow == frow and scol == fcol:
                ans = ans + 1
                # ans.append(1)
            if srow < frow:
                backtrack(srow + 1, scol, frow, fcol)
            if scol < fcol:
                backtrack(srow, scol + 1, frow, fcol)

        # ans=[]
        backtrack(0,0, m - 1, n - 1)
        return ans

if __name__== '__main__':

    ans=0    #全局变量得在最外层定义，类中最外层定义的也就是类变量，没达到全局变量级别
    print(Solution().uniquePaths(3,7))