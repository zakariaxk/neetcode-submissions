class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seena = {}
        seenb = {}

        for i in range(len(s)):
            a = s[i]
            b = t[i]

            if a in seena and seena[a] != b:
                return False
            
            if b in seenb and seenb[b] != a:
                return False
            
            seena[a] = b
            seenb[b] = a
        return True
        