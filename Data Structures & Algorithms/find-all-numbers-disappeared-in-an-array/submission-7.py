class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        storage = set(range(1, len(nums) + 1))

        for num in nums:
            storage.discard(num)

        return list(storage)