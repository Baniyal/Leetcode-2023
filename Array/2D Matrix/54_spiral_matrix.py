"""
Given an m x n matrix, return all elements of the matrix in spiral order.
------------------------------------------------------------------------------------------------------------------------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
------------------------------------------------------------------------------------------------------------------------
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

def function(matrix,debug):
    resultant = []
    row_begin, row_end = 0, len(matrix) - 1
    col_begin, col_end = 0, len(matrix[0]) - 1
    while row_begin <= row_end and col_begin <= col_end:
        for i in range(col_begin,col_end + 1):
            resultant.append(matrix[row_begin][i])
        row_begin += 1
        for i in range(row_begin,row_end+ 1):
            resultant.append(matrix[i][col_end])
        col_end -= 1
        if row_begin <= row_end:
            for i in range(col_end, col_begin - 1, -1):
                resultant.append(matrix[row_end][i])
            row_end -= 1
        if col_begin <= col_end:
            for i in range(row_end, row_begin - 1, -1):
                resultant.append(matrix[i][col_begin])
            col_begin += 1
    print(resultant)
    return resultant


TEST_CASES = [
                ([[1,2,3],[4,5,6],[7,8,9]] ,[1,2,3,6,9,8,7,4,5]),
                ( [[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])
             ]

DEBUG = True

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break

