from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        for k in dic:
            if dic[k] > len(nums) //2:
                return k

