"""
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.
___________________________________________________________________________________
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
___________________________________________________________________________________
Input: root = [1,null,3]
Output: [1,3]
___________________________________________________________________________________
Input: root = []
Output: []
"""


#TODO: do this again
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
