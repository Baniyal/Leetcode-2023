"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
________________________________________________________________________________________________________________________
                                                SOLUTION
========================================================================================================================
O(n) solution
Iterate over all the elements of the array until the running sum of the array is less than the current element, in that
case reset the running sum of the array.

Divide and conquer solution

"""
def function(arr:list)-> int:
    running_sum, maximum_subarray_sum = 0, float("-inf")
    for curr_element in arr:
        running_sum += curr_element
        if curr_element > running_sum :
            running_sum = curr_element
        maximum_subarray_sum = max(maximum_subarray_sum, running_sum)

    return maximum_subarray_sum

TEST_CASES = [
                (   [-2,1,-3,4,-1,2,1,-5,4],    6   ),
                (   [1]                    ,    1   ),
                (   [5,4,-1,7,8]           ,   23   )
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break