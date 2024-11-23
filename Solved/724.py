from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sums = 0
        right_sums = sum(nums)

        for i in range(len(nums)):
            right_sums -= nums[i]

            if left_sums == right_sums:
                return i

            left_sums += nums[i]

        return -1


sol = Solution()
print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
