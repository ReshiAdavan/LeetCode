from collections import deque, defaultdict
from typing import List

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        adj = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                adj[stop].append(i)

        queue = deque([source])
        visited_stops = set([source])
        visited_routes = set()
        count = 0

        while queue:
            for _ in range(len(queue)):
                curr_stop = queue.popleft()
                if curr_stop == target:
                    return count
                for route_index in adj[curr_stop]:
                    if route_index not in visited_routes:
                        visited_routes.add(route_index)
                        for stop in routes[route_index]:
                            if stop not in visited_stops:
                                visited_stops.add(stop)
                                queue.append(stop)
            count += 1
        return -1

# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
