class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while(n != 1 or n != 10 or n != 100 or n != 1000):
            stringnum = "".join(str(n))
            inplace = 0

            for digit in stringnum:
                inplace += (int(digit) ** 2)
            
            n = inplace
            if n == 1 or n == 10 or n == 100 or n == 1000:
                return True
            if n in seen:
                return False
            seen.add(n)
        return False