"""
You are given a string word containing lowercase English letters.
Telephone keypads have keys mapped with distinct collections of lowercase English letters.
It is allowed to remap the keys numbered 2 to 9 to distinct collections of letters.
The keys can be remapped to any amount of letters, but each letter must be mapped to exactly one key.
You need to find the minimum number of times the keys will be pushed to type the string word.

Return the minimum number of pushes needed to type word after remapping the keys.
------------------------------------------------------------------------------------------------------------------------
Input: word = "xyzxyzxyzxyz"
Output: 12
Explanation: The remapped keypad given in the image provides the minimum cost.
"x" -> one push on key 2
"y" -> one push on key 3
"z" -> one push on key 4
Total cost is 1 * 4 + 1 * 4 + 1 * 4 = 12
It can be shown that no other mapping can provide a lower cost.
Note that the key 9 is not mapped to any letter: it is not necessary to map letters to every key, but to map all the letters.
------------------------------------------------------------------------------------------------------------------------
Input: word = "aabbccddeeffgghhiiiiii"
Output: 24
Explanation: The remapped keypad given in the image provides the minimum cost.
"a" -> one push on key 2
"b" -> one push on key 3
"c" -> one push on key 4
"d" -> one push on key 5
"e" -> one push on key 6
"f" -> one push on key 7
"g" -> one push on key 8
"h" -> two pushes on key 9
"i" -> one push on key 9
Total cost is 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 1 * 2 + 2 * 2 + 6 * 1 = 24.
It can be shown that no other mapping can provide a lower cost.
"""

from collections import Counter

def function(input_str, debug: bool) -> bool:
    count = Counter(input_str)
    sorted_freq_count = sorted(list(count.values()), reverse=True)
    res = 0
    for i, frequency in enumerate(sorted_freq_count):
        res += frequency * (i // 8 + 1)
    return res


TEST_CASES = [
    ("aabbccddeeffgghhiiiiii", 24),
    ("abcde", 5),
    ("xyzxyzxyzxyz", 12)
]

DEBUG = False

if __name__ == "__main__":
    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case, debug=DEBUG)
        if actual_result == expected_result:
            print(f"PASSED")
        else:
            print(
                f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}"
            )
        print("--------------------------------")
        if DEBUG:
            break
