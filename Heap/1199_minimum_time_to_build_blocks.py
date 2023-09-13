"""
You are given a list of blocks, where blocks[i] = t means that the i-th block needs t units of time to be built.
A block can only be built by exactly one worker. A worker can either split into two workers(# of workers increases by one)
or build a block then go home. Both decisions cost some time. The time cost of spliting one worker into two workers is
given as an integer split. Note that if two workers split at the same time, they split in parallel so the cost would be split.
Output the minimum time needed to build all blocks.
________________________________________________________________________________________________________________________
Input: blocks = [1], split = 1
Output: 1
Explanation: We use 1 worker to build 1 block in 1 time unit.
________________________________________________________________________________________________________________________
Input: blocks = [1,2], split = 5
Output: 7
Explanation: We split the worker into 2 workers in 5 time units then assign each of them to a block so the cost is
5 + max(1, 2) = 7.
________________________________________________________________________________________________________________________
Input: blocks = [1,2,3], split = 1
Output: 4
Explanation: Split 1 worker into 2, then assign the first worker to the last block and split the second worker into 2.
Then, use the two unassigned workers to build the first two blocks.
The cost is 1 + max(3, 1 + max(1, 2)) = 4.
==========================================SOLUTION======================================================================
Use huffman coding paradigm here
the more often the symbol is used, the shorter the length of the symbol
"""

blocks = [1, 2, 4, 7, 10]
split = 3

from heapq import heapify, heappop, heappush


def minBuildTime(blocks, split):
    heapify(blocks)
    while True:
        if len(blocks) == 1:
            return blocks[0]
        smallest_block, second_smallest_block = heappop(blocks), heappop(blocks)
        heappush(blocks, second_smallest_block + split)
