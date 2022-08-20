class Solution:
    def generateParenthesis(self, n: int) :
        def iswellformed(s):
            l = len(s)
            stack = []
            for i in range(l):
                if s[i] == '(':
                    stack.append(s[i])
                else:  # s[i]=')'
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
            if not stack:
                return True
            else:
                return False

        def generate(com):
            if len(com) == 2*n:
                if iswellformed(com):
                    result.append("".join(com))

            else:
                com.append('(')
                generate(com)
                com.pop()

                com.append(')')
                generate(com)
                com.pop()

        result=[]
        # combi=[]
        generate([])
        return result

#
# class Solution:
#     def generateParenthesis(self, n: int) :
#         def generate(A):
#             if len(A) == 2*n:
#                 if valid(A):
#                     ans.append("".join(A))
#             else:
#                 A.append('(')
#                 generate(A)
#                 A.pop()
#                 A.append(')')
#                 generate(A)
#                 A.pop()
#
#         def valid(A):
#             bal = 0
#             for c in A:
#                 if c == '(': bal += 1
#                 else: bal -= 1
#                 if bal < 0: return False
#             return bal == 0
#
#         ans = []
#         generate([])
#         return ans


A=Solution()
print(A.generateParenthesis(3))

# ??
# a=[1,2]
# b=[]
# b.append(a)
# a.pop()