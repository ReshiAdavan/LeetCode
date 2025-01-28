from typing import List

class UnionFind:
    def __init__(self, n):
        self.rank = [1] * n
        self.par = list(range(n))
        self.count = n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        self.count -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        uf = UnionFind(len(nums))
        factorIndex = {}

        for i, n in enumerate(nums):
            factor = 2
            while factor * factor <= n:
                if n % factor == 0:
                    if factor in factorIndex:
                        uf.union(i, factorIndex[factor])
                    else:
                        factorIndex[factor] = i
                    while n % factor == 0:
                        n //= factor
                factor += 1
            if n > 1:
                if n in factorIndex:
                    uf.union(i, factorIndex[n])
                else:
                    factorIndex[n] = i
        return (uf.count == 1)

# TC: O(N * sqrt(N))
# SC: O(N)

from math import gcd

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        nums = set(nums)
        if 1 in nums:
            return False
        if len(nums) == 1:
            return True

        nums = sorted(nums, reverse=True)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if gcd(nums[i], nums[j]) > 1:
                    nums[j] *= nums[i]  # multiply j by i
                    break  # connect j with i ; move to next i
            else:  # if no j found with shared factors
                return False  # not all numbers can connect
        return True

# Far faster sequentially than Union Find
# TC: O(NlogN + N^2)
# SC: O(N)
