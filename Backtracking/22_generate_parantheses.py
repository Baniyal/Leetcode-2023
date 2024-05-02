"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
------------------------------------------------------------------------------------------------------------------------
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
------------------------------------------------------------------------------------------------------------------------
Input: n = 1
Output: ["()"]
"""
def function(n:list)-> int:
    resultant = []
    def recursive(s, opened, closed):
        print(f"current string is  {s}")
        if 2 * n == opened + closed:
            resultant.append(s)

        if opened < n:
            recursive(s + '(', opened + 1, closed)
        if closed < opened:
            recursive(s + ')', opened, closed + 1)

    recursive("", 0,0)

    return resultant[::-1]



TEST_CASES = [
                (   3,   ["((()))","(()())","(())()","()(())","()()()"]  ),
                (  1,  ["()"]  ),
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