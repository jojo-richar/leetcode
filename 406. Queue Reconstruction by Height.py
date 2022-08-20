class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        people=sorted(people,key= lambda x:(-x[0],x[1]))
        for p in people:
            if len(res)<=p[1]:
                res.append(p)
            else:
                res.insert(p[1],p)
        return res
if __name__ == '__main__':
    people = [[7,0],[4,1],[7,1],[5,0],[6,1],[5,2]]

    print(Solution().reconstructQueue(people))
