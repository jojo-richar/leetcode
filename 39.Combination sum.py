class Solution:
    def combinationSum(self, candidates, target) :
        # def backtrack(candidates, index, combi, target, result):
        #     if target - candidates[index] == 0:
        #         combi.append(candidates[index])
        #         result.append(combi[:])
        #         combi.pop()
        #         backtrack(candidates, index + 1, combi, target, result)
        #
        #     if index <= len(candidates) - 1 and ((target - candidates[dinex]) >= min(candidates)):
        #         combi.append(candidates[index])
        #         backtrack(candidates, index, combi, target - candidates[index], result)
        #         combi.pop()
        #         backtrack(candidates, index + 1, combi, target+candidates[index], result)
        #     else:
        #         backtrack(candidates, index + 1, combi, target, result)
        def backtrack(index,res):
            if index >=len(candidates) or res>=target:
                if res==target:
                    result.append(temp[:])
                return

            temp.append(candidates[index])
            backtrack(index,res+candidates[index])
            temp.pop()
            backtrack(index+1,res)

        temp = []
        result = []
        backtrack(0, 0)
        return  result
        pass

Solution().combinationSum([2,3,6,7],7)