"""
There are n people in a social group labeled from 0 to n - 1.
You are given an array logs where logs[i] = [timestampi, xi, yi]
                                                        indicates that xi and yi will be friends at the time timestampi.

Friendship is symmetric. That means if a is friends with b, then b is friends with a.
Also, person a is acquainted with a person b if a is friends with b, or a is a friend of someone acquainted with b.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return -1.
------------------------------------------------------------------------------------------------------------------------
Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], n = 6
Output: 20190301
Explanation:
The first event occurs at timestamp = 20190101, and after 0 and 1 become friends, we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104, and after 3 and 4 become friends, we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107, and after 2 and 3 become friends, we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211, and after 1 and 5 become friends, we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224, and as 2 and 4 are already friends, nothing happens.
The sixth event occurs at timestamp = 20190301, and after 0 and 3 become friends, we all become friends.
Example 2:

Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
Explanation: At timestamp = 3, all the persons (i.e., 0, 1, 2, and 3) become friends.
"""
class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.latest = -1
        self.count = size
    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self, x, y,timestamp):
        root_X = self.find(x)
        root_Y = self.find(y)

        if root_X == root_Y:
            # print(f"For Friends {x} and {y}, they already belong to same set of friends")
            # print(f"The latest time stamp for them doesn't change {self.latest}")
            return False
        if root_X != root_Y:
            self.root[root_Y] = root_X
        self.latest = max(self.latest, timestamp)
        self.count -= 1
        return True
    def get_number_of_components(self):
        return self.count

def function(input_arr):
    graph_data, friends = input_arr
    friends_data = sorted(graph_data, key=lambda x: x[0])
    uf = UnionFind(friends)
    for time, friend_a, friend_b in friends_data:
        uf.union(friend_a, friend_b, time)
    if uf.count != 1:
        return -1
    return uf.latest



TEST_CASES = [
                (   ([[9,0,3],[0,2,7],[12,3,1],[5,5,2],[3,4,5],[1,5,0],[6,2,4],[2,5,3],[7,7,3]], 8), -1),
                (   ([[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], 6),   20190301 ),
                (   ([[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], 4),   3   ),

             ]

DEBUG = True


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
