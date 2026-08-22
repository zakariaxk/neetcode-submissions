class Solution:
    def signFunc(self, x:int):
        if x > 0:
            return 1
        elif x == 0:
            return 0
        else:
            return -1


    def arraySign(self, nums: List[int]) -> int:
        prod = math.prod(nums)
        return self.signFunc(prod)