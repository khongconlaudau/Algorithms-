# 70. Climbing stairs

class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [0] * 46
        for i in range(46):
            if i < 3:
                arr[i] = i + 1
            else:
                arr[i] = arr[i - 1] + arr[i - 2]
        return arr[n-1]

sol = Solution()
print(sol.climbStairs(6))



