class Solution:
    def exist(self, board, word) :
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 按照右左上下的顺序来搜素

        def backtrack(i, j, k):
            print(i, ",", j)
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi <= len(board) - 1 and 0 <= newj <= len(board[0]) - 1:
                    if (newi, newj) not in visited:
                        if backtrack(newi, newj, k + 1):
                            result = True
                            break
            visited.remove((i,j))
            return result

        visited = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                print("new gen")
                if backtrack(i, j, 0):
                    return True

        return False


if __name__== '__main__':
    print(Solution().exist([["C","A","A"],["A","A","A"],["B","C","D"]],"AAB"))



