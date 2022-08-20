
class Solution:
    def subsets(self, nums) :
    #
    #     def helper(i, tmp):
    #         res.append(tmp)
    #         for j in range(i, n):
    #             helper(j + 1, tmp + [nums[j]])
    #
    #
    #     res = []
    #     n = len(nums)
    #     helper(0, [])
    #     return res

        def backtrack(n , numlist, target):

            # global temp
            if n==target:
                result.append(temp[: ])
            # if n==target:
            #     # temp.clear()
            #     temp=[]  #注意这里对list赋值只是对新定义的局部变量（函数内层的list）赋值，无法改变外层的list,但是如果用append就可以改变，因为不定义list就没法append，默认调用外层的list
            else:
                temp.append(numlist[n])
                backtrack(n+1,numlist,target)
                temp.pop()
                backtrack(n+1, numlist, target)

        result=[]
        temp=[]
        targetnum=len(nums)
        backtrack(0,nums,targetnum)
        return result
if __name__== '__main__':
    print(Solution().subsets([1,2,3]))



