class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp, m = [[1,1,1,1,1]], (10**9 + 7)
        if n == 1: return 5
        for _ in range(2, n + 1):
            permutationsForA = dp[0][1] + dp[0][2] + dp[0][4] % m
            permutationsForE = dp[0][0] + dp[0][2] % m
            permutationsForI = dp[0][1] + dp[0][3] % m
            permutationsForO = dp[0][2]
            permutationsForU = dp[0][2] + dp[0][3] % m
            dp.append([permutationsForA, permutationsForE, 
                    permutationsForI, permutationsForO, permutationsForU])
            dp.pop(0)
            
        return (sum(dp[0]) % m)
    
# Beats 35.08% python submissions in runtime {O(n) time complexity}
# Beats 85.43% python submissions in memory usage {O(1) space complexity}
        