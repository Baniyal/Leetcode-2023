"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.

Populate each next pointer to point to its next right node.
                                                 If there is no next right node, the next pointer should be set to NULL.
------------------------------------------------------------------------------------------------------------------------
Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to
its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers,
with '#' signifying the end of each level.
------------------------------------------------------------------------------------------------------------------------
"""
from collections import deque


def function(root):
    if root is None:
        return
    queue = deque([root])
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()

            if i < size - 1:
                node.next = queue[0]
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return root


TEST_CASES = [
                       ((3, [[0,1],[1,2],[2,0]],             0,  2), True ),
                       ((6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0,  5), False)
             ]

DEBUG = False

if __name__ == '__main__':

    for test_case, expected_result in TEST_CASES:
        actual_result = function(test_case)
        if actual_result == expected_result:
            print(f"PASSED")
        else:
            print(f"FAILED \nTest Case {test_case} . With actual result: {actual_result} \n and expected result: {expected_result}")
        print("--------------------------------")
        if DEBUG:
            break
