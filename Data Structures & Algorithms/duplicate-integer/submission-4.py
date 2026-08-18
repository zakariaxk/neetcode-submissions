class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        #unique2 = {}

        for num in nums:
        #for i, num in enumerate(nums):
            if num in unique:
                return True
            
            unique.add(num)
            #unique2[num] = i

        return False

        