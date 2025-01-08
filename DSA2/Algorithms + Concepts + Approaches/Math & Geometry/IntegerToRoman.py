class Solution:
    def intToRoman(self, num: int) -> str:
        table = [["M", 1000], ["CM", 900], ["D", 500], ["CD", 400], ["C", 100], ["XC", 90], ["L", 50], 
            ["XL", 40], ["X", 10], ["IX", 9], ["V", 5], ["IV", 4], ["I", 1]]

        romanNumeralConversion = ""
        for ch, divisor in table:
            numChars = num // divisor
            if numChars:
                romanNumeralConversion = romanNumeralConversion + (numChars * ch)
                num %= divisor
        return romanNumeralConversion

# TC: O(n)
# SC: O(1)