"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
rob tonight without alerting the police.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
------------------------------------------------------------------------------------------------------------------------
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
"""

# Test Case 67/70
def slow_function(arr: list,debug) -> bool:
    def recursive_function(arr,index,mem,curr_loot):
        if mem.get((index,curr_loot),False):
            return mem[(index,curr_loot)]
        if index > len(arr) - 1:
            print("REACHED END OF ONE PATH, with current loot as",curr_loot)
            return curr_loot

        take_current =  recursive_function(arr,index + 2,mem,curr_loot + arr[index])
        dont_take_current = recursive_function(arr,index+ 1, mem, curr_loot )
        print(f"Robbing house at index {index} has loot {take_current}, current loot is {curr_loot + arr[index]}")
        print(f"Ignoring house at index {index} has loot {dont_take_current} curr_loot is {curr_loot}")
        print("-------------------------------------------------------------------------------------")
        mem[(index,curr_loot)] = max(take_current,dont_take_current)
        return max(take_current,dont_take_current)
    memoization = {}
    return    recursive_function(arr=arr,index=0,mem=memoization,curr_loot=0)

def function( nums: List[int]) -> int:
    if len(nums) == 0: return 0
    if len(nums) == 1: return nums[0]
    if len(nums) == 2: return max(nums)

    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

    return dp[-1]


TEST_CASES = [
([1,2,1,1], 3),
                (   [1,2,3,1]  ,               4),
                (   [2,7,9,3,1]  ,             12),
                (    [5],                       5),
                ([1,2,1,1], 3)
            ]

DEBUG = True

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break