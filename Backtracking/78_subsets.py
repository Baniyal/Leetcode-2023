"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
the subsets of {1,2,3} are ;, {1}, {2}, {3}, {1,2}, {1,3}, {2,3} and {1,2,3}.
"""

def function(arr: list,debug) -> int:
    result = []
    def recursive_function(array, index, path):
        if index == len(array):
            result.append(path)
        if index < len(array):
            recursive_function(array, index+1, path)
            recursive_function(array, index+1, path + [array[index]])

    recursive_function(arr,0,[])
    return sorted(result)


TEST_CASES = [
                ([1,2,3] ,[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
                ([0], [[],[0]])
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




