from collections import defaultdict


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        pat = []
        slist = []
        p_cnt = [0]*26
        s_cnt = [0]*26
        for str in p:
            p_cnt[ord(str)-ord('a')] += 1

        res = []
        ns = len(s)
        np = len(p)
        if np>ns:
            return []
        for i in range(np):
            s_cnt[ord(s[i])-ord('a')] += 1
        if p_cnt== s_cnt:
            res.append(0)
        for i in range(1, ns):
            if i + np -1 < ns:
                s_cnt[ord(s[i+np-1]) - ord('a')] += 1
                s_cnt[ord(s[i-1])-ord('a')] -= 1
                if s_cnt == p_cnt:
                    res.append(i)

        return res


if __name__ == '__main__':
    s = "aaa"
    p = "aaaaa"

    print(Solution().findAnagrams(s,p))
