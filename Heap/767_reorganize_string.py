"""
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
Return any possible rearrangement of s or return "" if not possible.
------------------------------------------------------------------------------------------------------------------------
Input: s = "aab"
Output: "aba"
------------------------------------------------------------------------------------------------------------------------
Input: s = "aaab"
Output: ""
"""
from heapq import heappop, heappush, heapify
from collections import Counter, deque
def function(s:str)-> str:
    count_dict = Counter(s)
    count_set = [(-1*val, key) for key, val in count_dict.items()]
    busy = deque()
    heapify(count_set)
    res = ""
    while count_set and len(res) < len(s):
        print("Heap--------->",count_set)
        count, char = heappop(count_set)
        count += 1
        if busy:
            popped_count, popped_char = busy.popleft()
            print("Popped out of the busy queue",popped_count, popped_char)
            heappush(count_set, (popped_count, popped_char))
        if count != 0:
            busy.append((count,char))
        res += char
        print("Result---------->",res)
        print("Queue-------->",busy)
        print("\n")
    if len(res) != len(s):
        return ""
    return res




TEST_CASES = [
                (    "aaab", ""     ),
                (    "aab", "aba"   )

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