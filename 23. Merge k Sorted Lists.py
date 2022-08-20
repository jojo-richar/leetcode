class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        global l3

        def linklist2list(head):
            lista=[]
            current = head
            while current:
                lista.append(current.val)
                current = current.next
            return lista

        def list2linklist(alist):
            if type(alist) == list:
                h = ListNode(0)
                current = h
                for i in lists[0]:
                    current.next = ListNode(i)
                    current = current.next
                l = h.next
                return l


        def mergetwolists(l1, l2):

            if type(l1) == list:
                h1 = ListNode(0)
                current1 = h1
                for i in l1:
                    current1.next = ListNode(i)
                    current1 = current1.next
                l1 = h1.next

            if type(l2) == list:
                h2 = ListNode(0)
                current2 = h2
                for i in l2:
                    current2.next = ListNode(i)
                    current2 = current2.next
                l2 = h2.next

            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            elif l1.val <= l2.val:
                l1.next=mergetwolists(l1.next, l2)
                return l1
            else:
                l2.next=mergetwolists(l1, l2.next)
                return l2

        k = len(lists)
        if k==0:
            return None
        for i in range(k):
            if lists[i] is None:
                lists.remove(lists[i])
        k = len(lists)
        if k==0:
            return None
        if k ==1:
            # a=ListNode(None)
            a=ListNode(lists[0])
            return a


        for i in range(k - 1):
            templist = mergetwolists(lists[k - 1 - i], lists[k - 2 - i])
            lists[k - 2 - i]= linklist2list(templist)
        if type(lists[0]) == list:
            h3 = ListNode(0)
            current3 = h3
            for i in lists[0]:
                current3.next = ListNode(i)
                current3 = current3.next
            l3 = h3.next
        return l3



if __name__ == '__main__':
    A=Solution()
    print(A.mergeKLists([[1]]))

