sum_res = 0


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        def calculatenum(t):
            res = 0
            while (t > 0):
                res += t % 10
                t = t // 10

            return res

        def move(i, j, k):
            if i < 0 or i >= m or j < 0 or j >= n or (board[i][j]) or  (calculatenum(i) + calculatenum(j)) > k:
                return
            global sum_res
            sum_res += 1
            board[i][j]=1
            move(i - 1, j, k)
            move(i + 1, j, k)
            move(i, j - 1, k)
            move(i, j + 1, k)

        board=[[0]*n for _ in range(m)]
        move(0,0,k)
        global  sum_res
        return sum_res

if __name__ == '__main__':
    m=3
    n=3
    k=1
    print(Solution().movingCount(m,n,k))
