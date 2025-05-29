from itertools import compress
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        group = ""
        for c in chars:
            if c not in group:
                group += c
                group += " "
                group += str(chars.count(c))
                group += " "
        chars = group.split()
        return len(group)

sol = Solution()
print(sol.compress(["a","a","b","b","c","c","c"]))