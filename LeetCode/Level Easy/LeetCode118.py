
class Solution:
    def generate(self, numRows: int):
        result = [[] for _ in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                # if j is the first or last elements prepend and append 1
                if j == 0 or j == i:
                    result[i].append(1)
                else:
                    #  if not iterator through the previous array, and adding its elements together(a pair)
                    result[i].append(result[i-1][j-1] + result[i-1][j])
        return result
# Run time: 32ms. Beats ~ 90%
sol = Solution()
print(sol.generate(5))



