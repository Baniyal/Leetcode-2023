"""
==========================PROBLEM STATEMENT===============================================================
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
An interleaving of two strings s and t is a configuration where s and t are divided into n and m substrings
respectively, such that:
                            s = s1 + s2 + ... + sn
                            t = t1 + t2 + ... + tm
                            |n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

==============================LESSONS=====================================================================
--Be very careful where to include and not to include if and elif----
---in case of recursion elif will make you miss out on all possible--
--outcomes.
_____________________________________________________________________
--The reason why memoization solution wasn't working in the starting because of how the dictionary was----
---setup, it should be -> the check  for if  items is present in the dictionary should be in the front----
---once function executes, put value of those identifiers(indexes), into the memoization container-------
==========================================================================================================
"""

s1, s2, s3 = 'aabcc', 'dbbca', "aadbbcbcac"
index_1, index_2, index_3 = 0, 0, 0


def isInterleaveRecursive(s1: str, s2: str, s3: str) -> bool:
    """
    Recursive solution
    99 / 106 testcases passed
    """
    if len(s1) == index_1 and len(s2) == index_2:
        return True
    if index_1 < len(s1) and s1[index_1] == s3[index_3]:
        subset_sol = isInterleaveRecursive(s1[index_1 + 1:], s2[index_2:], s3[index_3 + 1:])
        if subset_sol:
            return True
    if index_2 < len(s2) and s2[index_2] == s3[index_3]:
        subset_sol = isInterleaveRecursive(s1[index_1:], s2[index_2 + 1:], s3[index_3 + 1:])
        if subset_sol:
            return True
    return False


if len(s1) + len(s2) != len(s3):
    print("False")

# =======================================================================================================================
# =======================================================================================================================


MEMORY = dict()

s1, s2, s3 = "aabcc", "dbbca", "aadbbcbcac"


def isInterleaveMemoization(index_1, index_2) -> bool:
    """
    Memoization
    All testcases passed
    Beats 99.78% of users in terms of time complexity
    """
    if MEMORY.get((index_1, index_2), None) is not None:
        return MEMORY[(index_1, index_2)]

    if len(s1) == index_1 and len(s2) == index_2:
        return True
    if index_1 < len(s1) and s1[index_1] == s3[index_1 + index_2] and isInterleaveMemoization(index_1 + 1, index_2):
        return True
    if index_2 < len(s2) and s2[index_2] == s3[index_1 + index_2] and isInterleaveMemoization(index_1, index_2 + 1):
        return True

    MEMORY[(index_1, index_2)] = False
    return False


print(isInterleaveMemoization(0, 0))
