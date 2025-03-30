class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        subsets = []

        def generateSubsets(i, subset):
            if i >= len(tiles):
                if subset:
                    subsets.append(subset[::])
                return

            generateSubsets(i + 1, subset + [tiles[i]])
            generateSubsets(i + 1, subset)

        generateSubsets(0, [])

        permutations = set()

        def generatePermutations(i, perm):
            if i >= len(perm):
                strPerm = "".join(perm)
                if strPerm not in permutations:
                    permutations.add(strPerm)
                    return

            for j in range(i, len(perm)):
                perm[i], perm[j] = perm[j], perm[i]
                generatePermutations(i + 1, perm)
                perm[i], perm[j] = perm[j], perm[i]

        for subset in subsets:
            generatePermutations(0, subset)
        return len(permutations)

# TC: O(2^n + 2^n * n! * n)
# SC: O(2^n * n!)

from collections import Counter

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        def backtrack():
            count = 0
            for char in counter:
                if counter[char] > 0:
                    counter[char] -= 1
                    count += (1 + backtrack())
                    counter[char] += 1
            return count

        return backtrack()
    
# TC: O(2^n)
# SC: O(n)
