"""
You are given a list of airline tickets where tickets[i] = [fromi, toi] represent
the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.

All of the tickets belong to a man who departs from "JFK", thus,
the itinerary must begin with "JFK". If there are multiple valid itineraries,
you should return the itinerary that has the smallest lexical order when read as a single string.

For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
Output: ["JFK","MUC","LHR","SFO","SJC"]

Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"] but it is larger in lexical order.
"""
from collections import defaultdict

def function(input_arr:list, debug:bool) -> bool:
    edges = input_arr
    graph = defaultdict(list)
    for edge_1,edge_2 in edges:
        graph[edge_1].append(edge_2)

    for origin, iterianry in graph.items():
        iterianry.sort()


    def dfs(origin):
        print(f"Current Node is  {origin}")
        print(f"Current Path is  {result}")
        if len(result) == len(edges) + 1:
            return True
        if origin not in graph:
            return False
        neighbors = list(graph[origin])
        for index,neighbor in enumerate(neighbors):
            graph[origin].pop(index)
            result.append(neighbor)
            if dfs(neighbor): return True
            graph[origin].insert(index,neighbor)
            result.pop()
            return False

        result.append(origin)


    result = ["JFK"]
    dfs("JFK")
    return result

TEST_CASES = [
                (([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]] ),  ["JFK","ATL","JFK","SFO","ATL","SFO"]),
                (([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]),
                 ["JFK", "MUC", "LHR", "SFO", "SJC"]),

]

DEBUG = False


if __name__ == "__main__":

    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case,debug=DEBUG)
        if actual_result == expected_result:
            print(f"PASSED")
        else:
            print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break