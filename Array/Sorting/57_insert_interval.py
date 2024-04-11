"""
You are given an array of non-overlapping intervals  where intervals[i] = [starti, endi] represent the start
and the end of the ith interval and intervals is sorted in ascending order by starti.
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
Note that you don't need to modify intervals in-place. You can make a new array and return it.
------------------------------------------------------------------------------------------------------------------------
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
------------------------------------------------------------------------------------------------------------------------
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""
from typing import List

class Interval:
    def __init__(self,start,end):
        self.start = start
        self.end = end


def abandoned_function(input_arr:list)-> int:
    """
    abandoned this function due to all test cases not passing and added complexity of maintaining variables and flags
    """
    intervals, newInterval = input_arr[0], Interval(*input_arr[1])
    if len(intervals) == 0: return [input_arr[1]]
    resultant_intervals : List[int] = list()
    add_interval = True
    for curr_start, curr_end in intervals:
        if add_interval:
            if curr_end >= newInterval.start:
                curr_start = min(curr_start, newInterval.start)
                curr_end = max( curr_end ,newInterval.end)
                add_interval = False

        if len(resultant_intervals) > 0:
            last_interval = Interval(*resultant_intervals[-1])
            if curr_start <= last_interval.end:
                curr_start = min(last_interval.start, curr_start)
                curr_end = max(last_interval.end,curr_end)
                resultant_intervals.pop()

        print(f"curr_start {curr_start}, curr_end {curr_end}")
        resultant_intervals.append([curr_start, curr_end])
    if add_interval:
        resultant_intervals.append(input_arr[1])

    return resultant_intervals



import bisect

def function(input_arr: list) -> int:
    intervals, newInterval = input_arr[0], input_arr[1]
    intervals.append(newInterval)
    intervals.sort()
    resultant_intervals : List[int] = list()

    for curr_start, curr_end in intervals:
        if resultant_intervals:
            last_interval = Interval(*resultant_intervals[-1])
            if curr_start <= last_interval.end:
                curr_start = min(last_interval.start, curr_start)
                curr_end = max(last_interval.end,curr_end)
                resultant_intervals.pop()

        resultant_intervals.append([curr_start, curr_end])
    return resultant_intervals

TEST_CASES = [
                (   ([[1,3],[6,9]],                             [2,5])      , [[1,5],[6,9]]          ),
                (   ([[1,2],[3,5],[6,7],[8,10],[12,16]],        [4,8])     , [[1,2],[3,10],[12,16]] ),
                (   ([], [5,7]) , [[5,7]]),
                (   ([[1,5]], [2,3]), [[1,5]] ),
                (   ([[1,5]], [6,8]), [[1,5],[6,8]] ),
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break