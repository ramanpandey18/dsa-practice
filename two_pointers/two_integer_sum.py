from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n <= 1:
            return numbers
        p1 = 0
        p2 = n-1
        while p1 < p2:
            sum = numbers[p1] + numbers[p2]
            print("sum:", sum)
            print("p1 p2 are", p1, p2)
            if sum == target:
                print("target found", numbers[p1], numbers[p2])
                # return [numbers[p1], numbers[p2]]
                return [p1+1, p2+1]
            elif sum < target:
                print("sum less than target")
                p1 += 1
            else:
                print("sum greater than target")
                p2 -=1
            print("p1 p2 are", p1, p2)

solution = Solution()
numbers = [1,2,3,4]
target = 3
# Output: [1,2]
numbers=[2,3,4]
target=6
# Output: [1,3]
result = solution.twoSum(numbers, target)
print("Output:", result)