"""
Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows:
graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).
------------------------------------------------------------------------------------------------------------------------
Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


Constraints:

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i (i.e., there will be no self-loops).
All the elements of graph[i] are unique.
The input graph is guaranteed to be a DAG.
"""
from collections import defaultdict
def function(input_arr: list) -> int:
    edges = input_arr
    graph = defaultdict(list)
    for vertex in range(len(edges)):
        graph[vertex].extend(edges[vertex])
    def dfs(source,destination,path,visited):
        if source in visited:
            return
        visited.add(source)
        if source == destination:
            result.append(path + [destination])

        for neighbour in graph[source]:
            if neighbour not in visited:
                dfs(neighbour,destination,path + [source],visited)
        visited.remove(source)

    result = []
    dfs(0,len(edges)-1,[],set())
    return result

TEST_CASES = [
                       ([[1,2],[3],[3],[]], [[0,1,3], [0,2,3]]),
                       ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]])
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


#---------------------------------------------OPTIMIZED-DFS-RECURSIVE---------------------------------------------------
def allPathsSourceTarget(graph):
    n = len(graph)
    src , dest = 0 , n -1
    res = []
    def dfs(src , dest , path):
        if src == dest:
            res.append(path + [dest])
        for node in graph[src]:
            dfs(node,dest,path + [src])

    dfs(src,dest,[])
    return res


#--------------------------------------------------ITERATIVE------------------------------------------------------------
from typing import List


def allPathsSourceTarget(graph: List[List[int]]) -> List[List[int]]:
    def dfs(node):
        path.append(node)
        if node == len(graph) - 1:
            paths.append(path.copy())
            return

        next_nodes = graph[node]
        for next_node in next_nodes:
            dfs(next_node)
            path.pop()

    paths = []
    path = []
    if not graph or len(graph) == 0:
        return paths
    dfs(0)
    return paths