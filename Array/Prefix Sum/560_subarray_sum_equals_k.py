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