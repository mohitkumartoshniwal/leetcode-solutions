# https://www.youtube.com/watch?v=KLlXCFG5TnA&list=PLot-Xpze53leF0FeHz2X0aG3zd0mr1AW_&index=10
# TC: O(N) 
# SC: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index

        for currentIndex, num in enumerate(nums):
            complement = target - num
            if complement in prevMap:
                return [prevMap[complement], currentIndex]
                # The trick is to add the current element after checking
            prevMap[num] = currentIndex
        
        return []  # No solution found
        