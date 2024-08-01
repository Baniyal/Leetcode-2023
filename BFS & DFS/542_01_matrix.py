"""
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.
------------------------------------------------------------------------------------------------------------------------
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]
------------------------------------------------------------------------------------------------------------------------
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
"""

def function(input_arr: list) -> int:
    return  None

TEST_CASES = [
                       ([[0,0,0],[0,1,0],[0,0,0]] ,                    [[0,0,0],[0,1,0],[0,0,0]] ),
                       ([[0,0,0],[0,1,0],[1,1,1]] ,                    [[0,0,0],[0,1,0],[1,2,1]] )
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break