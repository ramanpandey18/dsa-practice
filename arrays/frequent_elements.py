from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arrLen = len(nums)
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        # arrLen = len(nums)
        # if arrLen == 1:
        #     return nums[0]
        # dict = {}
        # resSet = set()
        # for i in range(arrLen):
        #     if nums[i] in dict:
        #         dict[nums[i]] += 1
        #         if dict[nums[i]] >= k:
        #             resSet.add(nums[i])
        #     else:
        #         dict[nums[i]] = 1
        #         if k == 1:
        #             resSet.add(nums[i])
        # return list(resSet)

# dict { 1: 1, 2: 2, 3: 3}
# arr = [1,2]


solution = Solution()
nums = [1,2,2,3,3,3]
k = 2
result = solution.topKFrequent(nums, k)
print("Output:", result)
# Output: [2,3]
# Example 2:

# Input: nums = [7,7], k = 1

# Output: [7]