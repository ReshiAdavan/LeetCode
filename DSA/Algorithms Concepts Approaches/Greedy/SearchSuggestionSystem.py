from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = set(products)
        results = []

        for i in range(len(searchWord)):
            removals = set()

            for product in products:
                if searchWord[:i + 1] != product[:i + 1]:
                    removals.add(product)

            for product in removals:
                products.remove(product)

            results.append(sorted(products)[:3])
        return results

# N rep. len(searchWord), M rep. len(products)
# TC: O(N * MlogM)
# SC: O(N * M)
