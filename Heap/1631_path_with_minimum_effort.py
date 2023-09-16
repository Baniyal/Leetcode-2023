"""
You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns,
where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0),
and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left,
or right, and you wish to find a route that requires the minimum effort.
A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.
Return the minimum effort required to travel from the top-left cell to the bottom-right cell.
________________________________________________________________________________________________________________________
Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
==============================================LEARNINGS=================================================================
"""
from collections import deque

HEIGHTS = [[1,2,2],[3,8,2],[5,3,5]]



def is_reachable(matrix,val):
    row, col = len(matrix), len(matrix[0])
    visited = [[False]*col for _ in range(row)]
    queue = deque([(0,0)])

    while queue:
        x,y = queue.popleft()

        if x== row - 1 and y == col - 1:
            return True
        visited[x][y] = True
        for X, Y in [[0,1],[1,0],[0,-1],[-1,0]]:
            adjacent_x = x + X
            adjacent_y = y +Y
            if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[adjacent_x][adjacent_y]:
                current_difference = abs(matrix[adjacent_x][adjacent_y]- matrix[x][y])
                if current_difference <= val:
                    visited[adjacent_x][adjacent_y] = True
                    queue.append([adjacent_x, adjacent_y])



def minimumEffortPath(heights):
    left, right = 0, 10**6
    while left < right:
        result = (left + right) // 2
        if is_reachable(heights,result):
            right = result
        else:
            left = result+1

    return left

print(minimumEffortPath(HEIGHTS))

# print(is_reachable(HEIGHTS,4))








