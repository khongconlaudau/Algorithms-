from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in nums:
            if k - i  in nums and k - i != i:
                nums.remove(i)
                nums.remove(k - i)
                count += 1
        return count


print(Solution().maxOperations(nums=[3,1,3,4,3], k=6))