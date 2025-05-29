import re

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        x = re.findall(p,s)
        if not x:
            return False
        else:
            return True if x[0] == s else False
