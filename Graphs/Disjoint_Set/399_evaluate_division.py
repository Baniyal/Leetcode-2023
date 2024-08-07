"""
You are given an array of variable pairs equations and an array of real numbers values,
where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i].
Each Ai or Bi is a string that represents a single variable.

You are also given some queries,
where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
------------------------------------------------------------------------------------------------------------------------
Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0
Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]
Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
"""
from collections import defaultdict
def function(input_arr):
    equations, values, queries = input_arr
    nodes = set()
    graph = defaultdict(list)
    for edges, value in zip(equations, values):
        edge_1, edge_2 = edges
        graph[edge_1].append([edge_2,value]  )
        graph[edge_2].append([edge_1,1/value])
        nodes.add(edge_1)
        nodes.add(edge_2)

    def calculate(source,destination,path,visited):

        if source in visited:
            return -1
        visited.add(source)

        print(f"Source is {source}")
        print(f"Destination is {destination}")
        print(f"Visited is {visited}")
        print(f"Path is {path}")
        print("================================")

        if source == destination:
            return path

        for neighbor in graph[source]:
            neighbor_vertex, neighbor_edge = neighbor
            if neighbor_vertex in visited:
                continue
            print(f"Going to the neighbor {neighbor}")
            result = calculate(neighbor_vertex,destination,path*neighbor_edge,visited)
            if result != -1:
                return result
        return -1

    # result = []
    # for query in queries:
    #     if query[0] in nodes and query[1] in nodes:
    #         result.append(calculate(source=query[0],
    #                   destination=query[1],
    #                   path=1,
    #                   visited=set()))
    #     else:
    #         result.append(-1)
    print(calculate(source="x2",
                      destination="x4",
                      path=1,
                      visited=set()))
    return



TEST_CASES = [

                (   ([["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]],
[3.0,4.0,5.0,6.0],
[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]), [360.00000,0.00833,20.00000,1.00000,-1.00000,-1.00000]),
                (   ([["a","b"],["b","c"]],[2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),   [6.00000,0.50000,-1.00000,1.00000,-1.00000]  ),
                (   ([["a","b"],["b","c"],["bc","cd"]],[1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]),  [3.75000,0.40000,5.00000,0.20000]   ),
                (   ([["a","b"]],[0.5],[["a","b"],["b","a"],["a","c"],["x","y"]]),[0.50000,2.00000,-1.00000,-1.00000] )
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







"""
OPTIMIZED DFS SOLUTION
"""

from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(defaultdict)


# VISITED SET IS UPDATED as in ADD AND REMOVE WHENEVER WE EXIT THE FUNCTION | #TODO: REMEMBER THIS
        def backtrack_evaluate(curr_node, target_node, acc_product, visited):
            visited.add(curr_node)
            ret = -1.0
            neighbors = graph[curr_node]
            if target_node in neighbors:
                ret = acc_product * neighbors[target_node]
            else:
                for neighbor, value in neighbors.items():
                    if neighbor in visited:
                        continue
                    ret = backtrack_evaluate(
                        neighbor, target_node, acc_product * value, visited)
                    if ret != -1.0:
                        break
            visited.remove(curr_node)
            return ret

        # Step 1). build the graph from the equations
        for (dividend, divisor), value in zip(equations, values):
            # add nodes and two edges into the graph
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value

        # Step 2). Evaluate each query via backtracking (DFS)
        #  by verifying if there exists a path from dividend to divisor
        results = []
        for dividend, divisor in queries:
            if dividend not in graph or divisor not in graph:
                # case 1): either node does not exist
                ret = -1.0
            elif dividend == divisor:
                # case 2): origin and destination are the same node
                ret = 1.0
            else:
                visited = set()
                ret = backtrack_evaluate(dividend, divisor, 1, visited)
            results.append(ret)

        return results


"""
OPTIMIZED UNION FIND SOLUTION
"""
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        gid_weight = {}

        def find(node_id):
            if node_id not in gid_weight:
                gid_weight[node_id] = (node_id, 1)
            group_id, node_weight = gid_weight[node_id]
            # The above statements are equivalent to the following one
            #group_id, node_weight = gid_weight.setdefault(node_id, (node_id, 1))

            if group_id != node_id:
                # found inconsistency, trigger chain update
                new_group_id, group_weight = find(group_id)
                gid_weight[node_id] = \
                    (new_group_id, node_weight * group_weight)
            return gid_weight[node_id]

        def union(dividend, divisor, value):
            dividend_gid, dividend_weight = find(dividend)
            divisor_gid, divisor_weight = find(divisor)
            if dividend_gid != divisor_gid:
                # merge the two groups together,
                # by attaching the dividend group to the one of divisor
                gid_weight[dividend_gid] = \
                    (divisor_gid, divisor_weight * value / dividend_weight)

        # Step 1). build the union groups
        for (dividend, divisor), value in zip(equations, values):
            union(dividend, divisor, value)

        results = []
        # Step 2). run the evaluation, with "lazy" updates in find() function
        for (dividend, divisor) in queries:
            if dividend not in gid_weight or divisor not in gid_weight:
                # case 1). at least one variable did not appear before
                results.append(-1.0)
            else:
                dividend_gid, dividend_weight = find(dividend)
                divisor_gid, divisor_weight = find(divisor)
                if dividend_gid != divisor_gid:
                    # case 2). the variables do not belong to the same chain/group
                    results.append(-1.0)
                else:
                    # case 3). there is a chain/path between the variables
                    results.append(dividend_weight / divisor_weight)
        return results