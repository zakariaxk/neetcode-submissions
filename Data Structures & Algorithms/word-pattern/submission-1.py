class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        if len(pattern) != len(words):
            return False

        pat = {}
        used = set()

        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]

            if char in pat:
                if pat[char] != word:
                    return False
            
            else:
                if word in used:
                    return False

                pat[char] = word
                used.add(word)
        
        return True