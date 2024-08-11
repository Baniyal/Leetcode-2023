"""
You are given a network of n nodes, labeled from 1 to n.
You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi),where ui is the source node,
vi is the target node, and wi is the time it takes for a signal to travel from source to target.

If it is impossible for all the n nodes to receive the signal, return -1. k is the source node
"""
from heapq import heappop, heappush
from collections import defaultdict
def function(input_arr):
    times, n, k = input_arr
    graph = defaultdict(list)
    for edge_1, edge_2, weight in times:
        graph[edge_1].append((weight, edge_2))


    heap = []
    heap.append((0,k))
    visited = set()
    while heap:
        time, node = heappop(heap)
        visited.add(node)

        if len(visited) == n:
            return time

        for neighbor in graph[node]:
            n_time , neighbor_node = neighbor
            if neighbor_node not in visited:
                heappush(heap, (time + n_time , neighbor_node) )

    return -1

TEST_CASES = [
                (  ([[2,1,1],[2,3,1],[3,4,1]], 4, 2), 2 ),
                (  ([[1,2,1]], 2,2),                   -1),
                (  ( [[1,2,1]], 2, 1),                   1),

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

