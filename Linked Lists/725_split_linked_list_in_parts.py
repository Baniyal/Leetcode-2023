"""
Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked
list parts.The length of each part should be as equal as possible: no two parts should have a size differing by more
than one. This may lead to some parts being null.
The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size
greater than or equal to parts occurring later.
Return an array of the k parts.
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
use divmod(N, k) function to get the dividend and remainder for the particular
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


INPUT_ARRAY = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
INPUT_LINKED_LIST = [ListNode(val) for val in INPUT_ARRAY]

for i in range(len(INPUT_ARRAY)):
    current_node = INPUT_LINKED_LIST[i]
    if i != len(INPUT_ARRAY) - 1:
        current_node.next = INPUT_LINKED_LIST[i + 1]

HEAD = INPUT_LINKED_LIST[0]
K = 6


def splitListToParts(head, k):
    def get_length_of_list(head):
        n = 0
        while head:
            head = head.next
            n += 1
        return n

    length_of_list = get_length_of_list(head)
    result = []
    size_of_each_part = length_of_list // k
    iter = 0
    while iter < length_of_list and head:
        iter += 1
        temp = []
        if iter < length_of_list % k:
            for _ in range(size_of_each_part + 1):
                if head:
                    temp.append(head.val)
                    head = head.next
                else:
                    break
        else:
            for _ in range(size_of_each_part):
                if head:
                    temp.append(head.val)
                    head = head.next
                else:
                    break
        result.append(temp)

    return result


print(splitListToParts(HEAD, K))

# ====================================OFFICIAL SOLUTION=================================================================


def splitListToParts(self, root, k):
    cur = root
    for N in range(1001):
        if not cur: break
        cur = cur.next
    width, remainder = divmod(N, k)

    ans = []
    cur = root
    for i in range(k):
        head = cur
        for j in range(width + (i < remainder) - 1):
            if cur: cur = cur.next
        if cur:
            cur.next, cur = None, cur.next
        ans.append(head)
    return ans
