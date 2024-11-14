class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = 0
        sum = 0
        rs = []
        for i in candies:
            maxCandy = max(maxCandy,i)
        for i in candies:
            sum = i+ extraCandies
            if( sum >= maxCandy):
                rs.append(True)
            else:
                rs.append(False)
        return rs

# 0ms. Beats 100%