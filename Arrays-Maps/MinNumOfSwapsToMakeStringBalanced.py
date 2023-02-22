class Solution(object):
    def minSwaps(self, s):
        stack_size = 0
        for i in s:
            if i == "[":
                stack_size += 1
            else:
                if stack_size > 0: 
                    stack_size -= 1
        return (stack_size + 1) / 2

# Beats 100.00% python submissions in runtime
# Beats 80.70% python submissions in memory usage
                