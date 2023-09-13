"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
________________________________________________________________________________________________________________________
permutations for {1,2,3} are (1,2,3), (1,3,2), (2,1,3),(2,3,1), (3,1,2) and (3,2,1).
+++++++++++++++++++++++++++++++++++++++++++++LEARNINGS++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



=============================================ALGORITHM==========================================================
Initialize an answer array ans and an array curr to build permutations with.
Create a backtrack function that takes curr as an argument:
If curr.length == nums.length, add a copy of curr to ans and return.
Iterate over nums. For each num, if num is not in curr, do the following:
Add num to curr and call backtrack(curr), then remove num from curr.
Call backtrack with an initially empty curr.
Return ans.
"""

input_array = [1, 1, 2]


def permute(nums):
    result = []
    n = len(nums)

    def rec_func(nums, path):
        if len(path) == n and path not in result:
            result.append(path)
            return

        for i in range(n):
            if nums[i] not in path:
                rec_func(nums, path + [nums[i]])

    rec_func(nums,[])
    return result


# print(permute(input_array))

"""
Approach: Backtracking
Intuition

We are given that n <= 6. Typically, problems that ask you to find all of something with low bounds can be solved with
backtracking.In backtracking, we generate all solutions one element at a time. This problem is asking us to generate 
all possible permutations, so we will generate permutations one element at a time.

To generate a permutation one element at a time, we will use an array curr that represents the current permutation 
we are building. To start, we add the first element in nums.
We have curr = [nums[0]]. We are locking in this first value and we will now find all permutations that start with
nums[0].To find all permutations that start with nums[0], we start by adding the next element, which is nums[1]. We now
have curr = [nums[0], nums[1]]. We are locking in this second element and we will now find all permutations that start 
with nums[0], nums[1].This continues until we use all elements, i.e. curr.length == nums.length. Let's say that we have
finished finding all permutations that start with [nums[0], nums[1]]. Now what? We backtrack by removing the nums[1],
and we have curr = [nums[0]] again. Now, we add the second element that comes after nums[0], which is nums[2].
We have curr = [nums[0], nums[2]], and now we need to find all permutations that start with [nums[0], nums[2]].

Once we find all the permutations that start with [nums[0]], we backtrack by removing nums[0] from curr and adding the
next element. We have curr = [nums[1]], and now we need to find all permutations that start with nums[1].

This process is very recursive in nature. Each time we add an element, we solve a new version of the problem
(find all permutations that start with curr). The initial version of the problem is to find all permutations that start 
with [], which represents all possible permutations.
To summarize:
    try all numbers in the first position. 
    For each number in the first position, try all other numbers in the second position.
    For each pair of numbers in the first and second positions, try all other numbers in the third position, and so on.

The best way to think about the backtracking process is by modeling it as a tree.
You can imagine the solution space as a tree, with each node representing a version of curr.
Label each node with a number that represents the last number in curr.
Moving to a child is like adding the child's label to curr.

A permutation uses each element exactly once.
A node should only have children with labels representing elements that haven't been used yet in the current path.
"""

# =====================================================================================================================
#                                PERMUTATIONS WITH DUPLICATE

input_array = [1,1,2]


def permuteUnique(nums):
    def backtrack(remainder, path):
        remainder = remainder.copy()
        path = path.copy()
        if len(remainder) == 0:
            result.append(path)
        for i in range(len(remainder)):
            if i > 0 and remainder[i] == remainder[i - 1]:
                continue
            path.append(remainder[i])
            backtrack(remainder[0:i] + remainder[i + 1:], path)
            path.pop()
#           the above three lines are the same as the following
#           backtrack(remainder[0:i] + remainder[i + 1:], path + remainder[i])
#           it automatically appends the current element in th path and remove it

        return

    nums.sort()
    result = []
    backtrack(nums, [])
    return result


print(permuteUnique(input_array))