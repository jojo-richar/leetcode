# 节点类
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# 树生成代码
def generate_tree(vals):
    if len(vals) == 0:
        return None
    que = [] # 定义队列
    fill_left = True # 由于无法通过是否为 None 来判断该节点的左儿子是否可以填充，用一个记号判断是否需要填充左节点
    for val in vals:
        node = TreeNode(val) if val else None # 非空值返回节点类，否则返回 None
        if len(que)==0:
            root = node # 队列为空的话，用 root 记录根结点，用来返回
            que.append(node)
        elif fill_left:
            que[0].left = node
            fill_left = False # 填充过左儿子后，改变记号状态
            if node: # 非 None 值才进入队列
                que.append(node)
        else:
            que[0].right = node
            if node:
                que.append(node)
            que.pop(0) # 填充完右儿子，弹出节点
            fill_left = True #
    return root


class Solution:
    def searchMatrix(self, matrix, target):
        # row=len(matrix)
        # col=len(matrix[0])
        # i=0
        # j=col-1
        # while(i<row and j>=0):
        #     if matrix[i][j]==target:
        #         return True
        #     elif matrix[i][j]>target:
        #         j-=1
        #     else:
        #         i+=1
        # return False

        row = len(matrix)
        col = len(matrix[0])
        res = False
        for i in range(row):
            res = res or self.biSearch(matrix[i], target)

        return res

    def biSearch(self, rowlist, target):
        n = len(rowlist)
        start = 0
        end = n - 1
        res = False
        while (start <= end):
            mid = (start + end) // 2
            if rowlist[mid] == target:
                return True
            elif rowlist[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return res
if __name__ == '__main__':
    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 5
    print(Solution().searchMatrix(matrix,target))
    print("ok")