from urllib.request import proxy_bypass_registry


class Solution:
    def myAtoi(self, s: str) -> int:
        rs = ''
        index = 0
        for c in s.lstrip():
            if index == 0 and (c == "+" or c == "-"):
                rs += c
            elif c.isdigit():
                rs += c
            else:
                break
            index += 1
        if not rs or (len(rs) == 1 and rs in "+-"):
            return 0
        elif  int(rs) < -(2**31):
            return -(2**31)
        elif int(rs) > (2**31 -1):
            return 2**31 -1
        else:
            return int(rs)

# Runtime: 0ms Beats 100%

