from collections import defaultdict

import copy


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        m = len(board)
        n = len(board[0])
        board_copy = copy.deepcopy(board)

        def update(i, j):
            count = 0
            for neighbor in neighbors:
                newi = i + neighbor[0]
                newj = j + neighbor[1]
                if 0 <= newi < m and 0 <= newj < n and board_copy[newi][newj]:
                    count += 1
            if (count < 2 or count > 3) and board_copy[i][j] == 1:
                board[i][j] = 0
            if (count == 2 or count == 3) and board_copy[i][j] == 1:
                board[i][j] = 1
            if count == 3 and board_copy[i][j] == 0:
                board[i][j] = 1

        for i in range(m):
            for j in range(n):
                update(i, j)


if __name__ == '__main__':
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]

    print(Solution().gameOfLife(board))
