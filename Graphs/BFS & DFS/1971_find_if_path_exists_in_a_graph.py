"""
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi]
denotes a bi-directional edge between vertex ui and vertex vi.

Given edges and the integers n, source, and destination,
                            return true if there is a valid path from source to destination, or false otherwise.
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
"""
from collections import defaultdict
def function(input_arr: list) -> int:
    n, edges, source, destination = input_arr
    graph = defaultdict(list)
    for edge_1, edge_2 in edges:
        graph[edge_1].append(edge_2)
        graph[edge_2].append(edge_1)
    def dfs(source,destination,visited):
        print(f"Currently at the node {source}")
        print(f"Nodes visited so far are {visited}")
        print()

        visited.add(source)
        if source == destination:
            return True
        for neighbour in graph[source]:
            if neighbour not in visited:
                if dfs(neighbour,destination,visited):
                    return True

        return False


    return  dfs(source,destination,set())

TEST_CASES = [
                       ((3, [[0,1],[1,2],[2,0]],             0,  2), True ),
                       ((6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0,  5), False)
             ]

DEBUG = False

if __name__ == '__main__':

    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"PASSED")
        else:
            print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break


#-------------------------------------------OPTIMIZED DFS SOLUTION------------------------------------------------------
from typing import List
class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:

        adjacency_list = [[] for _ in range(n)]
        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)

        stack = [start]
        seen = set()

        while stack:
            node = stack.pop()
            if node == end:
                return True

            if node in seen:
                continue
            seen.add(node)

            for neighbor in adjacency_list[node]:
                stack.append(neighbor)

        return False