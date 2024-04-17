"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
                             and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
------------------------------------------------------------------------------------------------------------------------
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
========================================================================================================================
3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""


# test cases passed 308/313
def slow_function(arr:list, debug:bool) -> list[list[int]]:
    resultant_array : list[int] = []
    for target_index in range(len(arr)):
        target = arr[target_index]
        seen = set()
        for index in range(len(arr)):
            if index == target_index:
                continue
            if -target - arr[index] in seen:
                temp_arr = [target, arr[index], -target - arr[index]]
                temp_arr.sort()
                if temp_arr not in resultant_array:
                    resultant_array.append(temp_arr)
            seen.add(arr[index])
            if debug:
                print(f"Current Target is {target} at the index {target_index}")
                print(f"Resultant Array so far is {resultant_array}")
                print(f"for index {index} the seen set is {seen}")
                print("=============================================")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    return resultant_array



from typing import List
def threeSum( nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = set()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            target = 0 - nums[i]
            while l < r:
                if nums[l] + nums[r] == target:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return list(result)



TEST_CASES = [
                ([-1,0,1,2,-1,-4] ,[[-1,-1,2],[-1,0,1]]),
                ( [0,1,1], []),
                ([0,0,0], [[0,0,0]])

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