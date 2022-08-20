# # Definition for singly-linked list.
# class ListNode():
#     def __init__(self, val):
#         if isinstance(val, int):
#             self.val = val
#             self.next = None
#
#         elif isinstance(val, list):
#             self.val = val[0]
#             self.next = None
#             cur = self
#             for i in val[1:]:
#                 cur.next = ListNode(i)
#                 cur = cur.next
#
#     def gatherAttrs(self):
#         return ", ".join("{}: {}".format(k, getattr(self, k)) for k in self.__dict__.keys())
#
#     def __str__(self):
#         return self.__class__.__name__ + " {" + "{}".format(self.gatherAttrs()) + "}"
#
#
# class Solution:
#     def removeNthFromEnd(self, head, n: int) :
#
#         h=ListNode(0)
#         head=ListNode(head)
#         h.next = head
#         lenli=0
#         s=head
#         p=h
#         while(s):
#             lenli+=1
#             s=s.next
#         k=lenli-n+1
#         # if lenli==1:
#         #     return[]
#         for i in range(1,k):
#             p=p.next
#         p.next=p.next.next
#         return h.next
#
#     # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
#     #     def getLength(head: ListNode) -> int:
#     #         length = 0
#     #
#     #         while head:
#     #             length += 1
#     #             head = head.next
#     #         return length
#     #
#     #
#     #     head = ListNode(head)
#     #     dummy = ListNode(0)
#     #     dummy.next=head
#     #     length = getLength(head)
#     #     cur = dummy
#     #     for i in range(1, length - n + 1):
#     #         cur = cur.next
#     #     cur.next = cur.next.next
#     #     return dummy.next
#     #
#
#
#
# A=Solution()
# A.removeNthFromEnd([1],1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int) :
        def getLength(head) -> int:
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        length = getLength(head)
        cur = dummy
        for i in range(1, length - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next

if __name__ == '__main__':
    h = ListNode(0)
    current = h
    head=[1,2,3]
    for i in head:
        current.next = ListNode(i)
        current = current.next
    h.next=Solution().removeNthFromEnd(h.next,1)
    Solution().removeNthFromEnd(h.next, 3)
    a = []
    current = h.next
    while current:
        a.append(current.val)
        current = current.next
    print(a)