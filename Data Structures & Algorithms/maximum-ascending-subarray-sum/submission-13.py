class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        maxsub = nums[0]
        if n == 1:
            return nums[0]

        for i in range(n):
            curr = nums[i]
            intermediate = nums[i]
            for j in range(i + 1, n):
                if nums[j] > intermediate:
                    curr += nums[j]
                    maxsub = max(maxsub, curr)
                    intermediate = nums[j]
                else:
                    break
        return maxsub
