# Too slow

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return [max(nums[i : i + k]) for i in range(len(nums) - k + 1)]
