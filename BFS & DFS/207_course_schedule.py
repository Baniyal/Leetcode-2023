"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first
if you want to take course ai.
For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
------------------------------------------------------------------------------------------------------------------------
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
------------------------------------------------------------------------------------------------------------------------
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it
is impossible.
------------------------------------------------------------------------------------------------------------------------
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""
from collections import defaultdict


def function(input_arr:list, debug:bool) -> bool:
    edges, n = input_arr

    graph = defaultdict(list)
    for end, start in edges:
        graph[start].append(end)

    def recursive(node, visited, stack):
        visited[node], stack[node] = True, True
        for neighbor in graph[node]:
            if  not visited[neighbor] :
                if recursive(neighbor, visited, stack):
                    return True
            elif stack[neighbor]:
                return True
        stack[node] = False
        return False

    visited = [False]*(n+1)
    stack = [False]*(n+1)
    for node in range(n):
        if  not visited[node]:
            if recursive(node,visited,stack):
               return False
    return True

TEST_CASES = [
                (([[1,0]],2), True),
                (([[1,0],[0,1]],2), False)
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break