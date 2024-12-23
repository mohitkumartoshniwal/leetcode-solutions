class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0 # Left Pointer is for buying
        rightPointer = 1 # Right Pointer is for selling
        maxProfit = 0

        while rightPointer < len(prices):
            if prices[leftPointer] < prices[rightPointer]:
                profit = prices[rightPointer] - prices[leftPointer]
                maxProfit = max(profit, maxProfit)
                rightPointer += 1
            else:
                leftPointer = rightPointer
                rightPointer += 1
        
        return maxProfit

        