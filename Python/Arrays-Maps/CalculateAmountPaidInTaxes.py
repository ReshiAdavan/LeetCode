class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        tax = prev = 0
        for upper, p in brackets:
            if income >= upper:
                tax += (upper - prev) * p / 100
                prev = upper
            else:
                tax += (income - prev) * p / 100
                return tax
        return tax

# Beats 86.09% of users with Python3 in runtime
# Beats 58.06% of users with Python3 in memory