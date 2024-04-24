'''Money Change Problem
Compute the minimum number of coins needed
to change the given value into coins with denominations 1, 5, and 10.
Input: An integer money.
Output: The minimum number
of coins with denominations 1, 5,
and 10 that changes money.'''
"______________________________________"
'''In this problem, you will implement a simple greedy algorithm used by
cashiers all over the world. We assume that a cashier has unlimited number
of coins of each denomination.
Input format. Integer money.
Output format. The minimum number of coins with denominations 1, 5,
10 that changes money.
Constraints. 1 ≤ money ≤ 10^3'''
"______________________________________"
'''Sample 2.
Input:
28
Output:
6
28 = 10 + 10 + 5 + 1 + 1 + 1.'''


def money_exchange(n):
    return (n//10 + (n %10)//5 + n%5)
if __name__ == '__main__':
    n = int(input())
    print(money_exchange(n))

