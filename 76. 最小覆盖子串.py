from collections import defaultdict
import math

from collections import defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for i in range(len(t)):
            need[t[i]] += 1
        left = 0
        res = math.inf
        resstr = ''
        for i in range(len(s)):
            c = s[i]
            need[c] -= 1
            if max(need.values()) <= 0:  # 右边界已经拓展到含有所有t字符的位置了
                while (True):
                    if need[s[left]] == 0:  # 左边界已经拓展到极限
                        break
                    need[s[left]] += 1
                    left += 1
                if i - left + 1 < res:
                    res = i - left + 1
                    resstr = s[left:i + 1]  # 记录信息
                need[s[left]] += 1
                left += 1  # 左边界往右再拓展一步，此时滑动窗口不包含所有t字符
        return resstr


if __name__ == '__main__':
    s = "cwaefgc"
    t = "cae"
    print(Solution().minWindow(s, t))
    print("ok")
