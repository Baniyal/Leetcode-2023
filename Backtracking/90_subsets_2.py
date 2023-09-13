"""
Given an integer array nums that may contain duplicates, return all possible
subsets(the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""
nums = [1,2,2]


def subsetsWithDup(nums):
    result = []
    nums.sort()
    n = len(nums)

    def rec_func(nums, index, path):
        print("current index------------->", index)
        print("array left---------------->", nums[index:])
        print("subsets created----------->", result)
        print("curr path------------------<", path)
        print("\n")

        if index == len(nums):
            if path not in result:
                result.append(path)

        if index < n:
            rec_func(nums, index + 1, path)
            rec_func(nums, index + 1, path + [nums[index]])

    rec_func(nums, 0, [])
    return result

print(subsetsWithDup(nums))