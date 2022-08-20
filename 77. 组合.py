class Solution:
    def combine(self, n: int, k: int) :
        res = []
        temp = []
        used = [0] * (n + 1)

        def backtrack(x, start):
            if x == k:
                res.append(temp[::1])
                return
            for i in range(start, n + 1):
                if not used[i]:
                    temp.append(i)
                    used[i] = 1
                    backtrack(x+1, i)
                    temp.pop()
                    used[i] = 0

        backtrack(0, 1)
        return res


if __name__ == '__main__':
    n = 4
    k = 2
    print(Solution().combine(n,k))
