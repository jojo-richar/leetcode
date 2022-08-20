class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return p


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
    l1=[1,2,3]
    for i in l1:
        current.next = ListNode(i)
        current = current.next
    h2 = ListNode(0)
    current2 = h2
    l2=[5,6,1,8,4,5]
    for i in l2:
        current2.next = ListNode(i)
        current2 = current2.next
    print(Solution().reverseList(h1.next))
