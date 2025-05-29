# 9. Palindrome Number

class Solution:
    def isPalindrome(self, x: int) -> bool:
    # convert int to string, and compare the string in forward and backward ways
        s1 = str (int)
        return s1 == s1[::-1]



