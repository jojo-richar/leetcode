class Solution:
    def wordBreak(self, s: str, wordDict):
        # n=len(s)
        # dp=[False]*(n+1)  #前i个字符能否匹配上
        # dp[0]=True
        # for i  in  range(n+1):
        #     for j in range(i,n+1):
        #         if dp[i] and s[i:j] in wordDict:
        #             dp[j]=True
        # return dp[-1]
        import functools
        @functools.lru_cache(None)
        def back_track(s):
            if (not s):
                return True
            res = False
            for i in range(1, len(s) + 1):
                if (s[:i] in wordDict):
                    res = back_track(s[i:]) or res
            return res

        return back_track(s)



if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]

    print(Solution().wordBreak(s,wordDict))