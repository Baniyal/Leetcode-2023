"""
Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.
Can you solve it without sorting?
------------------------------------------------------------------------------------------------------------------------
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
------------------------------------------------------------------------------------------------------------------------
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""


from collections import defaultdict
def function(input_arr: list,debug) -> bool:
    return result

TEST_CASES = [
                (([3,2,1,5,6,4], 2), 5),
                (([3,2,3,1,2,4,5,5,6], 4) , 4),
             ]

DEBUG =  False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break