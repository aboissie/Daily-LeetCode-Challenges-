from typing import List
from queue import PriorityQueue

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Method: build a priority queue where we store the number of stops
        # Each level of the priority queue will store the path and cost of the path
        # We will search for all levels <= k, and take minimum cost among these
        cityFrom = set()
        cityTo = set()
        distances = {}
        for flight in flights:
            cityFrom.add(flight[0])
            cityTo.add(flight[1])
            distances[flight[1]] = {}

        for flight in flights:
            from_, to_, dist_ = flight
            for path in distances[from_]:
                if
                distances[to_]
            if distances[from_] + dist_ < distances[to_]:
                distances[from_]
            distances[to_] = {min()

        flights = sorted(flights, key = lambda x:x[0])
        return flights

if __name__=="__main__":
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1

    print(Solution().findCheapestPrice(n, flights, src, dst, k))
