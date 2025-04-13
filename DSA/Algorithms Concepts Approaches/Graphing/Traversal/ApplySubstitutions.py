from typing import List

class Solution:
    def find(self, text: str) -> List[str]:
        placeholders, curr, inside = [], [], False
        for char in text:
            # closing '%'
            if char == '%' and inside:
                placeholders.append("".join(curr))
                curr, inside = [], False
            # opening '%'
            elif char == "%":
                inside = True
            # build substr inside pair of %'s
            elif inside:
                curr.append(char)
        return placeholders

    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        adj = {}
        for var, value in replacements:
            placeholders = self.find(value)
            if placeholders:
                adj[var] = placeholders

        cache = {}
        replacements = dict(replacements)

        def dfs(node, vis):
            vis.add(node)
            if node in cache:
                return cache[node]

            val = replacements[node]
            placeholders = self.find(val)

            if not placeholders:
                cache[node] = val
                return val

            res = val
            for p in placeholders:
                v = vis.copy()
                finalVal = dfs(p, v)
                res = res.replace(f"%{p}%", finalVal)

            cache[node] = res
            return res

        result = text
        placeholders = self.find(text)
        for p in placeholders:
            placeholder = f"%{p}%"
            fval = dfs(p, set())
            result = result.replace(placeholder, fval)
        return result

## Let n rep. len(replacements), m rep. len(text), and k rep. max length of a placeholder
# TC: O(m + n^2 * k); m to process text, n^2 worst-case depth of graph per node, k worst-case length of substitute 
# SC: O(n * k); n for the cache, k for length of substitute
