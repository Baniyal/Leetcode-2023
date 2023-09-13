"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
========================================================================================================================
=============================================== LEARNINGS ==============================================================
where ever  there is k and talk of minimum or maximum think of using heaps
for max heap multiply all the values by -1
don;t be stupid and save information about the number rather than that, save information about the index of the number
instead
========================================================================================================================
37/51 test cases passed
"""

from heapq import heappush, heappop, heappushpop, heapify, nlargest

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3


def maxSlidingWindow(nums, k):
    start = 0
    heap = []
    result = []
    for end in range(len(nums)):
        heappush(heap, -1 * nums[end])
        if end - start + 1 == k:
            curr_max = -1 * heap[0]
            index = heap.index(-1 * nums[start])
            result.append(curr_max)
            print("current_max-------------->", curr_max)
            print("heap--------------------->", heap)
            print("curr_index--------------->", end)
            print("sliding window----------->", nums[start: end + 1])
            print("the start element in heap>", index)
            print("\n")

            heap[index] = heap[-1]
            heap.pop()
            heapify(heap)
            start += 1
    return result


# =======================================================================================================================
# =======================================================================================================================
# +++++++++++++++++++++++++++++++++++++++QUEUE APPROACH++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# =======================================================================================================================
"""
A sliding window is a constant-size subarray that moves through the array. At
each position of the window, we want to calculate some information about the
elements inside the window. An interesting problem is to maintain the sliding
window minimum, which means that at each position of the window, we should
report the smallest element inside the window.
The sliding window minimum can be calculated using the same idea that we
used for calculating the nearest smaller elements. We maintain a chain whose
first element is always the last element in the window, and each element in the
chain is smaller than the previous element. The last element in the chain is
always the smallest element inside the window. When the sliding window moves
forward and a new element appears, we remove from the chain all elements that
are larger than the new element. After this, we add the new element to the chain.
Finally, if the last element in the chain does not belong to the window anymore,
it is removed from the chain.


also use a deque to hold the indices of the elements in the sliding window
    
"""

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

from collections import deque

from collections import deque


def maxSlidingWindow(nums, k):
    window = deque()
    result = []

    for i in range(len(nums)):
        while window and window[0] <= i - k:
            window.popleft()

        while window and nums[window[-1]] < nums[i]:
            window.pop()
        window.append(i)
        if i >= k - 1:
            result.append(nums[window[0]])

    return result
