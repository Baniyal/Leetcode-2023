"""
Given an integer array nums, reorder it such that nums[0] <= nums[1] >= nums[2] <= nums[3]....
You may assume the input array always has a valid answer.
________________________________________________________________________________________________________________________
Input: nums = [3,5,2,1,6,4]
Output: [3,5,1,6,2,4]
Explanation: [1,6,2,5,3,4] is also accepted.
============================================INTUITION===================================================================
The question can be reworded as Reorder given array in such a manner that
          -  "every element at an odd index is greater than or equal to its adjoining elements at even indices"
"""
NUMS = [3,5,2,1,6,4]


def wiggleSort(nums):
    length_of_array: int = len(nums)
    nums.sort()
    for i in range(1,length_of_array-1,2):
        nums[i] , nums[i+1] = nums[i+1] , nums[i]
    return nums




print(wiggleSort(NUMS))
