"""
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:
Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.
________________________________________________________________________________________________________________________
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
________________________________________________________________________________________________________________________
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
=======================================LEARNINGS========================================================================
Do a left to right and right to left pass increasing the number of candies based on the ratings
________________________________________________________________________________________________________________________
When applying conditional check make sure that the updated value is dependent on reasonable parameters in this case the
neighbour rather than indiscriminately updating the value.
"""
RATINGS = [1, 2, 87, 87, 87, 2, 1]


def candy(ratings):
    number_of_children = len(ratings)
    candies = [1] * number_of_children
    for i in range(1, number_of_children):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i-1] + 1
    print("LEFT TO RIGHT PASS")
    print("==================")
    print(candies)
    result = candies[-1]
    for i in reversed(range(number_of_children - 1)):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i] , candies[i+1] + 1)
        result += candies[i]
    print("RIGHT TO LEFT PASS")
    print("==================")
    print(candies)
    return result


print(candy(RATINGS))
