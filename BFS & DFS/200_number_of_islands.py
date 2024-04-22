"""
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
------------------------------------------------------------------------------------------------------------------------
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
------------------------------------------------------------------------------------------------------------------------
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
------------------------------------------------------------------------------------------------------------------------
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""
from collections import deque
def function(matrix:list,debug)-> int:
    queue = deque()
    m,n = len(matrix) , len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                queue.append([i,j])

    visited = set()
    number_of_islands = 0
    def is_valid_point(x, y, visited):
        if 0 <= x < m and 0 <= y < n and (x, y) not in visited and matrix[x][y] != "0":
            return True
        return False

    while queue:
        curr_node = queue.popleft()
        if (curr_node[0],curr_node[1]) in visited:
            continue
        visited.add((curr_node[0],curr_node[1]))
        stack = [curr_node]
        while stack:
            x,y = stack.pop()
            for X,Y in [[0,1],[1,0],[0,-1],[-1,0]]:
                next_node_x, next_node_y = x+X ,y+Y
                if debug:
                    print("Current node is",[x,y])
                    print("Next node is",next_node_x,next_node_y)
                if is_valid_point(next_node_x, next_node_y,visited):
                    visited.add((next_node_x, next_node_y))
                    print("Node is valid")
                    print("Adding it to the stack")
                    stack.append([next_node_x, next_node_y])
                print("------------------------------")
            print("VISITED NODES",visited)
            print("======================================")
        number_of_islands += 1
        print("NUMBER OF ISLANDS",number_of_islands)
    return number_of_islands

TEST_CASES = [
                ([["1","1","1","1","0"],
                  ["1","1","0","1","0"],
                  ["1","1","0","0","0"],
                  ["0","0","0","0","0"]],   1   ),
                ([["1","1","0","0","0"],
                  ["1","1","0","0","0"],
                  ["0","0","1","0","0"],
                  ["0","0","0","1","1"]],  3   )
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break