"""
Two strings are considered close if you can attain one from the other using the following operations:
ration 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.
Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.
------------------------------------------------------------------------------------------------------------------------
Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
------------------------------------------------------------------------------------------------------------------------
Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.
------------------------------------------------------------------------------------------------------------------------
Input: word1 = "cabbba", word2 = "abbccc"
Output: true
Explanation: You can attain word2 from word1 in 3 operations.
Apply Operation 1: "cabbba" -> "caabbb"
Apply Operation 2: "caabbb" -> "baaccc"
Apply Operation 2: "baaccc" -> "abbccc"
"""

from collections import Counter
def function(input_strings, debug:bool) -> list:
    string_1, string_2 = input_strings
    len_1, len_2 = len(string_1), len(string_2)
    if len_1 != len_2: return False
    count_string_1 , count_string_2 = Counter(string_1), Counter(string_2)
    if sorted(count_string_1.values()) != sorted(count_string_2.values()): return False
    return True

TEST_CASES = [
                (("cabbba","abbccc"), True),
                (("abc",  "bca"),     True),
                (("a","aa") ,        False)
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