"""
You are given an integer array coins representing coins of different denominations and an integer amount representing a
total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
------------------------------------------------------------------------------------------------------------------------
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
------------------------------------------------------------------------------------------------------------------------
Input: coins = [2], amount = 3
Output: -1
------------------------------------------------------------------------------------------------------------------------
Input: coins = [1], amount = 0
Output: 0
"""

def function(input_arr:list)-> int:
    coins, amount = input_arr
    dp = [float("inf")]*(amount+1)
    dp[0] = 0

    for i in range(1,amount+1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i-coin] + 1)
                print(f"Current coin {coin}")
                print(f"Current amount is {i}")
                print(f"The DP array so far is {dp}")
        print("-------------------------------------------")

    return dp[-1] if dp[-1] != float('inf') else -1




TEST_CASES = [
                (    ([1,2,5],11), 3 ),
                (    ([2],3), -1     ),
                (    ([1],0), 0      )
             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case)
    if actual_result == expected_result:
        print(f"Test Case {test_case} passed")
    else:
        print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break