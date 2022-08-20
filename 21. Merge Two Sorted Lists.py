class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

 #递归版
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

#遍历版
# class Solution:
#     def mergeTwoLists(self, l1, l2):
#         # def getLength(head) -> int:
#         #     length = 0
#         #     while head:
#         #         length += 1
#         #         head = head.next
#         #     return length
#
#         dummy1=ListNode(0,l1)
#         dummy2=ListNode(0,l2)
#         resultlist=ListNode(0)
#         dummy0=resultlist
#         head1=dummy1.next
#         head2=dummy2.next
#         while(head1 or head2):
#             if not (head1 and head2):
#                 if head1:
#                     tempnode = ListNode(head1.val)
#                     resultlist.next=tempnode
#                     resultlist=resultlist.next
#                     head1=head1.next
#                 else:
#                     tempnode = ListNode(head2.val)
#                     resultlist.next=tempnode
#                     resultlist = resultlist.next
#                     head2=head2.next
#             else:
#                 if head1.val>=head2.val:
#                     tempnode=ListNode(head2.val)
#                     resultlist.next=tempnode
#                     resultlist = resultlist.next
#                     head2=head2.next
#                 else:
#                     tempnode = ListNode(head1.val)
#                     resultlist.next=head1
#                     resultlist = resultlist.next
#                     head1=head1.next
#         return dummy0.next



if __name__ == '__main__':
    h1 = ListNode(0)
    current = h1
    l1=[1,3,4]
    for i in l1:
        current.next = ListNode(i)
        current = current.next
    h2 = ListNode(0)
    current2 = h2
    l2=[2,6]
    for i in l2:
        current2.next = ListNode(i)
        current2 = current2.next
    result=Solution().mergeTwoLists(h1.next,h2.next)
    print('suc')
