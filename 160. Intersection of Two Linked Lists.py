class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def reverselist(link):
            if not link.next:
                return link
            pre = link
            cur = link.next
            pre.next = None
            while cur:
                temp = cur.next
                cur.next = pre
                pre =cur
                cur = temp
            return pre

        head1=reverselist(headA)
        head2=reverselist(headB)
        res=0
        while(head1 and head2):
            if head1.val==head2.val:
                res=head1.val
            head1=head1.next
            head2=head2.next
        return res
    # def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    #     hashset=set()
    #     while(headA):
    #         hashset.add(headA)
    #         headA=headA.next
    #
    #     while(headB):
    #         if headB in hashset:
    #             return headB
    #         headB=headB.next
    #     return 0






if __name__ == '__main__':
    h1 = ListNode(0)
    current = h1
    l1=[4,1,8,4,5]
    for i in l1:
        current.next = ListNode(i)
        current = current.next
    h2 = ListNode(0)
    current2 = h2
    l2=[5,6,1,8,4,5]
    for i in l2:
        current2.next = ListNode(i)
        current2 = current2.next
    print(Solution().getIntersectionNode(h1.next,h2.next))
