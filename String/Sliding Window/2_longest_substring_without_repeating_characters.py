"""
Given a string s, find the length of the longest substring without repeating characters.
________________________________________________________________________________________________________________________
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
________________________________________________________________________________________________________________________
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
________________________________________________________________________________________________________________________
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
========================================================================================================================
                                                SOLUTION
Use two pointer approach to solve the problem,
right pointer moves with every iteration until we reach end of the string
Left pointer moves when the character is already present in the dictionary,
       LOOP left += 1 until string[left] is the char.
"""

def function(string: str,debug) -> int:
    left: int = 0
    char_set: set = set()
    result:int = 0
    for right in range(len(string)):
        if string[right] in char_set:
            while string[left] != string[right]:
                left = left + 1
            left += 1
            char_set.remove(string[right])


        char_set.add(string[right])
        result = max(result, right - left + 1)
        if debug:
            print(f"current character is {string[right]}")
            print(f"left index is at {left}")
            print(f"right index is at {right}")
            print("---------------------------")
    return result

TEST_CASES = [
                ["abcabcbb"         ,       3],
                ["bbbbb"            ,       1],
                ["pwwkew"           ,       3],
                [""                 ,       0],
                ["d"                ,       1],
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