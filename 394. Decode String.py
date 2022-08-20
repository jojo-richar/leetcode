class Solution:
    def decodeStringDfs(self, s: str) -> str:
        def dfs(i):
            res, multi = "", 0
            # 这里不能用for i in range(len(s)),因为递归调用时，新的循环不从0开始从i开始
            while i < len(s):
                # 遇到数字
                if '0' <= s[i] <= '9':
                    multi = multi * 10 + int(s[i])  # 考虑数字是2位以上的情况
                # 遇到'['开始将后续的string递归
                elif s[i] == '[':
                    i, tmp = dfs(i + 1)
                    # 注意，返回i的含义是更新上层递归指针位置，因为内层递归已经吃掉一串str，若不跟新i，外层仍然从i+1开始，则会重复处理内层处理过的一串str。
                    res += multi * tmp
                    multi = 0
                # 遇到']'到达递归边界，结束递归，返回新i和处理好的内层res
                elif s[i] == ']':
                    return i, res
                # 遇到其他，则当字母串处理
                else:
                    res += s[i]
                i += 1
            # 考虑结尾是...]abc的情况
            return res

        return dfs(0)
if __name__ == '__main__':
    s = "3[a]2[bc]"
    print(Solution().decodeStringDfs(s))
