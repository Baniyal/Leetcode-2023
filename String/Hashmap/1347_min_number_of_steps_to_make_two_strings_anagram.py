"""
You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with
another character.                                         Return the minimum number of steps to make t an anagram of s.
------------------------------------------------------------------------------------------------------------------------
Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
------------------------------------------------------------------------------------------------------------------------
Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.
------------------------------------------------------------------------------------------------------------------------
Input: s = "anagram", t = "mangaar"
Output: 0
Explanation: "anagram" and "mangaar" are anagrams.
"""

from collections import Counter
def function(input_arr: list,debug) -> bool:
    s, t = input_arr
    count = Counter(s)
    result = 0
    for char in t:
        if char not in count:
            result += 1
        elif char in count and count.get(char) > 1:
            count[char] -= 1
        else:
            del count[char]
    return result
TEST_CASES = [
    (["gctcxyuluxjuxnsvmomavutrrfb","qijrjrhqqjxjtprybrzpyfyqtzf"],18),
                (["leetcode", "practice"], 5),
                ( [ "bab","aba" ] ,                         1),

                ( [ "anagram",   "mangaar"] ,               0)
            ]

DEBUG =  False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break