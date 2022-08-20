class Solution:
    def __init__(self) -> None:
        self.cnt = 0

    def getPermutation(self, n: int, k: int) -> str:
        temp = []
        used = [0] * (n + 1)

        def dfs(x, n):
            if x == n:
                self.cnt += 1
                return
            for i in range(1, n + 1):
                if used[i]:
                    continue
                temp.append(i)
                used[i] = 1
                dfs(x + 1, n)
                if self.cnt == k:
                    # res.append(temp[::1])
                    return
                temp.pop()
                used[i] = 0

        dfs(0, n)
        return ''.join(str(num) for num in temp[::1])


if __name__ == '__main__':
    n = 3
    k = 3
    print(Solution().getPermutation(n, k))
