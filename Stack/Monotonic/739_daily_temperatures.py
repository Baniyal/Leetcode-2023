"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
------------------------------------------------------------------------------------------------------------------------
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
------------------------------------------------------------------------------------------------------------------------
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
------------------------------------------------------------------------------------------------------------------------
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""
def function(arr:list)-> int:
    monotonic_stack = []
    resultant = []
    for i in range(len(arr)-1,-1,-1):
        while monotonic_stack:
            print("Last element in the stack", monotonic_stack[-1][0])
            print("Current Element", arr[i])
            print("-----------------------------------")
            if monotonic_stack[-1][0] <= arr[i]:
                monotonic_stack.pop()
            else:
                break
        if monotonic_stack:
            resultant.append(monotonic_stack[-1][1] - i)
        else:
            resultant.append(0)
        print("resulstant----->", resultant[::-1])
        monotonic_stack.append([arr[i],i])
    return resultant[::-1]

TEST_CASES = [
                ([73,74,75,71,69,72,76,73],  [1,1,4,2,1,1,0,0]            ),
                (   [30,40,50,60],           [1,1,1,0]                    ),
                (   [30,60,90],              [1,1,0]                      ),

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