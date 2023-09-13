"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and
nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
________________________________________________________________________________________________________________________
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
________________________________________________________________________________________________________________________
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
________________________________________________________________________________________________________________________
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
________________________________________________________________________________________________________________________
"""

nums = [5,4,3,2,1]


def increasingTriplet(nums):
    n = len(nums)
    smallest_l_to_r = [float("inf")] * n
    largest_r_to_l = [float("-inf")] * n
    smallest_l_to_r[0] = nums[0]
    min_so_far = smallest_l_to_r[0]
    largest_r_to_l[-1] = nums[-1]
    max_so_far = largest_r_to_l[-1]
    for i in range(1, n):
        if min_so_far > nums[i]:
            min_so_far = nums[i]
        smallest_l_to_r[i] = min_so_far

    for i in reversed(range(n - 1)):
        if max_so_far < nums[i]:
            max_so_far = nums[i]
        largest_r_to_l[i] = max_so_far

    for i in range(1,n-1):
        if smallest_l_to_r[i] < nums[i] < largest_r_to_l[i]:
            return True
    print(nums)
    print(smallest_l_to_r)
    print(largest_r_to_l)
    return False

print(increasingTriplet(nums))
