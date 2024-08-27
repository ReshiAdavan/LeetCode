class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        graph = {src: [] for src, dst in tickets}
        res = []

        for src, dst in tickets:
            graph[src].append(dst)

        for key in graph:
            graph[key].sort()

        def dfs(graph, result, src):
            if src in graph:
                destinations = graph[src][:]
                while destinations:
                    dest = destinations[0]
                    graph[src].pop(0)
                    dfs(graph, result, dest)
                    destinations = graph[src][:]
            result.append(src)

        dfs(graph, res, "JFK")
        res.reverse()

        if len(res) != len(tickets) + 1:
            return []

        return res
    
# Beats 96.50% of users with Python3 in runtime
# Beats 34.43% of users with Python3 in memory