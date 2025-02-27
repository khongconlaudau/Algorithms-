from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        count = 1
        j = 1
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        
        return j

#  Better solution (LeetCode Solution)

# class Solution:
#     int k = 2;

#     for i in range(2, len(nums)):
#         if nums[i] != nums[k-2]:
#             nums[k] = nums[i]
#             k +=1 
#     return k