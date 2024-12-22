from typing import List
from collections import defaultdict

class UnionFind:
    # SC: O(n)
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    # TC: O(1) amortized
    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return x

    # TC: O(1) amortized
    def union(self, x1, x2):
        p1, p2 = self.find(x1), self.find(x2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        emailAccount = {} # email -> index

        # TC: O(n)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in emailAccount:
                    uf.union(i, emailAccount[email])
                else:
                    emailAccount[email] = i
            
        # TC: O(n)
        emailGroups = defaultdict(list) # index -> [emails]
        for email, i in emailAccount.items():
            leader = uf.find(i)
            emailGroups[leader].append(email)

        # TC: O(mlogm)
        res = []
        for i, _ in emailGroups.items():
            name = accounts[i][0]
            res.append([name] + sorted(emailGroups[i]))
        return res
    
# TC: O(mlogm) -> m is # of emails total
# SC: O(n) -> n is # of accounts
