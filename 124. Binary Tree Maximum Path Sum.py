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
    def maxPathSum(self, root) :
        def search(root):
            if not root:
                return 0
            rootval=root.val
            left=search(root.left)  #左子树中所能提供的最大值
            right=search(root.right)  #右子树中所能提供的最大值
            innerpath=rootval+left+right  #该根节点情况下所能提供的最大值
            res.append(innerpath)
            outerpath=rootval+max(0,left,right)  #当遍历到这个根节点时考虑此路径的收益
            if outerpath<0:
                return 0
            else:
                return outerpath

        res=[]
        search(root)
        return max(res)




if __name__ == '__main__':
    null=None
    llist=[-10,9,20,null,null,15,7]
    root=generate_tree(llist)
    print(Solution().maxPathSum(root))