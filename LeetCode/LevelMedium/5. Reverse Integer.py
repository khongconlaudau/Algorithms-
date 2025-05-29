class Solution:
    def reverse(self, x: int) -> int:
        rs = str(x)
        if x < 0:
            rs = int(rs[:0:-1]) * -1
        else:
            rs = int (rs[::-1])
        if abs(rs) > (2**31):
            return 0
        return rs

# Runtime: 35ms Beats: 86.75%

class z:
    def maxArea(self, height) -> int:
        area = 0
        rs = 0
        for index, value in enumerate(height):
            if (index * value) > area:
                area = index * value
                rs = value
        return rs ** 2

sol = z()
list = [1, 2, 3 ,4 ,5, 6]
print(sol.maxArea([1,2,1]))