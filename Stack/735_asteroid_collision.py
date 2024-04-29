"""
We are given an array asteroids of integers representing asteroids in a row.
For each asteroid, the absolute value represents its size, and the sign represents its direction
(positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode. If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.
------------------------------------------------------------------------------------------------------------------------
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
------------------------------------------------------------------------------------------------------------------------
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
------------------------------------------------------------------------------------------------------------------------
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
"""

from collections import deque
def function(arr:list)-> int:
    stack = []
    for curr_element in arr:
        while stack  and  stack[-1] > 0 and curr_element < 0 :
            if stack[-1] + curr_element < 0:
                stack.pop()
            elif stack[-1] + curr_element > 0:
                break
            else:
                stack.pop()
                break
        else:
            stack.append(curr_element)
    return stack

TEST_CASES = [
(   [5,10,-5], [5,10]),
                (  [8,-8],[]                        ),
                (  [10,2,-5], [10]                                    ),

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