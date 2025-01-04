class Solution:
    def countAndSay(self, n: int) -> str:
        def RLE(s):
            res = []
            f = 1
            curr = s[0]

            for i in range(1, len(s)):
                if s[i] == curr:
                    f += 1
                else:
                    res.append(str(f) + curr)
                    curr = s[i]
                    f = 1

            res.append(str(f) + curr)
            return "".join(res)

        if n == 1:
            return "1"
        return RLE(self.countAndSay(n - 1))

# TC: O(n * 2^n)
# SC: O(2^n)
