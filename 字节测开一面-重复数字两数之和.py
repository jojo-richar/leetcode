from collections import defaultdict
class Solutiou:
    def twosum(self,nums,target):
        res=[]
        n=len(nums)
        hashmap=defaultdict(list)
        for i in range(n):
            if target-nums[i] in hashmap:
                for element in hashmap[nums[target-nums[i]]]:
                    res.append([i,element])


            else:
                hashmap[nums[i]].append(i)

        return res






if __name__ == '__main__':
    nums=[2,7,2,7,11,4,5]
    target = 9
    print(Solutiou().twosum(nums,target))


