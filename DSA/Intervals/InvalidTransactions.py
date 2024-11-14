from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = {}
        result = set()
        for i, t in enumerate(transactions):
            name, time, amount, city = t.split(",")
            if name not in hashmap:
                hashmap[name] = []
                if int(amount) > 1000:
                    result.add(i)
            else:
                prevTrans = hashmap[name]
                for j in range(len(prevTrans)):
                    _, ptime, _, pcity = transactions[prevTrans[j]].split(",")
                    if int(amount) > 1000:
                        result.add(i)
                    if abs(int(time) - int(ptime)) <= 60 and city != pcity:
                        result.add(i)
                        result.add(prevTrans[j])
            hashmap[name].append(i)
        return [transactions[t] for t in result]
    
# TC: O(n*n)
# SC: O(n)