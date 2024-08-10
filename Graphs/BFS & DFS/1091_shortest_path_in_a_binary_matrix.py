"""
Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[0,1],[1,0]]
Output: 2
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
"""
import collections


def function(input_arr):
    grid = input_arr
    m, n = len(grid), len(grid[0])
    visited = [[False]*n for _ in range(m)]
    def is_valid(x,y):
        if (0 <= x < m) and (0 <= y < n) and visited[x][y] == False and grid[x][y] == 0:
            return True
        return False

    if grid[0][0] == 1:
        return  -1
    queue = collections.deque([[0,0]])
    destination = [m-1,n-1]

    result = 0
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            if node == destination:
                return result + 1
            for I,J in [[0,1],[-1,0],[-1,1],[-1,-1],[1,1],[1,0],[0,-1],[1,-1]]:
                X, Y = node[0]+I, node[1]+J
                if is_valid(X,Y):
                    queue.append([X,Y])
                    visited[X][Y] = True
        result += 1
    return result if result > 0  else  -1


TEST_CASES = [
                       ([[0,1],[1,0]]            , 2),
                       ([[0,0,0],[1,1,0],[1,1,0]], 4),
                       ([[1,0,0],[1,1,0],[1,1,0]], -1)
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
