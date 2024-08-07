"""
You are given a string s,
an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.
------------------------------------------------------------------------------------------------------------------------
Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
------------------------------------------------------------------------------------------------------------------------
Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
------------------------------------------------------------------------------------------------------------------------
Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""
import collections
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.count = size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y):
        root_X = self.find(x)
        root_Y = self.find(y)

        if root_X == root_Y:
            return False

        self.root[root_Y] = root_X
        self.count -= 1
        return True
    def get_number_of_components(self):
        return self.count

    def get_components(self):
        components = collections.defaultdict(list)
        for i in range(len(self.root)):
            root = self.find(i)
            components[root].append(i)

        return list(components.values())

    def connected(self,x,y):
        return self.find(x) == self.find(y)

from collections import OrderedDict
def function(input_arr):
    string, edges = input_arr
    string_mapping = OrderedDict()
    for i in range(len(string)):
        string_mapping[i] = string[i]

    uf = UnionFind(len(string))
    for edge_1, edge_2 in edges:
        uf.union(edge_1, edge_2)
    print(uf.get_components())
    print(uf.get_number_of_components())
    for component in uf.get_components():
        arr = [string_mapping[index] for index in component]
        arr.sort()
        temp_string = "".join(arr)
        index = 0
        for i in component:
            string_mapping[i] = temp_string[index]
            index += 1
    return "".join(string_mapping.values())



TEST_CASES = [
                (   ("dcab",[[0,3],[1,2]]), "bacd"),
                (   ("dcab", [[0,3],[1,2],[0,2]]), "abcd" ),
                (   ("cba",  [[0,1],[1,2]]),   "abc" ),

             ]

DEBUG = False


if __name__ == '__main__':
    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"Test Case {test_case} passed")
        else:
            print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break
