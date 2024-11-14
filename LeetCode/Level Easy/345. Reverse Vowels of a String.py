class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiou"
        container = ""
        rs = ""
        for c in s:
            if c.lower() in vowels:
                container += c
        index = len(container) - 1
        for c in s:
            if c.lower() in vowels:
                rs += container[index]
                index -= 1
            else:
                rs += c
        return rs
# Faster Solution
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         vowels=[i for i in s if i in "aeiouAEIOU"]
#         result=[i if i not in "aeiouAEIOU" else vowels.pop() for i in s]
#         return "".join(result)
