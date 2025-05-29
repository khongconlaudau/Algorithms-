from typing import List


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        length = len(nums)

        p_outlier = nums[length - 2: length]
        if p_outlier[0] == p_outlier[1]:
            return p_outlier[0]
        total = 0
        for i in range(length - 2):
            total += nums[i]

        return p_outlier[0] if p_outlier[0] == total else p_outlier[1]

sol = Solution()
print(sol.getLargestOutlier([2,3,5,10]))