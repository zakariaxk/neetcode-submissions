class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while True:
            if n == 1:
                return True
            stringnum = "".join(str(n))
            inplace = 0

            for digit in stringnum:
                inplace += (int(digit) ** 2)
            
            n = inplace
            if n in seen:
                return False
            seen.add(n)
        return False