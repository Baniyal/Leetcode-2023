"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].
The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|,
where |val| denotes the absolute value of val.
Return the minimum cost to make all points connected.
"""
import copy

# UnionFind class
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
            root = self.find(i)  # Find the root of each element
            components[root].append(i)  # Group by root

        return list(components.values())

    def connected(self,x,y):
        return self.find(x) == self.find(y)
def function(input_arr):
    points = copy.deepcopy(input_arr)
    n = len(points)
    all_edges = []

    for curr_node in range(n):
        for next_node in range(curr_node + 1, n):
            weight = abs(points[curr_node][0] - points[next_node][0]) + \
                     abs(points[curr_node][1] - points[next_node][1])
            all_edges.append((weight, curr_node, next_node))

    all_edges.sort()

    resultant_cost = 0
    uf = UnionFind(n)
    for weight, start, end in all_edges:
        print(f"Weight {weight},Start={start},End={end}")

        if uf.union(start, end):
            resultant_cost += weight
        if uf.get_number_of_components() == 1:
            return resultant_cost


TEST_CASES = [
                ([[-1000000,-1000000],[1000000,1000000]], 0),
                (   [[0,0],[2,2],[3,10],[5,2],[7,0]], 20),
                (   [[3,12],[-2,5],[-4,1]], 18 ),

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



#================================================================HEAP SOLUTION==========================================

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) == 0:
            return 0
        size = len(points)
        pq = []
        uf = UnionFind(size)

        for i in range(size):
            x1, y1 = points[i]
            for j in range(i + 1, size):
                x2, y2 = points[j]
                # Calculate the distance between two coordinates.
                cost = abs(x1 - x2) + abs(y1 - y2)
                edge = Edge(i, j, cost)
                pq.append(edge)

        # Convert pq into a heap.
        heapq.heapify(pq)

        result = 0
        count = size - 1
        while pq and count > 0:
            edge = heapq.heappop(pq)
            if not uf.connected(edge.point1, edge.point2):
                uf.union(edge.point1, edge.point2)
                result += edge.cost
                count -= 1
        return result


class Edge:
    def __init__(self, point1, point2, cost):
        self.point1 = point1
        self.point2 = point2
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

