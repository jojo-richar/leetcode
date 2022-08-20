class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        stack = []
        for i in range(n):
            if (s[i] == '(') or (s[i]=='[') or (s[i]== '{'):
                stack.append(s[i])
            else:
                temp = s[i]
                if not stack:
                    return False
                if ((stack[-1], temp) == ('(', ')')) or ((stack[-1], temp) == ('[', ']')) or (
                        (stack[-1], temp) == ('{', '}')):
                    # or ((stack[-1],temp) ==('[',']')) or ((stack[-1],temp) ==('{','}'))
                    stack.pop()
                else:
                    return False
        if stack == []:
            return True
        else:
            return False


A=Solution()
print(A.isValid('(])'))