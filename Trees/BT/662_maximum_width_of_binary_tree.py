"""

Submissions
Testcase
Testcase
Test Result
Test Result
Code
662. Maximum Width of Binary Tree
Solved
Medium
Topics
Companies
Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.



Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,2,5,null,null,9,6,null,7]
Output: 7
Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width exists in the second level with length 2 (3,2).
"""
from collections import deque
def function(root):
    queue = deque()
    queue.append([root ,1])
    max_width = 1
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_node, curr_node_index = queue.popleft()
            if curr_node.left : queue.append([curr_node.left, 2* curr_node_index])
            if curr_node.right: queue.append([curr_node.right, 2 * curr_node_index + 1])
        if len(queue) == 0:
            break
        indices = [val[1] for val in queue]
        max_width = max(max_width, indices[-1] - indices[0] + 1)
    return max_width