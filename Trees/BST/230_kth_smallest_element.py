"""
Given the root of a binary search tree, and an integer k,
                                   return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
Follow up: If the BST is modified often (i.e., we can do insert and delete operations)
                                               and you need to find the kth smallest frequently, how would you optimize?
"""
from dataclasses import dataclass
from typing import Optional
@dataclass
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    # Recursive solution
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        print(root.val)
        inorder(root.right)

    # Iteratively solution
    counter = 0
    stack = []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0: return root.val
        root = root.right