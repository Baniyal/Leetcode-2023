"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.
------------------------------------------------------------------------------------------------------------------------
Input: s = "3[a]2[bc]"
Output: "aaabcbc"
------------------------------------------------------------------------------------------------------------------------
Input: s = "3[a2[c]]"
Output: "accaccacc"
------------------------------------------------------------------------------------------------------------------------
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
"""


def function(input_string:list)-> int:
    return



TEST_CASES = [
                (   "3[a]2[bc]", "aaabcbc"),
                (   "3[a2[c]]" ,  "accaccacc"   ),
                (   "2[abc]3[cd]ef", "abcabccdcdcdef"),
             ]

DEBUG = True

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break