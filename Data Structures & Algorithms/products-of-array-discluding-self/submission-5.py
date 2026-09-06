class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        product = 1
        zeros = 0

        for num in nums:
            if num:
                product *= num
            else:
                zeros += 1
        if zeros > 1:
            return [0] * n
        elif zeros == 1:
            for i, num in enumerate(nums):
                if not num:
                    output[i] = product
                else:
                    output[i] = 0
            return output
        else:
            for i, num in enumerate(nums):
                output[i] = product // num
            return output
        