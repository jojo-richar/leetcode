from collections import defaultdict
class Solution:
    def largestIsland(self, grid) -> int:
        nr = len(grid)
        nc = len(grid[0])
        key = 2
        area = defaultdict(int)
        res=0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 1:
                    area[key] = self.dfs(grid, i, j,key)
                    res=max(res,area[key])
                    key += 1

        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == 0:
                    neighbors=set()
                    for a,b in (i-1,j),(i+1,j),(i,j-1),(i,j+1):
                        if 0<=a<nr and 0<=b<nc:
                            neighbors.add(grid[a][b])
                    res=max(res,1+sum(area[key] for key in neighbors ))
        return res

    def dfs(self, grid, r, c ,key):
        nr = len(grid)
        nc = len(grid[0])
        if not (0 <= r <= nr - 1 and 0 <= c <= nc - 1):  #越界了
            return 0
        if grid[r][c] != 1:  # 不是未遍历陆地，是海洋或者已经遍历的陆地
            return 0
        grid[r][c] = key
        return (1 +
                self.dfs(grid, r - 1, c,key)
                + self.dfs(grid, r + 1, c,key)
                + self.dfs(grid, r, c - 1,key)
                + self.dfs(grid, r, c + 1,key))


if __name__ == '__main__':
    grid=[[0,0],[0,0]]
    print(Solution().largestIsland(grid))
