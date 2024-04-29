"""
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
------------------------------------------------------------------------------------------------------------------------
Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
"""

from collections import defaultdict
def function(matrix,debug):
    result = 0
    m, n = len(matrix), len(matrix[0])
    row_dict, col_dict = defaultdict(str) , defaultdict(str)
    for j in range(n):
        col_num = 0
        for i in range(m):
            col_num += matrix[i][j]*(10**(m-i-1))
        col_dict[col_num] = col_dict.get(col_num,0) + 1

    for i in range(m):
        row_num = 0
        for j in range(n):

            row_num += matrix[i][j]*(10**(n-j-1))
            print(matrix[i][j]*(10**(n-j-1)))
        print("========================================")
        row_dict[row_num] = row_dict.get(row_num,0) + 1



    print("Row Dict---------->",row_dict)
    print("Col Dict---------->",col_dict)

    for col_key in col_dict.keys():
        if row_dict.get(col_key,False) != False:
            result += row_dict[col_key]*col_dict[col_key]

    return result

TEST_CASES = [
                ( [[2,30,400],[40,7,6],[300,7,7]] , 0),
                ( [[3,2,1],[1,7,6],[2,7,7]]                , 1),
                ( [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]], 3)
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

