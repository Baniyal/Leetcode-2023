"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the
elements in both subsets is equal or false otherwise.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

def function(arr: list,debug) -> bool:
    def sub_function(arr, index, target, mem):
        if (index, target) in mem:
            return mem[(index, target)]
        if target < 0:
            mem[(index, target)] = False
            return False

        if target == 0:
            mem[(index, target)] = True
            return True

        for i in range(index, len(arr)):
            result = sub_function(arr, i + 1, target - arr[index], mem)
            if result:
                mem[(i, target)] = True
                return True
        mem[(index, target)] = False
        return False

    if sum(arr) % 2 != 0: return False
    target = sum(arr) // 2
    memoization = {}

    return sub_function(arr, index=0, target=target, mem=memoization)
TEST_CASES = [
                (   [1,5,3,11,5,3]  ,               True),
                (   [1,2,3,5]   ,              False)
            ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break