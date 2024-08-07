"""
Given a string containing digits from 2-9 inclusive,
                                                return all possible letter combinations that the number could represent.
------------------------------------------------------------------------------------------------------------------------
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
------------------------------------------------------------------------------------------------------------------------
Input: digits = "2"
Output: ["a","b","c"]
"""
from typing import List
def function(n: int)-> List[str]:
    letters = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    digits = str(n)
    result = []

    def backtrack(index, path):
        if len(path) == len(digits):
            result.append("".join(path))
            return
        possible_letters = letters[digits[index]]
        for letter in possible_letters:
            backtrack(index + 1, path + letter)
    backtrack(0,"")

    return result


TEST_CASES = [
                (   23,  ["ad","ae","af","bd","be","bf","cd","ce","cf"]  ),
                (   2,   ["a","b","c"] ),
             ]

DEBUG = False

if __name__ == "__main__":

    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"Test Case {test_case} passed")
        else:
            print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break