# def linklist2list(head):
#     lista = []
#     current = head
#     while current:
#         lista.append(current.val)
#         current = current.next
#     return lista
#
#
# def list2linklist(alist):
#     if type(alist) == list:
#         h = ListNode(0)
#         current = h
#         for i in alist:
#             current.next = ListNode(i)
#             current = current.next
#         l = h.next
#         return l
class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 如果不加self，表示是类的一个属性(可以通过"类名.变量名"的方式引用),加了self表示是类的实例的一个属性(可以通过"实例名.变量名"的方式引用)

class Solution:
    def linklist2list(self,head):
        lista = []
        current = head
        while current:
            lista.append(current.val)
            current = current.next
        return lista

    def list2linklist(self,alist):
        if type(alist) == list:
            h = ListNode(0)
            current = h
            for i in alist:
                current.next = ListNode(i)
                current = current.next
            l = h.next
            return l
    def mergeKLists(self, lists):
        import heapq
        dummy = ListNode(0)
        p = dummy
        head = []
        for i in range(len(lists)):
            if lists[i] :
                heapq.heappush(head, (lists[i].val, i))  #对于二维数据（x,y）就比较x的值，保证堆顶是x最小的二维向量
                lists[i] = lists[i].next
        while head:
            val, idx = heapq.heappop(head)
            p.next = ListNode(val)
            p = p.next
            if lists[idx]:
                heapq.heappush(head, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next


if __name__ == '__main__':
    A=Solution()
    lists=[A.list2linklist([3,5]),A.list2linklist([1,3,4]),A.list2linklist([-2,6]),A.list2linklist([-5,6])]
    print(A.mergeKLists(lists))

