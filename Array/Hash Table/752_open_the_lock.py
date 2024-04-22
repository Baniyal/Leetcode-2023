"""
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots:
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock,
return the minimum total number of turns required to open the lock, or -1 if it is impossible.
------------------------------------------------------------------------------------------------------------------------
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
------------------------------------------------------------------------------------------------------------------------
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".
------------------------------------------------------------------------------------------------------------------------
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.
"""

from collections import deque
def function(input_arr, debug:bool) -> list:
    next_slot = {
        "0": "1",
        "1": "2",
        "2": "3",
        "3": "4",
        "4": "5",
        "5": "6",
        "6": "7",
        "7": "8",
        "8": "9",
        "9": "0",
    }

    prev_slot = {
        "0": "9",
        "1": "0",
        "2": "1",
        "3": "2",
        "4": "3",
        "5": "4",
        "6": "5",
        "7": "6",
        "8": "7",
        "9": "8",
    }

    deadend, target = input_arr
    visited = set(deadend)
    visited.add("0000")
    possible = deque(["0000"])
    if "0000" in deadend:
        return -1
    turns = 0
    while possible:
        temp_possible_length = len(possible)
        for _ in range(temp_possible_length):
            current_combination = possible.popleft()
            if current_combination == target:
                return turns
            for wheel in range(4):
                new_combination = list(current_combination)
                new_combination[wheel] = next_slot[new_combination[wheel]]
                new_combination_str = "".join(new_combination)

                if new_combination_str not in visited:
                    possible.append(new_combination_str)
                    visited.add(new_combination_str)

                new_combination = list(current_combination)
                new_combination[wheel] = prev_slot[new_combination[wheel]]
                new_combination_str = "".join(new_combination)

                if new_combination_str not in visited:
                    possible.append(new_combination_str)
                    visited.add(new_combination_str)

        turns += 1

    return -1

TEST_CASES = [
                ((["0201","0101","0102","1212","2002"],"0202")                       ,        6),
                ((["8888"], "0009")                                                 ,         1),
                ((["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"),        -1),
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