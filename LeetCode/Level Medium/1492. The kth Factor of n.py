class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        nums = [1]
        for i in range(2, n):
            if n % i == 0:
                nums.append(i)
        if len(nums) < k - 1:
            return -1

        nums.append(n)
        return nums[k - 1]

