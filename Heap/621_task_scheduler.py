"""
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n.
Each cycle or interval allows the completion of one task. Tasks can be completed in any order,
but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.
Return the minimum number of intervals required to complete all tasks.
------------------------------------------------------------------------------------------------------------------------
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.
After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval,
neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.
------------------------------------------------------------------------------------------------------------------------
Input: tasks = ["A","C","A","B","D","B"], n = 1
Output: 6
Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
With a cooling interval of 1, you can repeat a task after just one other task.
------------------------------------------------------------------------------------------------------------------------
Input: tasks = ["A","A","A", "B","B","B"], n = 3
Output: 10
Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.
There are only two types of tasks, A and B, which need to be separated by 3 intervals.
This leads to idling twice between repetitions of these tasks.
"""
from collections import Counter, defaultdict
def function(input_arr, debug:bool) -> list:
    arr, n = input_arr
    count = Counter(arr)
    max_count = count.most_common()[0][1]
    reverse_count =  defaultdict(list)
    for key, value in count.most_common():
        reverse_count[value].append(key)
    maximum_count_tasks = len(reverse_count[max_count])
    return max(len(arr), (n+1)*(max_count - 1) + maximum_count_tasks )

TEST_CASES = [
                ((["A","A","A","B","B","B","C"],  2),        8),
                ((["A","C","A","B","D","B"],  1),         6),
                ((["A","A","A", "B","B","B"], 3),        10),
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