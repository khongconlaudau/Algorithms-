from inspect import stack


class Solution:
    def isValid(self, s):
        stack = []
        for c in s:
           if c in "{":
               stack.append("}")
           elif c in "(":
               stack.append(")")
           elif c in "[":
               stack.append("]")
           elif not stack or stack.pop() != c:
               return False
        return not stack


sol = Solution()
print(sol.isValid("([])"))