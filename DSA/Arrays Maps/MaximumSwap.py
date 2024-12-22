## Two pass

class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        N = len(str(num))

        max_indexes = [0] * N
        max_indexes[-1] = N - 1

        for i in range(N - 2, -1, -1):
            if int(n[i]) > int(n[max_indexes[i + 1]]):
                max_indexes[i] = i
            else:
                max_indexes[i] = max_indexes[i + 1]

        for i in range(N):
            if int(n[i]) < int(n[max_indexes[i]]):
                n[i], n[max_indexes[i]] = n[max_indexes[i]], n[i]
                return int("".join(n))
        return num
    
# TC: O(n)
# SC: O(n)

## One pass

class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        N = len(str(num))

        best = N - 1
        left = -1
        right = -1

        for i in range(N - 2, -1, -1):
            if int(n[i]) > int(n[best]):
                best = i
            elif int(n[i]) < int(n[best]):
                left = i
                right = best

        if left != -1:
            n[left], n[right] = n[right], n[left]
            return int("".join(n))
        return num
    
# TC: O(n) 
# SC: O(n)




