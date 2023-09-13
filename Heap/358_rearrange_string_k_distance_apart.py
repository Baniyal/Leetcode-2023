"""
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other.
If it is not possible to rearrange the string, return an empty string "".
________________________________________________________________________________________________________________________
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.
________________________________________________________________________________________________________________________
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.
________________________________________________________________________________________________________________________
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
"""
from collections import Counter
from heapq import heappop, heappush, heapify

S = "aaaabbcc"
K = 3

"""
============================================INTUITION====================================================================
Priority Queue  | Heap

We are given a string S with only lowercase English letters and an integer K; we need to rearrange the characters of
S so that the same characters are at least distance K from each other.This implies that if we place a character at index,
say x, the smallest index that this same character can be placed at next is index x+K. We can return any string as long 
as the above criteria are met.But which character to start from? One observation we need to make here is that when we 
keep a character on indices, say x and x+K  all characters between these indices must be unique; otherwise, there would 
be a pair of characters breaking the rule. From this observation, we can deduce that it might be better to start with
characters that have high frequencies in the string SSS. This is because if we are left with high-frequency characters 
in the end, we might not be able to find enough different characters to place between the two same characters.
Therefore, for each index, we will find the character with the highest frequency (not used in the last K indices) and
put it in the answer string. One might think of sorting the characters by their count to achieve this, but the 
frequencies will be changing continuously, and we will need to sort the characters again and again. To efficiently keep
track of the maximum frequency, we can use a max heap, keeping the highest frequency character at the top.
Now, we know which character to place at the current index, but we cannot simply put the character back into the heap 
without ensuring that it won't come back before the following K indices. For this, we will use a queue; when we pop the 
character from the heap and use it in the answer string, we will decrement its frequency and insert it into the queue.
When the queue size becomes KKK, we will know that the character at the front can be reused, and there will be one entry
in the queue for each character placed in the answer string.

Before popping out the character from the max heap, we will check if the size of the queue is K or not; if yes, we will
insert that character with its frequency in the heap. This way, the heap will only hold characters that are allowed to 
be used. Then we will pop the highest frequency character from the heap and use it for the answer string. In case the 
heap is empty; it would imply that no character is available now, i.e. placed before K indices, and hence we will return
an empty string in such cases as the problem requires.
===============================================ALGORITHM================================================================
* Create a map freq from character to integer (or integer to integer by converting char to ASCII values). This map will 
store the frequency of each character in the string S.
* Create a max heap/priority queue free; this queue will have all the characters that can be placed next, with the
character having the highest frequency at the top.
* Initialize an empty queue busy, which will store the characters that cannot be used as they have been used within 
previous K indices.
* Do the following until the length of string ans becomes equal to the length of S:
-------------Check if the size of busy is K; if yes, remove it from the front of the queue and add the element back to free.
-------------If free is empty, there is no available character to place, and the task is impossible. Return an empty string.
-------------Remove the top character from the heap and append it to ans. Decrement its frequency in freq. If the frequency
            is not zero, insert it into the busy.
"""
from heapq import heappop, heappush, heapify
from collections import deque
STRING = "aabbcc"
K = 3


def rearrangeString_2(s, k):
    count_dict = Counter(s)
    count_set = [(-1*val, key) for key, val in count_dict.items()]
    busy = deque()
    heapify(count_set)
    res = ""
    while count_set and len(res) < len(s):
        print("Heap--------->",count_set)
        count, char = heappop(count_set)
        if count == 0:
            continue

        if len(busy) == k:
            print("--------queue is full--------")
            popped_count, popped_char = busy.popleft()
            print(popped_count, popped_char)
            heappush(count_set, (popped_count, popped_char))
        if count != 1:
            busy.append((count + 1,char))
        res += char
        print("Result---------->",res)
        print("Queue-------->",busy)
        print("\n")
    if len(res) != len(s):
        return ""
    return res


print(rearrangeString_2(STRING,K))
