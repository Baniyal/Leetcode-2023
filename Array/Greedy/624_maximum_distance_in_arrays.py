"""
You are given m arrays, where each array is sorted in ascending order.
You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the
distance between two integers a and b to be their absolute difference |a - b|.
Return the maximum distance.
________________________________________________________________________________________________________________________
Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
________________________________________________________________________________________________________________________
Input: arrays = [[1],[1]]
Output: 0
"""

ARRAYS = [[-8, -7, -7, -5, 1, 1, 3, 4], [-2], [-10, -10, -7, 0, 1, 3], [2]]


def maxDistance(arrays):
    result = 0
    min_so_far, max_so_far = [arrays[0][0], arrays[0][-1]]
    print(arrays)
    for i in range(1, len(arrays)):
        curr_min, curr_max = [arrays[i][0], arrays[i][-1]]
        result = max(result, abs(curr_max - min_so_far), abs(max_so_far - curr_min))
        min_so_far, max_so_far = min(min_so_far, curr_min), max(max_so_far, curr_max)
    return result


print(maxDistance(ARRAYS))
