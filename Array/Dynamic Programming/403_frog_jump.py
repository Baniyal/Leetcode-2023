"""
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist
a stone. The frog can jump on a stone, but it must not jump into the water.
Given a list of stones' positions (in units) in sorted ascending order, determine if the frog can cross the river by
landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.
If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units.
The frog can only jump in the forward direction.
________________________________________________________________________________________________________________________
Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone,
then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
________________________________________________________________________________________________________________________
Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
Input: stones = [0,1,3,4,5,7,9,10,12]
========================================================================================================================
16 test cases passed out of 52, TLE error
"""


def canCross(stones):
    stones_positions = set(stone_pos for stone_pos in stones)
    if stones[1] != 1:
        return False
    MEMOIZATION = {}
    last_stone = stones[-1]

    def func(curr_jump, curr_pos):
        if curr_pos not in stones_positions:
            return False
        print("curr_position ----------->", curr_pos)
        print("curr_jump---------------->", curr_jump)
        print("stones_positions--------->", stones_positions)
        print("destination-------------->", stones[-1])
        print("\n \n")
        if curr_pos == last_stone:
            return True
        if (curr_jump, curr_pos) in MEMOIZATION:
            return MEMOIZATION[(curr_jump, curr_pos)]
        for nex_jump in [curr_jump + 1, curr_jump - 1, curr_jump]:
            if (curr_pos + nex_jump > curr_pos) and func(nex_jump, curr_pos + nex_jump):
                MEMOIZATION[(curr_pos, curr_jump)] = True
                return True
        MEMOIZATION[(curr_pos, curr_jump)] = False
        return False

    if stones[1] == 1:
        return func(1, 1)
    else:
        return False


print(canCross(stones))


# =======================================================================================================================
# =========================================ACCEPTED SOLUTION=============================================================
def canCross(stones):
    n = len(stones)
    stoneSet = set(stones)
    visited = set()

    def goFurther(value, units):
        if (value + units not in stoneSet) or ((value, units) in visited):
            return False
        if value + units == stones[n - 1]:
            return True
        visited.add((value, units))
        return goFurther(value + units, units) or goFurther(value + units, units - 1) or goFurther(value + units,
                                                                                                   units + 1)

    return goFurther(stones[0], 1)
