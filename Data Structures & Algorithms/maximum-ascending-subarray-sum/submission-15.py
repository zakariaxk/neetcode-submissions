class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        curr = nums[0]
        maxsub = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] <= nums[i - 1]:
                curr = 0
            curr += nums[i]
            maxsub = max(maxsub, curr)
        return maxsub