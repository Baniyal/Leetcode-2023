"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an
 array of the non-overlapping intervals that cover all the intervals in the input.
------------------------------------------------------------------------------------------------------------------------
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
------------------------------------------------------------------------------------------------------------------------
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""
def function(arr:list)-> int:
    arr.sort(key= lambda x: x[0])
    resultant_array = [arr.pop(0)]
    while arr:
        curr_start, curr_end = arr.pop(0)
        print([curr_start, curr_end])
        if resultant_array[-1][0] <= curr_start <= resultant_array[-1][1] :
            print(f"Merging between {resultant_array[-1]} and {[curr_start, curr_end]}  ")
            resultant_array[-1][0] = min(resultant_array[-1][0],curr_start)
            resultant_array[-1][1] = max(resultant_array[-1][1],curr_end)
        else:
            resultant_array.append([curr_start,curr_end])
        print("Resultant Array so far---------->",resultant_array)
    print("================================")
    return resultant_array





TEST_CASES = [
                (    [[1,3],[2,6],[8,10],[15,18]],  [[1,6],[8,10],[15,18]]   ),
                (   [[1,4],[4,5]]                ,           [[1,5]]         )
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