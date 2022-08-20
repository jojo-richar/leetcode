class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head) :
        temp = head
        listDic = dict()
        while temp:
            tempnode = ListNode(temp.val)
            listDic[tempnode] =temp.val
            temp = temp.next
        ordered=sorted(listDic.items(),key= lambda x: x[1])
        res = ListNode(0)
        dummyhead = res
        for key in ordered:
            dummyhead.next = key[0]
            dummyhead = dummyhead.next

        return res.next




if __name__ == '__main__':
    h1 = ListNode(0)
    current = h1
    l1=[4,2,1,3,2]
    for i in l1:
        current.next = ListNode(i)
        current = current.next
    print(Solution().sortList(h1.next))
