# 121. Best Time to Buy and Sell Stock

class Solution:
    def maxProfit(self, prices) -> int:
        best_price = prices[0]
        max_profit = 0

        for i in prices[1:]:
            if best_price > i:
                best_price = i

            max_profit = max(max_profit, i - best_price)
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
