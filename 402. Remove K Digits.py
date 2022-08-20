# 节点类
import inspect, sys , collections


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)

        # m=n-k #m is the num need to be chosen
        # res=[]
        # index=-1
        # for i in range(m,0,-1):

        #     temp=min(num[index+1:n-i+1])
        #     index=num.index(temp)
        #     res.append(temp)

        # return res
        monostack = []
        count = 0
        for i in range(n):
            while (monostack and int(num[i]) < int(monostack[-1]) and count < k):
                monostack.pop()
                count += 1

            monostack.append(num[i])

        monostack = monostack[0:n - k]

        while (len(monostack) > 1 and monostack[0] == '0'):  # 删除前端无用的0
            monostack.pop(0)

        if not monostack:
            return '0'
        return "".join(monostack)



if __name__ == '__main__':
    num = "1432219"
    k = 3
    print(Solution().removeKdigits(num,k))
    print("ok")