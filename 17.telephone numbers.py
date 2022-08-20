# class Solution:
#     def letterCombinations(self, digits: str) :
#         if not digits:
#             return list()
#
#         phoneMap = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }
#
#         def backtrack(index: int):
#             if index == len(digits):
#                 combinations.append("".join(combination))
#             else:
#                 digit = digits[index]
#                 for letter in phoneMap[digit]:
#                     combination.append(letter)
#                     backtrack(index + 1)
#                     combination.pop()
#
#         combination = list()
#         combinations = list()
#         backtrack(0)
#         return combinations
# A=Solution()
# re=A.letterCombinations('23')
#
#
class Solution:
    def letterCombinations(self, digits: str) :
        if not digits: return []
        phone = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        queue = ['']  # 初始化队列
        for digit in digits:
            for _ in range(len(queue)):
                tmp = queue.pop(0)
                for letter in phone[ord(digit)-50]:# 这里我们不使用 int() 转换字符串，使用ASCII码
                    queue.append(tmp + letter)
        return queue

A=Solution()
re=A.letterCombinations('253')