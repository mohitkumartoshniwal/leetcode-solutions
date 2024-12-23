# TC : O(N)
# SC: O(1)
# Since array is sorted, we can ignore the values which exceed the target

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers)-1

        while leftPointer < rightPointer:
            sum = numbers[leftPointer] + numbers[rightPointer]
            if sum < target:
                leftPointer += 1
            elif sum > target:
                rightPointer -=1
            else: 
                return [leftPointer + 1, rightPointer + 1]
        