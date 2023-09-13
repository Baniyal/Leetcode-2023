"""
You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
Return the length longest chain which can be formed.
You do not need to use up all the given intervals. You can select pairs in any order.
________________________________________________________________________________________________________________________
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].
________________________________________________________________________________________________________________________
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
========================================================================================================================
===========================================LEARNINGS====================================================================
if you want to sort a list of lists by the first element of each list and if that element is similar then by the second
element
                sorted(list_of_lists, key=lambda x: (x[0], x[1]))
"""
pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]



def findLongestChain(pairs):
    sorted_pairs = sorted(pairs, key=lambda x: (x[1], x[0]))
    result = 1
    if len(pairs) == 1:
        return result
    previous_pair = sorted_pairs[0]
    for i in range(1,len(sorted_pairs)):
        print("Previous pair------------",previous_pair)
        print("Current pair-------------",sorted_pairs[i])

        if sorted_pairs[i][0] > previous_pair[1]:
            previous_pair = sorted_pairs[i]
            result += 1
        print("Current Longest Chain----", result)
        print("\n")

    return result

print(findLongestChain(pairs))
