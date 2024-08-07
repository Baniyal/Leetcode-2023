"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
                                                return the index of target if it is in nums, or -1 if it is not in nums.
"""
def function(testcase)-> int:
    nums, target = testcase
    n = len(nums)
    left, right = 0, n - 1


    # This helps find the pivot element, eventually it will be at the index -> left
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1

    def binarySearch(left_boundary, right_boundary, target):
        left, right = left_boundary, right_boundary
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    if (answer := binarySearch(0, left - 1, target)) != -1:
        return answer

    return binarySearch(left, n - 1, target)



TEST_CASES = [
                (    ([4,5,6,7,0,1,2],   0),4   ),
                (  ([4,5,6,7,0,1,2],  3), -1 ),
                (   ([1] , 0),   -1   )
             ]



DEBUG = False

if __name__ == '__main__':
    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"Test Case {test_case} passed")
        else:
            print(f"Test Case {test_case} failed. With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break