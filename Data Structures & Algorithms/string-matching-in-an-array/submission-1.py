class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for word in words:
            for possible in words:
                if word != possible and word in possible:
                    res.append(word)
                    break
        return res