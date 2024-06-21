class Solution(object):
    def suggestedProducts(self, products, searchWord):
        resultList, tempList = [], []
        products.sort()
        left, right = 0, len(products) - 1

        for i in range(len(searchWord)):
            c = searchWord[i]

            while left <= right and (len(products[left]) <= i or products[left][i] != c):
                left += 1
            while left <= right and (len(products[right]) <= i or products[right][i] != c):
                right -= 1

            j = right - left + 1 
            mini = min(3, j) 
            for k in range(mini): 
                tempList.append(products[left + k])

            resultList.append(tempList)
            tempList = []
        return resultList

# Beats 98.43% python submissions in runtime
# Beats 72.44% python submissions in memory usage  