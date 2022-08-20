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
    def __init__(self, ans=None):
        self.ans = TreeNode(0)

    def lowestCommonAncestor(self, root, p,q) :  # 返回以root为根结点的树中（包含root）的某子结点h，使得在h的子树(并包含h)中找到p或q
        # if not root:
        #     return
        # if root.val==q.val or root.val==p.val:
        #     return root
        # left=self.lowestCommonAncestor(root.left,p,q)
        # right=self.lowestCommonAncestor(root.right,p,q)
        # if not left and not right:
        #     return None
        # if not left:
        #     return right
        # elif not right:
        #     return left
        # else:
        #     return root

        def dfs(root, p, q):  # 包含root在内的root的子树中能否找到p或q
            if not root:
                return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if (left and right) or ((root.val == p.val or root.val == q.val) and (left or right)):
                self.ans = root

            return left or right or root.val == q.val or root.val == p.val

        dfs(root, p, q)
        return self.ans
if __name__ == '__main__':
    null=None
    root = [1,2]
    p = [2]
    q = [1]
    root=generate_tree(root)
    p = generate_tree(p)
    q= generate_tree(q)
    print(Solution().lowestCommonAncestor(root,p,q))
    print("ok")