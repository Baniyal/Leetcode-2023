"""
You are given an m x n grid where each cell can have one of three values:
                            - 0 representing an empty cell,
                            - 1 representing a fresh orange, or
                            - 2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens
             4-directionally.
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
"""
from collections import deque

def function(arr:list)-> int:
    return None

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    result = 0
    fresh_oranges = 0
    rotten_positions = deque([])
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                rotten_positions.append([i, j, 0])
            if grid[i][j] == 1:
                fresh_oranges += 1
    visited = [[False] * n for _ in range(m)]
    while rotten_positions:

        curr_rotten_orange = rotten_positions.popleft()


        cro_x, cro_y, temp = curr_rotten_orange
        if visited[cro_x][cro_y]:
            continue
        visited[cro_x][cro_y] = True
        print("curr_rotten_orange---------->", curr_rotten_orange[:2])

        print("rotten_positions ----------->", rotten_positions)

        print("max time so far------------->", result)
        print("fresh oranges left---------->", fresh_oranges)

        print("visited array -------------->", visited)
        result = max(temp, result)
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            nro_x, nro_y = cro_x + x, cro_y + y
            if 0 <= nro_x < m and 0 <= nro_y < n and visited[nro_x][nro_y] == False and grid[nro_x][nro_y] == 1 and grid[nro_x][nro_y] != 2:
                if [nro_x, nro_y, temp + 1] in rotten_positions : continue
                rotten_positions.append([nro_x, nro_y, temp + 1])
                fresh_oranges -= 1

        print("\n")
    print("FRESH",fresh_oranges)
    if fresh_oranges > 0:
        return -1
    return result




TEST_CASES = [
                (   [[2,1,1],[1,1,0],[0,1,1]],   4   ),
                (   [[2,1,1],[0,1,1],[1,0,1]],  -1   ),
                (   [[0,2]]                  ,   0   )
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