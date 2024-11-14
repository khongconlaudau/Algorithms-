from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rs = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            rs[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            rs[i] *= right
            right *= nums[i]
        return rs

