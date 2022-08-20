class Solution:
    def numIslands(self, grid) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])
        num_island = 0
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    num_island += 1
                    self.dfs(grid, i, j)

        return num_island

    def dfs(self, grid, r, c):
        nr = len(grid)
        nc = len(grid[0])
        if not (0 <= r <= nr - 1 and 0 <= c <= nc - 1):
            return
        if grid[r][c] != "1":
            return
        grid[r][c] = "2"
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r, c - 1)
        self.dfs(grid, r, c + 1)


if __name__ == '__main__':
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]

    print(Solution().numIslands(grid))
