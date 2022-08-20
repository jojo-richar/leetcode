class ListNode():
    """定于链表节点"""

    def __init__(self, value):
        self.value = value
        self.next = None


class NodeList():
    """定义链表"""

    def __init__(self):
        self.head = None

    def nodelist_init(self, list0):
        """初始化链表，使用list数据"""
        node_list = []
        for l in list0:
            newnode = ListNode(l)
            node_list.append(newnode)
        for i in range(len(node_list) - 1):
            node_list[i].next = node_list[i + 1]
        node_list[-1].next = None
        self.head = node_list[0]

    def listsort(self):
        """链表排序，可以选择不同的排序方案"""
        s = Solution()
        s.quicksorted(self.head, None)    # 快排

        # s = Solution1()  # 归并排序
        # self.head = s.mergesort(self.head)

    def printListnode(self):
        """输出链表每个节点值"""
        p = self.head
        while p:
            print(p.value)
            p = p.next


class Solution():
    """快排类"""

    def __init__(self):
        pass


    def quicksorted(self, head, end):
        if head != end:
            node = self.partition(head, end)  # 先挖坑填数
            self.quicksorted(head, node)  # 递归调用
            self.quicksorted(node.next, end)  # 递归调用

    def partition(self, head, end):
        p1, p2 = head, head.next  # p2是遍历指针，p1是小数的指针

        while p2 != end:
            if p2.value < head.value:
                p1 = p1.next

                tmp = p2.value
                p2.value = p1.value
                p1.value = tmp
            p2 = p2.next

        tmp = head.value
        head.value = p1.value
        p1.value = tmp

        return p1


class Solution1():
    """归并排序类"""

    def __init__(self):
        pass

    def mergesort(self, head):
        if not head or not head.next:
            """链表为空或仅有一个节点，直接返回结果"""
            return head
        mid = self.getmid(head)

        mer1 = self.mergesort(head)
        mer2 = self.mergesort(right)
        result = self.merge(mer1, mer2)
        return result

    def getmid(self, head):
        """使用快慢指针寻找链表中间节点"""
        fast = head.next
        slow = head

        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        node = slow.next
        slow.next = None  # 切断前后链表
        return node

    def merge(self, head1, head2):
        """对两个链表进行归并，比较两个链表当中的值，合并到一个新的链表当中"""
        dummy = ListNode(-1)
        p = dummy
        p1 = head1
        p2 = head2
        while p1 and p2:
            if p1.value < p2.value:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next
        if p1:
            p.next = p1
        else:
            p.next = p2
        return dummy.next


if __name__ == '__main__':
    """代码直接可以跑，python3."""
    nodelist = NodeList()
    nodelist.nodelist_init([3, 5, 7, 3, 2, 5, 1])
    nodelist.listsort()
    nodelist.printListnode()


