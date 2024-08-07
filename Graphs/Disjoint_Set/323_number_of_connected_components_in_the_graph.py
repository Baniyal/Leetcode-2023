"""
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi]
indicates that there is an edge between ai and bi in the graph.
Return the number of connected components in the graph.
"""

from collections import defaultdict

import collections


class UnionFind:

    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.components = size
    def __repr__(self):
        return f"UnionFind({self.root})"

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        root_X = self.find(x)
        root_Y = self.find(y)

        if root_X == root_Y:
            return False
        self.parent[root_X] = root_Y
        self.components -= 1
        return True

    def connected(self, x, y):

        parent_x = self.find(x)
        parent_y = self.find(y)
        print(f"Checking node connectivity for {x} and {y}")
        print(f"Parent of {x} if {parent_x}")
        print(f"Parent of {y} if {parent_y} \n")
        return self.find(x) == self.find(y)

def function(input_arr):
    edges, n = input_arr
    uf = UnionFind(n)

    for A, B in edges:
        uf.union(A, B)
    return uf.components


def dfs_function(input_arr):
    edges, n = input_arr
    graph = defaultdict(list)
    for edge_1, edge_2 in edges:
        graph[edge_1].append(edge_2)
        graph[edge_2].append(edge_1)

    seen = set()
    def dfs(node):
        if node not in seen:
            seen.add(node)
            for neighbor in graph[node]:
                dfs(neighbor)
    connected_component = 0
    for i in range(n):
        if i not in seen:
            dfs(i)
            connected_component += 1
    return connected_component





TEST_CASES = [
                (   ([[0,1],[1,2],[2,3],[3,4]], 5),   1  ),
                (   ([[0,1],[1,2],[3,4]]      , 5),   2   ),

             ]

DEBUG = False


if __name__ == '__main__':
    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"Test Case {test_case} passed")
        else:
            print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break
