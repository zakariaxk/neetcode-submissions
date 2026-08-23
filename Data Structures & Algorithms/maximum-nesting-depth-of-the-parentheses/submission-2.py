class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxd = 0

        for char in s:
            if char == '(':
                stack.append(0)
            elif char == ')':
                maxd = max(maxd, len(stack))
                stack.pop()
            else:
                continue
        
        return maxd