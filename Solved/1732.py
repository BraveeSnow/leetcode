from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        largest = max(0, gain[0])
        while len(gain) > 1:
            gain[0] += gain.pop(1)
            largest = max(largest, gain[0])

        return largest
