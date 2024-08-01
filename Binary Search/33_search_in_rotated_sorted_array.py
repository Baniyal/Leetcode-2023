"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
                                                return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
------------------------------------------------------------------------------------------------------------------------
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
def function(input_arr:list)-> int:


    def rec_function():
        return
    return None



TEST_CASES = [
                (    ([4,5,6,7,0,1,2],   0),4   ),
                (  ([4,5,6,7,0,1,2],  3), -1 ),
                (   ([1] , 0),   -1   )
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