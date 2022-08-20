class Solution:
    def removeInvalidParentheses(self, s: str) :
        res = []
        leftmove = 0
        rightmove = 0
        n = len(s)
        for i in range(n):
            if s[i] == "(":
                leftmove += 1
            if s[i] == ")":
                if leftmove > 0:
                    leftmove -= 1
                else:
                    rightmove += 1  # 计算出需要删除的左右括号数量

        def isValid(s):
            numParent = 0
            for i in range(len(s)):
                if s[i] == "(":
                    numParent += 1
                if s[i] == ")":
                    if numParent > 0:
                        numParent -= 1
                    else:
                        return False

            return (numParent == 0)

        def search(s, start, leftmove, rightmove):
            if leftmove == 0 and rightmove == 0 and isValid(s) and s not in res:
                res.append(s)
                return
            for i in range(start, len(s)):
                if s[i] == '(' and leftmove > 0:
                    search(s[:i] + s[i + 1:], i, leftmove-1, rightmove)
                if s[i] == ")" and rightmove > 0:
                    search(s[:i] + s[i + 1:], i, leftmove, rightmove-1)

        search(s, 0, leftmove, rightmove)
        return res


if __name__ == '__main__':
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))
    print("ok")