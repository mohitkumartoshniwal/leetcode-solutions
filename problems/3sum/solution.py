# https://www.youtube.com/watch?v=jzZsG8n2R9A
# TC: O(N^2)
# SC: depending upon sorting

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        # We are sorting to remove duplicates in the first line of the loop
        nums.sort()

        for index, firstValue in enumerate(nums):
            if index > 0 and nums[index - 1] == firstValue:
                continue
            
            # Basically 2 sum problem then
            leftPointer, rightPointer = index + 1, len(nums) - 1
            while leftPointer < rightPointer:
                ThreeSum = firstValue + nums[leftPointer] + nums[rightPointer]

                if ThreeSum > 0:
                    rightPointer -= 1
                elif ThreeSum < 0:
                    leftPointer +=1
                else:
                    res.append([firstValue, nums[leftPointer], nums[rightPointer]])
                    leftPointer += 1
                    # Extra while loop to remove the duplicates again, it should handle duplicates from the right as well
                    while nums[leftPointer] == nums[leftPointer - 1] and leftPointer < rightPointer: 
                        leftPointer += 1
            
        return res
                
        