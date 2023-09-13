"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot
tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any
point in time.Given the two integers m and n, return the number of possible unique paths that the robot can take to
reach the bottom-right corner.
________________________________________________________________________________________________________________________
Input: m = 3, n = 7
Output: 28
________________________________________________________________________________________________________________________
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
"""
m, n = 3, 7


def uniquePaths(m, n):
    matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        matrix[i][0] = 1
    for j in range(n):
        matrix[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            print("row index----->", i)
            print("col index----->", j)
            print("\n")
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[-1][-1]


# print(uniquePaths(m, n))

"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square
that is an obstacle.Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
________________________________________________________________________________________________________________________
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
________________________________________________________________________________________________________________________
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
"""

obstacleGrid = [[0, 1], [0, 0]]


def uniquePathsWithObstacles(obstacleGrid):
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    matrix = [[0] * n for _ in range(m)]
    if obstacleGrid[0][0] == 1:
        return 0
    for i in range(m):
        if obstacleGrid[i][0] != 1 and matrix[i - 1][0] is not None:
            matrix[i][0] = 1
        elif obstacleGrid[i][0] != 1 and matrix[i - 1][0] is None:
            matrix[i][0] = None
        if obstacleGrid[i][0] == 1:
            matrix[i][0] = None

    for i in range(n):
        if obstacleGrid[0][i] != 1 and matrix[0][i - 1] is not None:
            matrix[0][i] = 1
        elif obstacleGrid[0][i] != 1 and matrix[0][i - 1] is None:
            matrix[0][i] = None
        if obstacleGrid[0][i] == 1:
            matrix[0][i] = None

    for i in range(1, m):
        for j in range(1, n):
            print("row index----->", i)
            print("col index----->", j)

            top = matrix[i - 1][j]
            top_val = 0 if top is None else top
            right = matrix[i][j - 1]
            right_val = 0 if right is None else right
            if obstacleGrid[i][j] == 1:
                matrix[i][j] = None
            else:
                matrix[i][j] = top_val + right_val
            print(matrix)
            print("\n")
    return matrix[-1][-1]


# print(uniquePathsWithObstacles(obstacleGrid))


"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum 
of all numbers along its path.
________________________________________________________________________________________________________________________
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
________________________________________________________________________________________________________________________
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
"""

grid = [[1,2,3],[4,5,6]]


def minPathSum(matrix):
    m, n = len(matrix), len(matrix[0])
    for i in range(1,m):
        matrix[i][0] += matrix[i-1][0]
    for j in range(1,n):
        matrix[0][j] += matrix[0][j-1]

    print(matrix)
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = min(matrix[i - 1][j] , matrix[i][j - 1]) + matrix[i][j]
    return matrix[-1][-1]


print(minPathSum(grid))
