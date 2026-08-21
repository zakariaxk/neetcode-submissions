class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        values = [1, 5, 10, 50, 100, 500, 1000]

        mapp = dict(zip(symbols, values))

        valList = list(s)

        for i in range(len(s)):
            valList[i] = mapp[valList[i]]

        valList.append(0)

        total = 0

        for i in range(len(s)):
            if valList[i] < valList[i + 1]:
                total -= valList[i]
            else:
                total += valList[i]

        return total


        