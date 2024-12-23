class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currentSum = 0

        for num in nums:
            # Ordering matters. First remove the negative prefix otherwise [-1] will be left out
            if currentSum < 0:
                currentSum = 0
            currentSum = currentSum + num
            maxSub = max(currentSum, maxSub)

        return maxSub
        