# 节点类
class Node(object):
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
        node = Node(val) if val else None # 非空值返回节点类，否则返回 None
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
    def __init__(self) -> None:
        self.n=0
        self.res=0
    def kthLargest(self, root, k: int) -> int:
        def inordersearch(root):
            if not root:
                return
            inordersearch(root.right)
            if self.n==0:return
            if  root:
                self.n-=1
            if self.n==0:
                self.res=root.val
            inordersearch(root.left)
            if self.n == 0: return

        self.n=k
        inordersearch(root)
        return self.res

if __name__ == '__main__':
    null = None
    root = [3, 1, 4, null, 2]
    k = 1
    tree=generate_tree(root)
    print(Solution().kthLargest(tree,k))
