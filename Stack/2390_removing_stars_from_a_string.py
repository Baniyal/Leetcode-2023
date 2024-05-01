"""
You are given a string s, which contains stars *.
In one operation, you can:
    Choose a star in s.
    Remove the closest non-star character to its left, as well as remove the star itself.
    Return the string after all stars have been removed.
Note:
The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
------------------------------------------------------------------------------------------------------------------------
Input: s = "leet**cod*e"
Output: "lecoe"
Explanation: Performing the removals from left to right:
- The closest character to the 1st star is 't' in "leet**cod*e". s becomes "lee*cod*e".
- The closest character to the 2nd star is 'e' in "lee*cod*e". s becomes "lecod*e".
- The closest character to the 3rd star is 'd' in "lecod*e". s becomes "lecoe".
There are no more stars, so we return "lecoe".
------------------------------------------------------------------------------------------------------------------------
Input: s = "erase*****"
Output: ""
Explanation: The entire string is removed, so we return an empty string.
"""

def function(arr:list)-> int:
    stack = []
    stars = 0
    for char in arr:
        if char == "*":
            if stack:
                stack.pop()
            else:
                stars += 1
        else:
            if stars == 0:
                stack.append(char)
            else:
                stars -= 1
                stack.pop()
        print("Stars at current postion: ", stars)
        print("Stack at current postion: ", stack)
    return "".join(stack)

TEST_CASES = [
                (   "leet**cod*e", "lecoe"),
                (   "erase*****" ,   ""   ),
                ("ke*cod*", "kco"),
                ("", "")
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