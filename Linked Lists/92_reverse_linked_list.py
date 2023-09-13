"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.
------------------------------------------------------------------------------------------------------------------------
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""


def reverseList(self, head):
    prev = None
    while head:
        curr = head
        head = head.next
        curr.next = prev
        prev = curr
    return prev


# ==========================================REVERSE LIST 2==============================================================

"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
list from position left to position right, and return the reversed list.Given the head of a singly linked list and two
integers left and right where left <= right, reverse the nodes of the list from position left to position right, and
return the reversed list.
________________________________________________________________________________________________________________________
Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


INPUT_ARRAY = [1, 2, 3, 4, 5]
LEFT = 2
RIGHT = 4
INPUT_LINKED_LIST = [ListNode(val) for val in INPUT_ARRAY]

for i in range(len(INPUT_ARRAY)):
    current_node = INPUT_LINKED_LIST[i]
    if i != len(INPUT_ARRAY) - 1:
        current_node.next = INPUT_LINKED_LIST[i + 1]

HEAD = INPUT_LINKED_LIST[0]


def reverseBetween(head, left, right):
    iterable = 1
    start = head
    prev = None
    curr = head
    while head:
        print("iter----------------->", iterable)
        print("head----------------->", head.val)
        print("curr----------------->", curr.val)
        print("prev----------------->", prev.val if prev else "None")
        print("\n")

        if iterable == left:
            last = prev
            print("**********************************")
            print("**********************************")
            print("**********************************")
            while iterable != right:
                print("INSIDE REVERSE FUNCTION")
                print("iter----------------->", iterable)
                print("head----------------->", head.val)
                print("curr----------------->", curr.val)
                print("prev----------------->", prev.val if prev else "None")
                print("\n")

                iterable += 1
                curr = head
                head = head.next
                prev = curr
            last.next = prev
            print("EXITING REVERSE LOOP")
            print("**********************************")
            print("**********************************")
            print("**********************************")

        iterable += 1
        curr = head
        if head: head = head.next
        prev = curr
    return start

result = (reverseBetween(HEAD, LEFT, RIGHT))

while result:
    print(result.val)
    result = result.next
