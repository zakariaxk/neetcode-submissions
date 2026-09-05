class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest = -1
        for i in range(len(arr) - 1, -1, -1):
            curr = arr[i]
            arr[i] = biggest
            biggest = max(curr, biggest)
        return arr