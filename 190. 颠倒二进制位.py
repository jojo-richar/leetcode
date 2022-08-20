# 节点类
import inspect, sys , collections


class Solution:
    def reverseBits(self, n) :
        res=0
        for i in range(32):
            res=res<<1 | n&1
            n=n>>1
        return res



if __name__ == '__main__':
    n=964176192
    print(Solution().reverseBits(n))
    print("ok")