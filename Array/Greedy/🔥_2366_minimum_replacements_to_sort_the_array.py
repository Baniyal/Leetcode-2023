"""
You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two
elements that sum to it.
For example, consider nums = [5,6,7].
In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
Return the minimum number of operations to make an array that is sorted in non-decreasing order.
________________________________________________________________________________________________________________________
Input: nums = [3,9,3]
Output: 2
Explanation: Here are the steps to sort the array in non-decreasing order:
- From [3,9,3], replace the 9 with 3 and 6 so the array becomes [3,3,6,3]
- From [3,3,6,3], replace the 6 with 3 and 3 so the array becomes [3,3,3,3,3]
There are 2 steps to sort the array in non-decreasing order. Therefore, we return 2.
________________________________________________________________________________________________________________________
Input: nums = [1,2,3,4,5]
Output: 0
Explanation: The array is already in non-decreasing order. Therefore, we return 0.
++++++++++++++++++++++++++++++++++++++++++++++HINTS+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
It is optimal to never make an operation to the last element of the array.
We don't want to make operation to the last element because we want it to remain the largest value, and it is untouched.
You can iterate from the second last element to the first. If the current value is greater than the previous bound,we
want to break it into pieces so that the smaller one is as large as possible but not larger than the previous one.
=============================================LEARNINGS==================================================================

"""


"""
+++++++++++++++++++++++++++++++++++++++++++++++++STRATEGY+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
We can only make numbers smaller, not larger. So we should iterate from right to left;
this way, we know exactly how small we have to make the current number, because we already know what the number to the
right is, and we know the current number has to be smaller than that.

Suppose we're iterating from right to left. The current number is n, and the right number is prev. 
We have to consider how to split n into some m numbers (m can be 1), such that...
a. The largest (and rightmost) of those m numbers must be less than or equal to prev.
b. The smallest (and leftmost) of these m numbers should probably be as large as possible. Why? 
Because this will become our next prev, so if it's higher, it will probably be easier to split numbers to the left.
c. We should probably split as little as we possibly can, since this is an optimization problem on the number of splits.
This fact is important to us when splitting:
for any positive integer n and all 1 <= k <= n, it's possible to represent n as the sum of k numbers,
such that all numbers differ by no more than 1.
Why is this relevant? Because as we iterate from right to left, we're going to try to split n into k integers
such that the largest is less than or equal to prev, the difference between all numbers is no more than 1,
the numbers are as large as possible, and there are as few numbers as possible.
Note that the last three conditions go hand-in-hand!
If the numbers are as large as they possibly can be such that they're all less than or equal to prev,
then there will definitely be as few as possible.

The largest k that we can split into will be ceil(n / prev)

to understand why, let's break it into two cases:
n % prev == 0 - in other words, prev divides n.
            In this case, we should break n into as many copies of prev as we can.
            This will prevent us from lowering prev in our next iteration, and since prev is the highest we can make our
            new elements without breaking the sorted condition, it also means we're splitting into as few elements as possible.
n % prev > 0 - in other words, prev does not divide n. In this case, we can't have all elements equal to prev,
            but we can do the next best thing. We can use one extra element ((n // prev) + 1) than we would in the 
            first case to make the lowest element (n // prev) instead. Because of the property about k that I stated above,
            this is always doable.
Time complexity is O(N), space complexity is O(1). Solution below.
"""
import math

input_array = [2, 10, 20, 19, 1]


def minimumReplacement(nums):
    counter = 0
    last_processed = nums[-1]
    n = len(nums)
    for i in range(n - 2, -1, -1):
        k = math.ceil(nums[i]/last_processed)
        counter += k - 1
        last_processed = nums[i]//k

    return counter


print(minimumReplacement(input_array))
