from typing import List
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        response = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            response[tuple(count)].append(s)
        return list(response.values())

solution = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
result = solution.groupAnagrams(strs)
print("Output:", result)