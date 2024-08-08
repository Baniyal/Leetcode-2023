"""
Given a reference of a node in a connected undirected graph.
                                                                Return a deep copy (clone) of the graph.
Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed).
For example, the first node with val == 1, the second node with val == 2, and so on.
The graph is represented in the test case using an adjacency list.
------------------------------------------------------------------------------------------------------------------------
"""
import copy
from collections import defaultdict

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def function(input_arr:list, debug:bool) -> bool:
    return copy.deepcopy(input_arr)

TEST_CASES = [
                ([[2,4],[1,3],[2,4],[1,3]], [[2,4],[1,3],[2,4],[1,3]]),
             ]

DEBUG = True


if __name__ == "__main__":

    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case,debug=DEBUG)
        if actual_result == expected_result:
            print(f"PASSED")
        else:
            print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break