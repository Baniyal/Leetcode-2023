"""
Given an integer array nums of unique elements, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

the subsets of {1,2,3} are ;, {1}, {2}, {3}, {1,2}, {1,3}, {2,3} and {1,2,3}
subsets = [1,2,3]
"""
nums = [0]


def subsets(nums):
    result = []
    n = len(nums)

    def rec_func(nums, index, path):
        print("current index------------->", index)
        print("array left---------------->", nums[index:])
        print("subsets created----------->", result)
        print("curr path------------------<", path)
        print("\n")

        if index == len(nums):
            result.append(path)

        if index < n:
            rec_func(nums, index + 1, path)
            rec_func(nums, index + 1, path + [nums[index]])

    rec_func(nums, 0, [])
    return result

print(subsets(nums))
