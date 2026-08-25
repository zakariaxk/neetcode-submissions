class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        ct = 0
        cs = 0
        while(cs < len(s) and ct < len(t)):
            if s[cs] == t[ct]:
                if cs == (len(s) - 1):
                    return True
                else:
                    cs += 1
                    ct += 1
            else:
                ct += 1
        return False