class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        l = 0
        r = 0  # 左闭右闭
        res = 1
        while (l <= r < n):
            while (r + 1 < n and (s[l:r + 2].count(s[r + 1]) < 2)):
                r += 1
            res = max(res, r - l + 1)
            r += 1  # 包含重复字符
            while (s[l] in s[l + 1:r + 1]):
                l += 1

        return res
if __name__ == '__main__':
    s= "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
