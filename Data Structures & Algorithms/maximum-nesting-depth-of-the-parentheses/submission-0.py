class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxD = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
                maxD = max(maxD, len(stack))
            elif s[i] == ')':
                stack.pop()
            else:
                continue
        return maxD


            