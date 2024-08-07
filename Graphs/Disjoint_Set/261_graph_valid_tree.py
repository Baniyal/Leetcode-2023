"""
You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.
------------------------------------------------------------------------------------------------------------------------
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true
------------------------------------------------------------------------------------------------------------------------
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false
"""
import collections


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

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
        if not uf.union(A, B):
            return False
    return True


    return True

def function(input_arr):
    edges, n = input_arr
    if len(edges) != n-1: return False
    adj_list = [[] for _ in range(n)]
    for edge_1,edge_2 in edges:
        adj_list[edge_1].append(edge_2)
        adj_list[edge_2].append(edge_1)

    stack = [0]
    seen = set()
    seen.add(0)

    while stack:
        node = stack.pop()
        for neighbor_node  in adj_list[node]:
            if neighbor_node in seen: return False
            stack.append(neighbor_node)
            seen.add(neighbor_node)

            adj_list[neighbor_node].remove(node)

    return seen == n



def parent_approach(n):
    parent = {0: -1}
    stack = [0]
    adj_list = [[] for _ in range(n)]
    while stack:
        node = stack.pop()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]:
                continue
            if neighbour in parent:
                return False
            parent[neighbour] = node
            stack.append(neighbour)

    return len(parent) == n


def recursive_function( n: int, edges) -> bool:
    if len(edges) != n - 1: return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    seen = set()

    def dfs(node, parent):
        if node in seen: return;
        seen.add(node)
        for neighbour in adj_list[node]:
            if neighbour == parent:
                continue
            if neighbour in seen:
                return False
            result = dfs(neighbour, node)
            if not result: return False
        return True

    # We return true iff no cycles were detected,
    # AND the entire graph has been reached.
    return dfs(0, -1) and len(seen) == n


def iterative_bfs( n: int, edges) -> bool:

    if len(edges) != n - 1: return False

    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    parent = {0: -1}
    queue = collections.deque([0])

    while queue:
        node = queue.popleft()
        for neighbour in adj_list[node]:
            if neighbour == parent[node]:
                continue
            if neighbour in parent:
                return False
            parent[neighbour] = node
            queue.append(neighbour)

    return len(parent) == n

from typing import List
def recursive_DFS(self, n: int, edges: List[List[int]]) -> bool:
    if len(edges) != n - 1: return False

    # Create an adjacency list.
    adj_list = [[] for _ in range(n)]
    for A, B in edges:
        adj_list[A].append(B)
        adj_list[B].append(A)

    # We still need a seen set to prevent our code from infinite
    # looping if there *is* cycles (and on the trivial cycles!)
    seen = set()

    def dfs(node):
        if node in seen: return
        seen.add(node)
        for neighbour in adj_list[node]:
            dfs(neighbour)

    dfs(0)
    return len(seen) == n

TEST_CASES = [
                (   ([[0,1],[1,2],[2,3],[1,3],[1,4]], 5),   False  ),
                (   ([[0,1],[0,2],[0,3],[1,4]]      , 5),   True   ),

             ]

DEBUG = True


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
