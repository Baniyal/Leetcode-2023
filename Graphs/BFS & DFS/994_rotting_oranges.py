"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
"""
import collections
import copy


def function(input_arr):
    matrix = input_arr
    m,n = len(matrix), len(matrix[0])
    visited = copy.deepcopy(matrix)

    def is_valid(x,y):
        if (0 <= x < m) and (0 <= y < n) and visited[x][y] == False and matrix[x][y] == 1:
            return True
        return False
    rotten = collections.deque([])
    fresh = 0
    for i in range(m):
        for j in range(n):
            visited[i][j] = False
            if matrix[i][j] == 2:
                rotten.append([i,j])
            if matrix[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    time = 0
    while rotten:
        size = len(rotten)
        print(f"Rotten is  {rotten} of size {size}")
        for i in range(size):
            node = rotten.popleft()
            visited[node[0]][node[1]] = True
            for I,J in [[0,1],[-1,0],[1,0],[0,-1]]:
                X, Y = node[0]+I, node[1]+J
                if is_valid(X,Y):
                    print(f"Adding the element {[X,Y]} into queue ")
                    fresh -= 1
                    matrix[X][Y] = 2
                    print(f"Number of fresh elements left {fresh}")
                    rotten.append([X,Y])
                    if fresh == 0:return time + 1
        print("\n")
        time += 1
    print(f"Time taken is {time}")
    return time if fresh == 0 else -1


TEST_CASES = [
                       ([[2,1,1],[1,1,0],[0,1,1]]           , 4),
                       ([[2,1,1],[0,1,1],[1,0,1]], -1),
                       ([[0,2]], 0)
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


