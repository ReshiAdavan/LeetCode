class Solution:
    def customSortString(self, order: str, s: str) -> str:
        mapping = {c: i for i, c in enumerate(order)}

        def customKey(c):
            return mapping.get(c, len(order))

        return "".join(sorted(s, key=customKey))

# TC: O(nlogn)
# SC: O(n)
