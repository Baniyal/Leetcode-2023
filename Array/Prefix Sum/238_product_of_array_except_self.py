"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of
nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
________________________________________________________________________________________________________________________
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
________________________________________________________________________________________________________________________
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
==============================================LEARNINGS=================================================================

"""

nums = [-1, 1, 0, -3, 3]

#TODO: THIS AGAIN

















def productExceptSelf(nums):
    n = len(nums)
    prefix_product, suffix_product, resultant_array = [1] * n, [1] * n, [1] * n
    for i in range(n):
        if i != 0:
            prefix_product[i] = prefix_product[i - 1] * nums[i]
        else:
            prefix_product[i] = nums[i]
    for i in reversed(range(n)):
        if i != n - 1:
            suffix_product[i] = suffix_product[i + 1] * nums[i]
        else:
            suffix_product[i] = nums[i]

    for i in range(n):
        if i != 0 and i != n - 1:
            resultant_array[i] = prefix_product[i - 1] * suffix_product[i + 1]
        elif i == 0:
            resultant_array[i] = suffix_product[i + 1]
        elif i == n - 1:
            resultant_array[i] = prefix_product[i - 1]

    return resultant_array


print(productExceptSelf(nums))
