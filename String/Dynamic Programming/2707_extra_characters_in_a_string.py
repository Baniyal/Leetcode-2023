"""
You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non
overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which
are not present in any of the substrings.
                                    Return the minimum number of extra characters left over if you break up s optimally.
________________________________________________________________________________________________________________________
Input: s = "leetscode", dictionary = ["leet","code","leetcode"]
Output: 1
Explanation: We can break s in two substrings: "leet" from index 0 to 3 and "code" from index 5 to 8. There is only 1
unused character (at index 4), so we return 1.
________________________________________________________________________________________________________________________
Input: s = "sayhelloworld", dictionary = ["hello","world"]
Output: 3
Explanation: We can break s in two substrings: "hello" from index 3 to 7 and "world" from index 8 to 12. The characters at indices 0, 1, 2 are not used in any substring and thus are considered as extra characters. Hence, we return 3.
"""
from functools import cache

# ==============================================Algorithm===============================================================
"""
To achieve O(1) lookups, convert the list of strings in the dictionary to a set.
Define a recursive function called dp that takes the starting index of the substring as a parameter.
At each recursive call of dp check if the starting index start has reached the end of the string s. If so, return 0.
Set ans, the answer for the current state, to dp(start + 1) + 1.
If the starting index is not at the end of the string, explore all possible substrings starting from the current index start.
For each possible substring, checks if it exists in the dictionary. If it does, recursively calculate the minimum number of extra characters starting from the next index dp(end + 1).
Keep track of the minimum number of extra characters encountered so far (ans) and update it whenever a lower value is found.
To optimize the solution and avoid redundant computations, utilize memoization. Store the results of previously computed subproblems in a separate data structure.
Finally, call the dp function with the starting index set to 0.
"""
parent_string = "leetscode"
dic = ["leet", "code", "leetcode"]


@cache
def minExtraChar(s, dictionary):
    set_of_subsets = set(dictionary)

    def rec_func(string, start):
        if start == len(string):
            return 0

    rec_func(s, 0)


print(minExtraChar(parent_string, dic))
