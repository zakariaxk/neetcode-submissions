class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique2 = {}

        for i, num in enumerate(nums):
            if num in unique2:
                return True
            
            unique2[num] = i

        return False

        