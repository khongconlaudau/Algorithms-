# class Solution:
#     def searchInsert(self, nums, target):
#         i = 0
#         for i in range(len(nums)):
#             if target == nums[i] or target < nums[i]:
#                 return i
#
#         return i+1
#

# Log(n) cause LinearSearch

class Solution:
    def searchInsert(self, nums, target):
        start, end = 0, len(nums)-1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1

        return start

