"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array
relations where relations[i] = [prevCoursei, nextCoursei], representing a prerequisite relationship between
course prevCoursei and course nextCoursei: course prevCoursei has to be taken before course nextCoursei.
In one semester, you can take any number of courses as long as you have taken all the prerequisites in the previous
semester for the courses you are taking.
Return the minimum number of semesters needed to take all courses. If there is no way to take all the courses, return -1
________________________________________________________________________________________________________________________
Input: n = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: The figure above represents the given graph.
In the first semester, you can take courses 1 and 2.
In the second semester, you can take course 3.
________________________________________________________________________________________________________________________
Input: n = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: No course can be studied because they are prerequisites of each other.
+++++++++++++++++++++++++++++++++++++++++++++++THEORY+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed
edge u v, vertex u comes before v in the ordering.
* Note: Topological Sorting for a graph is not possible if the graph is not a DAG i.e. a cycle exists in the graph
Topological Sorting vs Depth First Traversal (DFS):
---------------In DFS, we print a vertex and then recursively call DFS for its adjacent vertices.
               In topological sorting, we need to print a vertex before its adjacent vertices.
Algorithm for Topological Sorting
---------------Prerequisite: DFS
---------------We can modify DFS to find the Topological Sorting of a graph. In DFS, We start from a vertex, we first
               print it, and then Recursively call DFS for its adjacent vertices.
---------------In topological sorting,
               We use a temporary stack.
               We don’t print the vertex immediately,
               we first recursively call topological sorting for all its adjacent vertices, then push it to a stack.
               Finally, print the contents of the stack.
               Note: A vertex is pushed to stack only when all of its adjacent vertices
               (and their adjacent vertices and so on) are already in the stack

Create a stack to store the nodes.
Initialize visited array of size N to keep the record of visited nodes.
Run a loop from 0 till N
    if the node is not marked True in visited array
        Call the recursive function for topological sort and perform the following steps.
            Mark the current node as True in the visited array.
            Run a loop on all the nodes which has a directed edge to the current node
                if the node is not marked True in the visited array:
                    Recursively call the topological sort function on the node
            Push the current node in the stack.
Print all the elements in the stack.
++++++++++++++++++++++++++++++++++++++++++++++++APPLICATION+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Applications of Topological Sorting:

Topological Sorting is mainly used for scheduling jobs from the given dependencies among jobs.

In computer science, applications of this type arise in:
        Instruction scheduling
        Ordering of formula cell evaluation when recomputing formula values in spreadsheets
        Logic synthesis
        Determining the order of compilation tasks to perform in make files
        Data serialization
        Resolving symbol dependencies in linkers
=========================================================================================================

def generate_topological_sort(n,edges):
    graph = defaultdict(list)


    for u, v in edges:
        graph[u].append(v)


    def recursive_func(curr_node, visited, stack):
        visited.add(curr_node)
        for neighbour in graph[curr_node]:
            if neighbour not in visited:
                recursive_func(neighbour, visited, stack)
        stack.append(curr_node)

    stack = list()
    visited = set()
    for node in range(1,n):
        if node not in visited:
            recursive_func(node, visited, stack)

    return stack[::-1]



===============================================LEARNINGS================================================================
always think if you need to track the nodes you have already been to or not

"""
from collections import defaultdict, deque
N = 3
RELATIONS = [[1,3],[2,3],[3,1]]

def is_dag_cyclic(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    def is_dag_cyclic_utility(curr_node,path):
        if curr_node in path:
            return True
        path.add(curr_node)
        for neigh_node in graph[curr_node]:
            if is_dag_cyclic_utility(neigh_node, path): return True
        path.remove(curr_node)
        return False

    for node in range(1, n+1):
        if is_dag_cyclic_utility(node, set()): return True
    return False


def minimumSemesters(n, edges):
    graph = defaultdict(list)
    queue = deque()
    visited = set()
    for u, v in edges:
        graph[u].append(v)
        if u not in queue: queue.append(u)

    if is_dag_cyclic(n,edges):
        return -1
    def recursive_func(curr_node, visited):
        visited.add(curr_node)
        print("Current Node--------->", curr_node)
        if len(visited) == n:
            return True
        for neigh_node in graph[curr_node]:
            if neigh_node not in visited:
                print("entering recursive function")
                recursive_func(neigh_node, visited)
                print("EXITING RECURSIVE FUNCTION")

    for node in range(1,n + 1):
        if recursive_func(node, visited): return True

    return -1


print(minimumSemesters(N, RELATIONS))



