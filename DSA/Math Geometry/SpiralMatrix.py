class Solution(object):
    def spiralOrder(self, matrix):        
        res = []
        l, r = 0, len(matrix[0])
        t, b = 0, len(matrix)
        while l < r and t < b:
            # left to right
            for i in range(l, r):
                res.append(matrix[t][i])
            t += 1
            # top to bottom
            for i in range(t, b):
                res.append(matrix[i][r - 1])
            r -= 1

            # right to left
            for i in range(r - 1, l - 1, -1):
                res.append(matrix[b - 1][i])
            b -= 1
            # bottom to top
            for i in range(b - 1,t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            
        return res[:len(matrix)*len(matrix[0])]

# Beats 83.57% python submissions in runtime
# Beats 89.47% python submissions in memory usage