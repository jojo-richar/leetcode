class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head) :
        # if not head:
        #     return None
        # traversNode=head
        # pre=traversNode
        # cur=traversNode.next
        # while(pre and cur):
        #     if  pre.next:
        #         tempPrenode=pre.next.next
        #     else:
        #         tempPrenode=None
        #     if  cur.next:
        #         tempCurnode=cur.next.next
        #     else:
        #         tempCurnode=None
        #     pre.next=cur.next
        #     pre=cur.next
        #     pre=tempPrenode
        #     cur=tempCurnode
        # return pre
        if not head and not head.next:
            return None
        newhead=head.next
        head.next=swapPairs(newhead.next)
        newhead.next=head

        return newhead





if __name__ == '__main__':
    h1 = ListNode(0)
    current = h1
    l1=[1,2,3,4]
    for i in l1:
        current.next = ListNode(i)
        current = current.next
    print(Solution().swapPairs(h1.next))
