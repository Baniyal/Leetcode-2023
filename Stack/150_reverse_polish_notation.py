"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.
------------------------------------------------------------------------------------------------------------------------
Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
------------------------------------------------------------------------------------------------------------------------
Input: tokens = ["4","13","5","/","+"]
Output: 6
------------------------------------------------------------------------------------------------------------------------
Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
"""
import math


def function(arr:list)-> int:
    operators = ['+', '-', '*','/']
    stack = []
    def operation(operator,num1,num2):
        print(f"Operation being performed is {operator} on {num1} and {num2}")
        print("================================")
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num2 - num1
        if operator == '*':
            return num1 * num2
        if operator == '/':
            return math.trunc(num2 / num1)

    while arr:
        element = arr.pop(0)
        print(f"Current element is {element}")
        if element not in operators:
            stack.append(int(element))
        else:
            stack.append(operation(element, stack.pop(),stack.pop()))
            print(f"Element added to the stack is {stack[-1]}")
        print(f"Ongoing stack {stack}")
    return stack[0]



TEST_CASES = [
(   ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
                (   ["2","1","+","3","*"], 9                                     ),
                (   ["4","13","5","/","+"], 6                                    ),

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