class Solution(object):
    def groupAnagrams(self, strs):
        H = defaultdict(list)
        for s in strs:
            H[str(sorted(s))].append(s)
        return H.values()

# Beats 47.82% python submissions in runtime
# Beats 46.49% python submissions in memory usage  