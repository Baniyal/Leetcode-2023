"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
------------------------------------------------------------------------------------------------------------------------
Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
------------------------------------------------------------------------------------------------------------------------
Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
------------------------------------------------------------------------------------------------------------------------
"""
from typing import List
from collections import deque
def function(matrix:List[List[int]])-> int:
    number_of_provinces = 0
    def dfs(i):
        visited[i] = True
        for node in range(no_of_cities):
            if not visited[node] and matrix[i][node] == 1:
                dfs(node)

    no_of_cities = len(matrix)
    visited = [False] * no_of_cities

    for i in range(no_of_cities):
        if not visited[i]:
            number_of_provinces += 1
            dfs(i)
            print(f"Visited after processing the city {i}, is {visited}")

    return number_of_provinces


TEST_CASES = [
                (   [[1,1,0],[1,1,0],[0,0,1]],   2   ),
                (   [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]], 1),

                (   [[1,0,0],[0,1,0],[0,0,1]],   3   )
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
