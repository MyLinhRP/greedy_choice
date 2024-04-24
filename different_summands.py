'''
Distinct Summands Problem
Represent a positive integer as the sum of the maximum number of pairwise distinct positive integers.
Input: A positive integer n.
Output: The maximum k such that n can be represented as the sum a1 + ··· + ak of k distinct positive integers.

Input format. An integer n.
Output format. In the first line, output the maximum number k such
that n can be represented as the sum of k pairwise distinct positive integers. In the second line,
output k pairwise distinct positive integers that sum up to n (if there are multiple such representations, output
any of them).
Constraints. 1 ≤ n ≤ 10^9.
'''
def find_distinct_summands(n: int):
    ans = []
    i = 1
    while i + 1 <= n - i:
        ans.append(i)
        n -= i
        i += 1
    if 0 < n:
        ans.append(n)
    return ans

if __name__ == '__main__':
    n = int(input())
    # Finding distinct summands
    summands = find_distinct_summands(n)
    # Printing output
    print(len(summands))
    print(*summands)
