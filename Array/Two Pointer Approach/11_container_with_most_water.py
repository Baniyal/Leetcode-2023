"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the
ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water
the container can contain is 49.
================================================INTUITION===============================================================
Consider we start with i = 0 and j = height.size() - 1.
                                                        i points to the first column and j points to the last column.
Now suppose that h(i)>h(j) (we are not loosing generality by this assumption)
We calculate the water capacity for the i, j. It will be h(j)*(j-i).
Now see that if we fix j at height.size() - 1 and vary i, we cannot get a greater water capacity. Why?
capacity = min of both heights * width between them. Since capacity is the product of these two terms,
we will look at each term individually.First about the width. It is easy to see that for all other i's
(i = 1, 2,... ,height.size()-2) we will have a lesser width.
Second, the height will be the minimum of the column at i and at j, i.e. min(h(i),h(j)).
But this value will be always less than h(j), So both factors in the calculation of the capacity will be smaller and
hence we can skip considering all the cases where i = 1, 2, 3, ..., height.size()-2 and j = height.size()-1
Which basically means that we can simply move j to j-1.
"""
def function(height: list,debug) -> int:
    length_of_array = len(height)
    left, right = 0, length_of_array - 1
    result = 0
    while left < right:
        left_height, right_height = height[left], height[right]
        curr_capacity = min(left_height, right_height) * (right - left)
        result = max(result, curr_capacity)
        if debug:
            print("left------------>", left)
            print("right----------->", right)
            print("left height----->", left_height)
            print("right height---->", right_height)
            print("curr_capacity--->", curr_capacity)
            print("result---------->", result)
            print("-----------------\n")
        if left_height >= right_height:
            right -= 1
        elif left_height < right_height:
            left += 1
    return result


TEST_CASES = [
                ["tmmzuxt", 5],
                ["abcabcbb"         ,       3],
                ["bbbbb"            ,       1],
                ["pwwkew"           ,       3],
                [""                 ,       0],
                ["d"                ,       1],

             ]

DEBUG = False

for test_case, expected_result in TEST_CASES:
    actual_result = function(test_case,debug=DEBUG)
    if actual_result == expected_result:
        print(f"PASSED")
    else:
        print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
    print("--------------------------------")
    if DEBUG:
        break
