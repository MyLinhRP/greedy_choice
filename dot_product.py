'''
Maximum Product of Two Sequences Problem
Find the maximum dot product of two sequences of numbers.
Input: Two sequences of n positive integers: price1,...,pricen and clicks1,...,clicksn.
Output: The maximum value of price1· c1 + ··· + pricen· cn,where c1,..., cn is a permutation of clicks1,...,clicksn.
'''
'__________________________________________________'
'''
Input format. The first line contains an integer n, the second one contains a sequence of integers price1 ,...,pricen
, the third one contains a sequence of integers clicks1,...,clicksn.
Output format. Output the maximum value of (price1·c1+···+pricen·cn),
where c1,..., cn is a permutation of clicks1,...,clicksn.
Constraints. 1 ≤ n ≤ 103; 0 ≤ pricei,clicksi ≤ 10^5 for all 1 ≤ i ≤ n.
'''
def dot_product(price, click):
	total_price = 0
	price = sorted(price)
	click = sorted(click)
	for i in range(len(price_arr)):
		total_price += price[i]*click[i]
	return total_price

if __name__ == '__main__':
	n = int(input())
	price_arr = list(map(int, input().split()))
	click_arr = list(map(int, input().split()))
	print(dot_product(price_arr, click_arr))



