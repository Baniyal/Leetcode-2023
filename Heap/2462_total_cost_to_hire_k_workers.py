"""
You are given a 0-indexed integer array costs where costs[i] is the cost of hiring the ith worker.
You are also given two integers k and candidates. We want to hire exactly k workers according to the following rules:
You will run k sessions and hire exactly one worker in each session.
In each hiring session, choose the worker with the lowest cost from either the first candidates workers
or the last candidates workers. Break the tie by the smallest index.
For example, if costs = [3,2,7,7,1,2] and candidates = 2, then in the first hiring session,
we will choose the 4th worker because they have the lowest cost [3,2,7,7,1,2].
In the second hiring session, we will choose 1st worker because they have the same lowest cost as 4th worker
but they have the smallest index [3,2,7,7,2]. Please note that the indexing may be changed in the process.
------------------------------------------------------------------------------------------------------------------------
Input: costs = [17,12,10,2,7,2,11,20,8], k = 3, candidates = 4
Output: 11
------------------------------------------------------------------------------------------------------------------------
Input: costs = [1,2,4,1], k = 3, candidates = 3
Output: 4

"""
import heapq
def function(input_arr)-> str:
    costs,k,candidates = input_arr
    n = len(costs)
    cand_heap = []
    left_bound, right_bound = candidates, n - candidates - 1
    for i in range(candidates):
        heapq.heappush(cand_heap, (costs[i], i))
    for i in reversed(range(n - candidates, n)):
        if i < left_bound:
            break
        heapq.heappush(cand_heap, (costs[i], i))

    total_cost = 0
    for _ in range(k):
        cost, inx = heapq.heappop(cand_heap)
        total_cost += cost
        if left_bound <= right_bound:
            if inx < left_bound:
                heapq.heappush(cand_heap, (costs[left_bound], left_bound))
                left_bound += 1
            elif inx > right_bound:
                heapq.heappush(cand_heap, (costs[right_bound], right_bound))
                right_bound -= 1
    return total_cost

TEST_CASES = [
                (   ( [17,12,10,2,7,2,11,20,8],  3,  4), 11  ),
                (   ( [1,2,4,1]               ,  3,  3), 4  )
             ]

DEBUG = True

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break