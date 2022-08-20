# 节点类
import heapq
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
    def minMeetingRooms(self, intervals) :
        if not intervals:
            return 0
        freeRooms = []  # 最小堆，储存各个会议的结束时间
        res=1
        intervals.sort(key=lambda x: x[0])  # 对列表按照列表的第一维元素进行排序
        heapq.heappush(freeRooms, intervals[0][1])

        for i in intervals[1:]:
            if i[0] <= freeRooms[0]:
                res += 1
            heapq.heappush(freeRooms,i[1])
        return res

if __name__ == '__main__':
    intervals =[[1,5],[4,6],[7,8].[8,9]]
    print(Solution().minMeetingRooms(intervals))
    print("ok")