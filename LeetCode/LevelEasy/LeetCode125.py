class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                result += i
        return result == result[::-1]

