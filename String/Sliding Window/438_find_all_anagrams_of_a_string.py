"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
You may return the answer in any order.
------------------------------------------------------------------------------------------------------------------------
Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
------------------------------------------------------------------------------------------------------------------------
Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""
from collections import Counter
def function(input_strings, debug:bool) -> list:
    s,p = input_strings
    p_count = Counter(p)
    sliding_window_size = len(p)
    sliding_window_dict = {}
    resultant_indexes = []
    for i in range(len(s)):
        sliding_window_dict[s[i]] = sliding_window_dict.get(s[i],0) + 1
        print("current index is",i)
        if i + 1 >= sliding_window_size :
            print("sliding_window_dict--->", sliding_window_dict)
            print("sliding_window_string->", s[i - sliding_window_size + 1 : i + 1 ])
            print(f"Remove character '{s[i-sliding_window_size + 1]}' from the sliding window  ")
            if sliding_window_dict == p_count:
                print(f"ANAGRAM FOUND, starting at {i-sliding_window_size + 1}")
                resultant_indexes.append(i-sliding_window_size + 1)
            sliding_window_dict[s[i-sliding_window_size+1]] = sliding_window_dict.get(s[i-sliding_window_size+1],0) - 1
            if sliding_window_dict[s[i-sliding_window_size+ 1]]  == 0:
                del sliding_window_dict[s[i-sliding_window_size + 1]]
        print("-------------------------------")
    # "cbaebabacd"
    return resultant_indexes

TEST_CASES = [
                (("cbaebabacd",  "abc"),        [0,6]),
                (("abab","ab"),               [0,1,2])
             ]

DEBUG = True

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break