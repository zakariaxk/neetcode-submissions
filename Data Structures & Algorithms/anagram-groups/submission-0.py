class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for n in strs:
            count = [0] * 26
            for char in n:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
            result[key].append(n)
        return list(result.values())



        
