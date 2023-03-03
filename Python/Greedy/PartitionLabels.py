class Solution(object):
    def partitionLabels(self, s):
        H = {}

        for n in s:
            if n in H: H[n] += 1
            else: H[n] = 1

        contenders, partitionSizes = [], []
        partitionCount, i = 0, 0

        while i < len(s):
            c = s[i]
            H[c] -= 1
            if c not in contenders:
                contenders.append(c)
            partitionCount += 1

            if H[c] == 0: 
                contenders.remove(c)

            if len(contenders) == 0 and partitionCount > 0:
                partitionSizes.append(partitionCount)
                partitionCount = 0
            i += 1
        
        return partitionSizes

# Beats 75.49% python submissions in runtime
# Beats 67.97% python submissions in memory usage