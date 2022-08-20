class Solution:
    def sumOddLengthSubarrays(self, arr) :
        n=len(arr)
        oddl=(n-1)//2
        oddLen=[2*n+1 for n in range(oddl+1)]
        sum=0
        for arrlen in oddLen:
            for i in range(n):
                templ=arrlen
                tempi=i
                if tempi+templ-1<n:
                    while(templ):
                        sum+=arr[tempi]
                        tempi+=1
                        templ-=1
        return sum
if __name__ == '__main__':
    arr = [1,4,2,5,3]
    print(Solution().sumOddLengthSubarrays(arr))
