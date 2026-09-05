class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.digitsSquared(n)

        while slow != fast:
            fast = self.digitsSquared(fast)
            fast = self.digitsSquared(fast)
            slow = self.digitsSquared(slow)

        if fast == 1:
            return True
        else:
            return False

    def digitsSquared(self, n: int) -> int:
        output = 0

        while n:
            digit = n % 10
            output += digit ** 2
            n = n // 10
        return output