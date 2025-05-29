class Solution:
    def partitionString(self, s: str) -> int:
        rs = [[]]
        count = 0
        for c in s:
            if c not in rs[count]:
                rs[count].append(c)
            else:
                rs.append([])
                count += 1
                rs[count].append(c)

        return count+1


sol = Solution()

print(sol.partitionString("abacaba"))