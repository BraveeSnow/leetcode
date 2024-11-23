"""
1207. Unique Number of Occurrences
Easy
Topics
Companies
Hint

Given an array of integers arr, return true if the number of occurrences of each value in the array
is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number
of occurrences.

Example 2:

Input: arr = [1,2]
Output: false

Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

 

Constraints:

    1 <= arr.length <= 1000
    -1000 <= arr[i] <= 1000

Runtime
0ms
Beats100.00%

Memory
16.62MB
Beats76.22%
"""

from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hashmap = defaultdict(lambda: 0)
        for val in arr:
            hashmap[val] += 1

        counts = [0] * (max(hashmap.values()) + 1)
        for val in hashmap.values():
            if counts[val] == 1:
                return False
            counts[val] = 1

        return True


sol = Solution()
print(sol.uniqueOccurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))
