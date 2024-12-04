from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        length = len(nums) -1 

        for i in range(k , -1, -1):
            nums[i], nums[length] = nums[length], nums[i]
            length -= 1

nums = [99,-1,-100,3]
sol = Solution()
sol.rotate(nums,2)

print(nums)
        