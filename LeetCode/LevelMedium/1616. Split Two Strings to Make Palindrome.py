class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        length = len(a)
        if length == 1:
            return True
        for i in range(length):
            print(f"a{i}: ",a[0:i])
            print(f"b{i}: ",b[i:length][::-1])
            if a[0:i] == b[i:length][::-1] or a[i:length] == b[0:i][::-1]:
                return True
        return False

sol = Solution()
# b="jizalu"
print(sol.checkPalindromeFormation(a="ulacfd", b="jizalu"))
# print(b[1:len(b)][::-1])