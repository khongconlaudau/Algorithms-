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

s1 = "Hello World"
print(s1.count("o"))


class Solution:
    def hammingWeight(self, n: int) -> int:
        index = findIndex(n)
        step = 0
        if index == 1:
            return 1
        else:
            for i in range(index - 1, -1, -1):
                if n >= 2 ** i:
                    n -= 2 ** i
                    step += 1
        return step


def findIndex(n) -> int:
    for i in range(1, 32):
        if (2 ** i) == n:
            return 1
        elif (2 ** i) > n:
            return i
