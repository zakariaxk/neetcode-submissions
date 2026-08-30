class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}

        for num in nums:
            freq_counter[num] = freq_counter.get(num, 0) + 1


        sorted_nums = sorted(freq_counter.keys(), key=lambda num: freq_counter[num], reverse = True)

        return sorted_nums[:k]
        # n = len(nums)
        # buckets = [0] * n

        # for i, num in enumerate(nums):
        #     buckets