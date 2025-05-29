# Given a string s consisting of words and spaces, return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s):
        reversed_str = s[::-1].lstrip()
        if " " in reversed_str:
            return reversed_str.find(" ")

        return reversed_str.find(reversed_str[-1]) +1

digits = [4, 3, 2, 1]
result = "".join(map(str, digits))
result = str (int (result) + 1)
print(type (result))