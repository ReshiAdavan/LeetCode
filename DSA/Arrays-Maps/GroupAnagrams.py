from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {} # freqMap, str

        for elem in strs:
            sortedStr = "".join(sorted(elem))
            if sortedStr not in table:
                table[sortedStr] = []
            table[sortedStr].append(elem)

        return list(table.values())

# TC: O(N*Klog(K))
# SC: O(N*K)
