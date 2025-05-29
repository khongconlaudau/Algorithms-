from typing import List

class Solution:
    # def canJump(self, nums:List[int]) -> bool:
    #     li = len(nums)
    #     max_reach = 0 
        
    #     for index, jump_length in enumerate(nums):
    #         if max_reach == li:
    #             return True
            
    #         if index > max_reach:
    #             return False 
            
    #         max_reach = max(max_reach, index + jump_length)
        
    #     return True
    
    
    # 2nd way to solve this solution 
    def canJump(self, nums:List[int]) -> bool:
        goal = len(nums) - 1
        
        for i in range(len(nums)- 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False