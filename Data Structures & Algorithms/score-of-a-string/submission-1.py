class Solution:
    def scoreOfString(self, s: str) -> int:
        n = len(s)
        sum = 0
        for i in range(n-1):
            sum += abs(ord(s[i+1]) - ord(s[i]))
        return sum