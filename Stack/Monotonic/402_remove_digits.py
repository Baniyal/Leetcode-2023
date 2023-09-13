"""
Given string num representing a non-negative integer num, and an integer k,
return the smallest possible integer after removing k digits from num.
_________________________________________________________________________________________
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is
the smallest.
_________________________________________________________________________________________
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not
contain leading zeroes.
__________________________________________________________________________________________
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

============================================================================================
====================================LEARNINGS===============================================
given two sequences of digit of the same length, it is the leftmost distinct digits that
determine the superior of the two numbers, e.g.
                                for A = 1axxx, B = 1bxxx, if the digits a > b, then A > B.

iterate from the left to right, when removing the digits.
The more a digit to the left-hand side, the more weight it carries.
CRITERIA FOR POPPING
when curr element is less than elements in the left of it, pop the elements on the left.
Try to think of native functions, like <<<<<<<< lstrip >>>>>>>>> function could've been used
for getting the proper number.
"""


def removeKdigits(nums, k):
    stack = []
    for num in nums:
        while stack and stack[-1] > num and k:
            stack.pop()
            k -= 1
        stack.append(num)
    stack = stack[:-k] if k else stack
    return "".join(stack).lstrip('0') or "0"