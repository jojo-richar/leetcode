import collections
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     need = collections.defaultdict(int)
    #     for c in t:
    #         need[c] += 1
    #     needCnt = len(t)
    #     i = 0
    #     res = (0, float('inf'))
    #     for j, c in enumerate(s):
    #         if need[c] > 0:
    #             needCnt -= 1
    #         need[c] -= 1
    #         if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
    #             while True:  # 步骤二：增加i，排除多余元素
    #                 c = s[i]
    #                 if need[c] == 0:
    #                     break
    #                 need[c] += 1
    #                 i += 1
    #             if j - i < res[1] - res[0]:  # 记录结果
    #                 res = (i, j)
    #             need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
    #             needCnt += 1
    #             i += 1
    #     return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


    def minWindow(self, s, t) :
        need=collections.defaultdict(int)
        n=len(s)
        ans=''
        lmin=n
        needcount = len(t)
        for i in range(len(t)):
            need[t[i]]=need[t[i]]+1
        i=0
        for j,c in enumerate(s):
            if need[c]>0:
                needcount-=1
            need[c]-=1
            if needcount==0: #开始寻找i
                while True:
                    c=s[i]
                    if need[c]==0:
                        break
                    need[c]+=1
                    i+=1
                if j-i+1 <= lmin:
                    lmin=j-i+1
                    ans=s[i:j+1]
                i+=1
                needcount+=1
                need[c]+=1
        return ans


        #     while(needcount>0 and j<n):
        #         if tempneed[s[j]]>0:
        #             needcount-=1
        #         tempneed[s[j]]=tempneed[s[j]]-1
        #         j=j+1
        #     j=j-1
        #     if needcount==0:
        #         a=i
        #         while(a<n and s[a] not in need.keys()):
        #             a=a+1
        #         length=j-a+1
        #         if length<=lmin:
        #             lmin=length
        #             ans=s[a:j+1]
        #
        # return ans

if __name__== '__main__':

    print(Solution().minWindow("cwaefgcf","cae"))


