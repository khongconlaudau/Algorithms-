# 169. Majority Element

class Solution:
    def majorityElement(self, nums) -> int:
        s1 = set()
        for i in nums:
            s1.add(i)

        total = 0
        rs = 0
        for i in s1:
            if total < nums.count(i):
                total = nums.count(i)
                rs = i
        return rs

# Runtime: 44 ms. Beats 90.52%