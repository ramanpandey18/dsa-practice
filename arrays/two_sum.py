from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numLen = len(nums)
        if numLen <= 1:
            return[]
        dict = {}
        for i in range(0, numLen):
            dict[nums[i]] = i
        print(dict)
        for i in range (0, numLen):
            complement = target - nums[i]
            print("target - nums[i]", target - nums[i])
            if complement in dict:
                if dict[complement] != i:
                    return [i, dict[complement]]
            dict[nums[i]] = i
        return []

solution = Solution()

# Input
nums = [1, 3, 4, 2]
target = 6

# Call the function
result = solution.twoSum(nums, target)

print("Output:", result)