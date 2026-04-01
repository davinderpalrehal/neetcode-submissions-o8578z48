class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        bought = prices[0]
        last = prices[0]

        for p in prices:
            if p < bought:
                bought = p
            else:
                res = max(res, p - bought)

        return res