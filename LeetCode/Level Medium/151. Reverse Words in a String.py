class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split()
        rs = " ".join(arr[::-1])
        return rs