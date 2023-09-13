"""
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other.
If it is not possible to rearrange the string, return an empty string "".
________________________________________________________________________________________________________________________
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
________________________________________________________________________________________________________________________
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
________________________________________________________________________________________________________________________
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
=============================================LEARNINGS=========================================================
Solution-1 below takes into account for the distance between strings to be exactly k no tatleast k
this is causing for 54 / 64 testcases passed
"""
from collections import Counter

STRING = "aabbcc"
K = 2


def rearrangeString(s, k):
    if k == 0 :
        return s
    number_of_characters = Counter(s)
    number_of_characters = dict(sorted(number_of_characters.items(), reverse=True, key=lambda x: x[1]))
    length_of_string = len(s)
    resultant_array = [None] * length_of_string

    ITERATOR = 0
    try:
        for char in number_of_characters.keys():
            print("-----------ITERATOR-----------")
            print(ITERATOR)
            while resultant_array[ITERATOR] is not None:
                ITERATOR += 1
            curr_index = ITERATOR
            resultant_array[curr_index] = char
            number_of_characters[char] -= 1
            while number_of_characters[char] > 0:
                curr_index = curr_index + k
                if resultant_array[curr_index] is None:
                    resultant_array[curr_index] = char
                    print("Current Index------------->", curr_index)
                    resultant_array[curr_index] = char
                    number_of_characters[char] -= 1
                    print("Number of characters------------->", number_of_characters[char])
                elif resultant_array[curr_index] is not None:
                    curr_index = curr_index + k
                    if curr_index > length_of_string - 1:
                        return "Not Possible"
            ITERATOR += 1
            print(resultant_array)
            print("---------------------------------------------------------------")
        print("========================================================================")
        print(number_of_characters)
    except BaseException as error:
        print(f"Error occured as {error}")
        return False
    return "".join(resultant_array)


# print(rearrangeString(STRING, K))



