"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters
'N' and 'Y':
                if the ith character is 'Y', it means that customers come at the ith hour
                    whereas 'N' indicates that no customers come at the ith hour.
                If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:
For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.
Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.
------------------------------------------------------------------------------------------------------------------------
Input: customers = "YYNY"
Output: 2
Explanation:
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
========================================================================================================================
==========================================LEARNINGS=====================================================================
In these questions think of doing, prefix  and suffix sum or running sum
solution for above problem
At any index, the penalty is the sum of prefix count of ‘N’ and suffix count of ‘Y’.
"""

customers = "YN"
expected_op = 2


def bestClosingTime(customers):
    n = len(customers)
    prefix_n = [0] * n
    suffix_y = [0] * n
    for i in range(n):
        if i == 0 and customers[i] == "N":
            prefix_n[i] = 1
        elif i == 0 and customers[i] == "Y":
            prefix_n[i] = 0
        elif customers[i] == "N":
            prefix_n[i] = prefix_n[i - 1] + 1
        elif customers[i] == "Y":
            prefix_n[i] = prefix_n[i - 1]

    for i in range(n - 1, -1, -1):
        if i == n - 1 and customers[i] == "Y":
            suffix_y[i] = 1
        elif i == n - 1 and customers[i] == "N":
            suffix_y[i] = 0
        elif customers[i] == "Y":
            suffix_y[i] = suffix_y[i + 1] + 1
        elif customers[i] == "N":
            suffix_y[i] = suffix_y[i + 1]

    resultant_index = 0
    temp_min = 10**4
    for i in range(n):
        if prefix_n[i] + suffix_y[i] < temp_min:
            print("i----------->",i)
            print("prefix N --->",prefix_n[i])
            print("suffix Y---->",suffix_y[i])
            print("min loss---->",max(prefix_n[i],suffix_y[i]))
            print("\n")
            resultant_index = i
            temp_min = prefix_n[i] + suffix_y[i]

    if customers[-1] == "Y":
        return resultant_index + 1
    else:
        return resultant_index


print(bestClosingTime(customers))

# ======================================================================================================================
# =============================================ACCEPTED SOLUTION========================================================
def bestClosingTime(customers):
    # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.
    cur_penalty = min_penalty = customers.count('Y')
    earliest_hour = 0
    for i, ch in enumerate(customers):
        if ch == 'Y':
            cur_penalty -= 1
        else:
            cur_penalty += 1
        # Update earliest_hour if a smaller penatly is encountered
        if cur_penalty < min_penalty:
            earliest_hour = i + 1
            min_penalty = cur_penalty

    return earliest_hour
