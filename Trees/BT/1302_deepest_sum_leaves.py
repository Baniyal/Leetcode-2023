"""
Given the root of a binary tree, return the sum of values of its deepest leaves.


Example 1:


Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
Output: 15
Example 2:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 19


Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100
"""
from collections import deque
def function(root):
    if root is None:
        return []

    queue = deque([root])
    while queue:
        n = len(queue)
        temp = []
        for _ in range(n):
            curr_node = queue.popleft()
            temp.append(curr_node.val)
            if curr_node.left:
                queue.append(curr_node.left)
            if curr_node.right:
                queue.append(curr_node.right)
    return sum(temp)
