class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        p = 0
        res = 0
        while p < len(s):
            if p + 1 < len(s) and s[p: p + 2] in roman_map:
                res += roman_map[s[p:p + 2]]
                p += 2
            else:
                res += roman_map[s[p]]
                p += 1
        return res

# TC: O(S)
# SC: O(1)
