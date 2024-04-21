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


"""
=======================================================523==============================================================
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
 

Example 1:

Input: nums = [23,2,4,6,7], k = 6
Output: true
Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
Example 2:

Input: nums = [23,2,6,4,7], k = 6
Output: true
Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
Example 3:

Input: nums = [23,2,6,4,7], k = 13
Output: false
"""


def checkSubarraySum(nums, k: int) -> bool:
    if len(nums) < 2: return False
    hash_map, prefix_sum = {0: -1}, 0
    for index, num in enumerate(nums):
        prefix_sum += num
        if k != 0: prefix_sum = prefix_sum % k
        if prefix_sum in hash_map:
            if index - hash_map[prefix_sum] > 1:
                return True
        else:
            hash_map[prefix_sum] = index

    return False