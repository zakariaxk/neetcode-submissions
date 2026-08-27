class Solution:
    def findMin(self, nums: List[int]) -> int:
        working = sorted(nums)
        return min(list(working))

        