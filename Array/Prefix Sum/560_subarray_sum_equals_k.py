"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,1,1], k = 2
Output: 2
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,2,3], k = 3
Output: 2
"""
from collections import defaultdict


def function(input_set,debug) -> bool:
    arr, k = input_set
    hash_map, prefix_sum = defaultdict(), 0
    result = 0
    for element in arr:
        prefix_sum += element
        if prefix_sum == k:
            result += 1
        if prefix_sum - k in hash_map:
            result += hash_map[prefix_sum - k]
        hash_map[prefix_sum] = hash_map.get(prefix_sum,0) + 1
        if debug:
            print("Currently at element ", element)
            print("Current prefix sum: ", prefix_sum)
            print("Hashmap",hash_map)
            print("Number of valid subarrays so far", result)
            print("----------------------------")
    print("=================================")
    return result

TEST_CASES = [
                (   ([1,1,1],2)  ,               2),
                (   ([1,2,3],3)  ,              2)
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
"""
================================================974=====================================================================
Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
------------------------------------------------------------------------------------------------------------------------
Input: nums = [5], k = 9
Output: 0
"""



def function_2(input_set,debug) -> bool:
    arr, k = input_set
    hash_map, prefix_sum = defaultdict(), 0
    result = 0
    for num in arr:
        prefix_sum += num
        if prefix_sum % k == 0:
            result += 1
        result += hash_map.get(prefix_sum % k, 0)
        hash_map[prefix_sum % k] = hash_map.get(prefix_sum % k, 0) + 1
    return result
