"""
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n.
(i.e The length of the garden is n).
There are n + 1 taps located at points [0, 1, ..., n] in the garden.
Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap can water
the area [i - ranges[i], i + ranges[i]] if it was open.
Return the minimum number of taps that should be open to water the whole garden, If the garden cannot be watered
return -1.
________________________________________________________________________________________________________________________
Input: n = 5, ranges = [3,4,1,1,0,0]
Output: 1
Explanation: The tap at point 0 can cover the interval [-3,3]
The tap at point 1 can cover the interval [-3,5]
The tap at point 2 can cover the interval [1,3]
The tap at point 3 can cover the interval [2,4]
The tap at point 4 can cover the interval [4,4]
The tap at point 5 can cover the interval [5,5]
Opening Only the second tap will water the whole garden [0,5]
___________________________________________________HINTS________________________________________________________________

The problem requires taps to cover a specific range, not just a single point. Since the taps' ranges are all zero, they
cannot water any interval other than a single point, which means they cannot cover the entire garden.


Create intervals of the area covered by each tap, sort intervals by the left end.
We need to cover the interval [0, n]. we can start with the first interval and out of all intervals that intersect with
it we choose the one that covers the farthest point to the right.What if there is a gap between intervals that is not
covered ? we should stop and return -1 as there is some interval that cannot be covered.
"""

length_of_garden, range_of_tap = 7, [1, 2, 1, 0, 2, 1, 0, 1]


# ================================================GREEDY================================================================


def minTaps(n, ranges):
    minimum_taps = 0
    max_reach = [0] * (n + 1)
    for i in range(len(ranges)):
        start = max(0, i - ranges[i])
        end = min(n, i + ranges[i])
        max_reach[start] = max(max_reach[start], end)

    curr_reach = 0
    next_reach = 0
    for i in range(n + 1):
        if i > next_reach:
            return -1
        if i > curr_reach:
            minimum_taps += 1
            curr_reach = next_reach
        next_reach = max(next_reach, max_reach[i])

    return minimum_taps


print(minTaps(length_of_garden, range_of_tap))
