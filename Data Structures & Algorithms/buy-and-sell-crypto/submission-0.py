class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                mxP = max(mxP, profit)
            else:
                l = r
            r += 1
        return mxP


        
