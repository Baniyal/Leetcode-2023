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
def main():
    uf = UnionFind(10)
    uf.union(1, 2)
    uf.union(2, 5)
    uf.union(5, 6)
    uf.union(6, 7)
    uf.union(3, 8)
    uf.union(8, 9)
    print(uf.connected(1, 5))  # true
    print(uf.connected(5, 7))  # true
    print(uf.connected(4, 9))  # false
    # 1-2-5-6-7 3-8-9-4
    uf.union(9, 4)
    print(uf.connected(4, 9))  # true
    print(uf)
    print(uf.get_components())

if __name__ == "__main__":
    main()