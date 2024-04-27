"""
A tree is an undirected graph in which any two vertices are connected by exactly one path.
In other words, any connected graph without simple cycles is a tree.
Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any node of the tree as the root.
When you select a node x as the root, the result tree has height h.
Among all possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
------------------------------------------------------------------------------------------------------------------------
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
------------------------------------------------------------------------------------------------------------------------
Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
"""
from collections import defaultdict

# 68/71 Test cases passed TLE
def function(input_arr:list)-> int:
    edges,n = input_arr
    if not edges:
        return [x for x in range(n)]
    tree = defaultdict(set)
    for node_1, node_2 in edges:
        tree[node_1].add(node_2)
        tree[node_2].add(node_1)

    while len(tree) > 2:
        leaves = []
        for node in tree:
            if len(tree[node]) == 1:
                leaves.append(node)
        for node in tree.keys():
            for leaf in leaves:
                if leaf in tree[node]:
                    tree[node].remove(leaf)
        for leaf in leaves:
            del tree[leaf]
        print("leaves:", leaves)


    return [*tree.keys()]


# OPTIMIZED SOLUTION

from typing import List
from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]


        adjacency_list = defaultdict(list)
        degree = [0] * n
        for u, v in edges:
            adjacency_list[u].append(v)
            adjacency_list[v].append(u)
            degree[u] += 1
            degree[v] += 1


        leaves = deque([i for i in range(n) if degree[i] == 1])


        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adjacency_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)

        return list(leaves)






TEST_CASES = [
                (([[1,0],[1,2],[1,3]],4),                              [1]            ),
                (([[3,0],[3,1],[3,2],[3,4],[5,4]],6),                 [3,4]           ),
                (([],1),[0]),
                (([],0),[])
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break