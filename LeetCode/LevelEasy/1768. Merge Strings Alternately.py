class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rs = ""
        for c in range(0, min(len(word1), len(word2))):
            rs += word1[c]
            rs += word2[c]
        if (len(word1) == len(word2)):
            return rs
        if (len(word1) > len(word2)):
            for c in range(len(word2), len(word1)):
                rs += word1[c]
        else:
            for c in range(len(word1), len(word2)):
                rs += word2[c]
        return rs

#  33ms Beat 72%