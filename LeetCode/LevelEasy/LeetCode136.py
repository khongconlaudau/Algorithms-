# 136. Single Number

class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for i in nums:
            result ^= i
        return result