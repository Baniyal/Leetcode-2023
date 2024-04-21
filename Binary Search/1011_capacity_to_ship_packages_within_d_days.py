"""
A conveyor belt has packages that must be shipped from one port to another within days.
The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the
conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped
                                                                                     within predefined days .
------------------------------------------------------------------------------------------------------------------------
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10
Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into
parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
------------------------------------------------------------------------------------------------------------------------
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
------------------------------------------------------------------------------------------------------------------------
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
"""
def function(input_arr: list,debug) :
    weights, days = input_arr

    def validate(max_weight):
        need, cur =  1, 0
        for w in weights:
            if cur + w > max_weight:
                need += 1
                cur = 0
            cur += w
        print(f"Number of days needed for ship of weight capacity {cur} is {need} days \n")
        return True if need > days else False


    left , right = max(weights), sum(weights)
    while left < right:

        middle = (left + right)//2
        print("left values is",left)
        print("right values is",right)
        print("cur values is",middle)
        print("------------------")
        if validate(middle):
            left = middle + 1
        else:
            right = middle


    return left



TEST_CASES = [
               ( [[1,2,3,4,5,6,7,8,9,10], 5] , 15 ),
               ( [[3,2,2,4,1,4],          3] ,  6 ),
               ( [[1,2,3,1,1],            4],   3 )
            ]

DEBUG =  False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break