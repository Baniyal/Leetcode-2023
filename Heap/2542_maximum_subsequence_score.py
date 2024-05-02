"""
You are given two 0-indexed integer arrays nums1 and nums2 of equal length n and a positive integer k.
You must choose a subsequence of indices from nums1 of length k.
For chosen indices i0, i1, ..., ik - 1, your score is defined as:
The sum of the selected elements from nums1 multiplied with the minimum of the selected elements from nums2.
It can defined simply as: (nums1[i0] + nums1[i1] +...+ nums1[ik - 1]) * min(nums2[i0] , nums2[i1], ... ,nums2[ik - 1]).
Return the maximum possible score.
A subsequence of indices of an array is a set that can be derived from the set {0, 1, ..., n-1} by deleting some or no elements.
------------------------------------------------------------------------------------------------------------------------
Input: nums1 = [1,3,3,2], nums2 = [2,1,3,4], k = 3
Output: 12
Explanation:
The four possible subsequence scores are:
- We choose the indices 0, 1, and 2 with score = (1+3+3) * min(2,1,3) = 7.
- We choose the indices 0, 1, and 3 with score = (1+3+2) * min(2,1,4) = 6.
- We choose the indices 0, 2, and 3 with score = (1+3+2) * min(2,3,4) = 12.
- We choose the indices 1, 2, and 3 with score = (3+3+2) * min(1,3,4) = 8.
Therefore, we return the max score, which is 12.
------------------------------------------------------------------------------------------------------------------------
Input: nums1 = [4,2,3,1,1], nums2 = [7,5,10,9,6], k = 1
Output: 30
Explanation:
Choosing index 2 is optimal: nums1[2] * nums2[2] = 3 * 10 = 30 is the maximum possible score.
"""
from heapq import heappush, heappop
def function(input_arr)-> str:
    nums1, num2, k = input_arr
    pairs = [ (n1, n2) for n1, n2 in zip(nums1, num2)]
    pairs = sorted(pairs, key=lambda x: x[1], reverse=True)
    run_sum = 0
    min_heap = []
    result = 0
    for i in range(len(pairs)):
        num1, num2 = pairs[i]
        run_sum += num1
        heappush(min_heap, num1)
        if len(min_heap) > k:
            num1_pop = heappop(min_heap)
            run_sum -= num1_pop
        if len(min_heap) == k:
            result = max(result, run_sum*num2)
    return result


TEST_CASES = [
                (   ( [1,3,3,2]  , [2,1,3,4]   , 3), 12  ),
                (   ( [4,2,3,1,1], [7,5,10,9,6], 1), 30  )
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break