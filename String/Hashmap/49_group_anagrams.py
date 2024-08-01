"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

from collections import defaultdict
def function(input_arr: list,debug) -> bool:
    hash_map = defaultdict(list)
    for each in input_arr:
        each_sorted = sorted(each)
        each_sorted = "".join(each_sorted)
        print("current string ---->", each)
        print("sorted string ---->", each_sorted)
        if each_sorted not in hash_map.keys():
            hash_map[each_sorted] = [each]
        else:
            hash_map[each_sorted].append(each)
        print("Current Hash,",hash_map)
    result = []
    for value in hash_map.values():
        result.append(value)

    return result

TEST_CASES = [
                (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
                ([""] , [[""]]),
                ( [ "a"] ,[["a"]])
             ]

DEBUG =  False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break