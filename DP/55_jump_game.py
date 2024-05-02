"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the
array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible
to reach the last index.
"""

def function( nums,debug) -> int:
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False
    curr_max = nums[0]
    for i in range(1, len(nums)):
        curr_max = max(curr_max, i + nums[i])
        if curr_max >= len(nums) - 1:
            return True
        if i >= curr_max:
            return False

TEST_CASES = [ ([1,0,1,0] , False),
                (   [2,3,1,1,4] , True),
                (   [3,2,1,0,4] , False)
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