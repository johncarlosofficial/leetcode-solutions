class Solution:

    def intToRoman(self, num: int) -> str:
        ans = []
        roman = [
            [1, 'I'],
            [4, 'IV'],
            [5, 'V'],
            [9, 'IX'],
            [10, 'X'],
            [40, 'XL'],
            [50, 'L'],
            [90, 'XC'],
            [100, 'C'],
            [400, 'CD'],
            [500, 'D'],
            [900, 'CM'],
            [1000, 'M'],
        ]

        for i in range(len(roman) - 1, -1, -1):
            while num >= roman[i][0]:
                ans.append(roman[i][1])
                num -= roman[i][0]

        return "".join(ans)
