class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        rs = ""
        for c in t:
            if c in s:
                rs += c

        return t in rs or t == rs

nums = [1,12,-5,-6,50,3]
print(sorted(nums))