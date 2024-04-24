'''Maximizing the Value of the Loot Problem
Find the maximal value of items that fit into the backpack.
Input: The capacity of a backpack W as well as the weights(w1,...,wn) and costs (c1,..., cn) ofn different compounds.
Output: The maximum total value of fractions of items that fit into the backpack of the given capacity: 
i.e., the maximum value of c1· f1 + ··· + cn · fn such that w1·f1+···+wn·fn ≤ W and 0 ≤ fi ≤1 for all i 
(fi is the fraction of the i-th item taken to the backpack).'''

'''Input format. The first line of the input contains the number n of compounds and the capacity W of a backpack. 
The next n lines define
the costs and weights of the compounds. The i-th line contains the
cost ci and the weight wi of the i-th compound.
Output format. Output the maximum value of compounds that fit into the backpack.
To ensure this, output your answer with at least four digits after the decimal point '''

'''Constraints. 1 ≤ n ≤ 10^3, 0 ≤ W ≤ 2 · 10^6; 0 ≤ ci ≤ 2 · 10^6, 0 < wi ≤ 2 · 10^6
for all 1 ≤ i ≤ n. All the numbers are integers.'''
'________________________________________________________________'
'''Input:
3 50
60 20 
100 50 
120 30
Output:
180.0000'''

def maximize_loot(n, W, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_value = 0.0
    for cost, weight in items:
        if W == 0:  # If the backpack is full, break out of the loop
            break
        amount = min(W, weight)
        total_value += amount*cost/weight
        W -= amount
    
    return total_value

if __name__ == "__main__":
    data = input().split()
    n, W = int(data[0]), int(data[1])
    items = []

    index = 0
    for _ in range(n):
        data = input().split()
        ci = int(data[0])
        wi = int(data[1])
        items.append((ci, wi))

    max_value = maximize_loot(n, W, items)
    print(f"{max_value:.4f}")
