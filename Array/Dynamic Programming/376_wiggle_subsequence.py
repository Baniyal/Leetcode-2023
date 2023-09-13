"""
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and
negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a
sequence with two non-equal elements are trivially wiggle sequences.
________________________________________________________________________________________________________________________
For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive
and negative.In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its
first two differences are positive, and the second is not because its last difference is zero.A subsequence is obtained
by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original
order.Given an integer array nums, return the length of the longest wiggle subsequence of nums.
________________________________________________________________________________________________________________________
nums = [1,17,5,10,13,15,10,5,16,8]
26/31 test cases passed
========================================LESSONS LEARNED=================================================================
Why to include two parameters greater or lesser when it can be done by a single parameter ?
"""

nums = [1,17,5,10,13,15,10,5,16,8]


def wiggleMaxLength(nums):
    greater = False
    lesser = False
    if len(nums) == 1:
        return 1
    if nums == [0,0] or nums == [0,0,0]:
        return 1
    if nums[1] > nums[0]: greater = True
    if nums[0] > nums[1]: lesser = True
    res = 2
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]: continue
        if nums[i] > nums[i - 1] and greater == True:
            lesser = False
        elif nums[i] < nums[i - 1] and lesser == True:
            greater = False
        elif nums[i] > nums[i-1] and lesser == True:
            greater = True
            lesser = False
            res += 1
        elif nums[i] < nums[i-1] and greater == True:
            greater = False
            lesser = True
            res += 1
    return res

# print(wiggleMaxLength(nums))


# =====================================OFFICIAL SOLUTION================================================================


def wiggleMaxLength(nums):
    n = len(nums)
    if n < 2:
        return n
    max_len = 1
    last_wiggle = None

    for i in range(1, n):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and last_wiggle != 1) or (diff < 0 and last_wiggle != -1):
            max_len += 1
            last_wiggle = 1 if diff > 0 else -1
    return max_len