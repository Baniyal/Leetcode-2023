"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations
of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than
150 combinations for the given input.
------------------------------------------------------------------------------------------------------------------------
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
------------------------------------------------------------------------------------------------------------------------
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
------------------------------------------------------------------------------------------------------------------------
Input: candidates = [2], target = 1
Output: []
------------------------------------------------------------------------------------------------------------------------
1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""

def function(input_arr:list)-> int:
    arr, target = input_arr[0], input_arr[1]
    arr.sort()
    result: list = []
    def rec_function(array,index,path,target):
        if DEBUG:
            print(f"Currently at index {index}")
            print(f"Path so far is {path}")
            print(f"Target at this point is {target}")
            print(f"Combination sum so far is {result}")
            print("----------------------------------------------------------------")
        if target == 0:
            result.append(path)
            return
        if target < array[index] :
            return
        for i in range(index, len(array)):
            rec_function(array,i,path + [array[i]],target - array[i])

    rec_function(arr,0,[],target)
    return result


TEST_CASES = [
                (   ([2,3,6,7], 7),   [[2,2,3],[7]]   ),
                (   ([2,3,5],   8),  [[2,2,2,2],[2,3,3],[3,5]]   ),
                (   ([2],       1),   []   )
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