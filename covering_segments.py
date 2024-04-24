'''
Covering Segments by Points Problem Find the minimum number of points needed to cover all given segments on a line.
Input: A sequence of n segments [l1, r1],...,[ln, rn] on a line.
Output: A set of points of minimum size such that each segment
[li, ri] contains a point, i.e., there exists a point x from this set such that li ≤ x ≤ ri
'''
'''
Input format. The first line of the input contains the number n of segments. Each of the following n lines contains two
integers li and ri (separated by a space) defining the coordinates of endpoints of the i-th segment.
Output format. The minimum number k of points on the first line and the integer coordinates of k points
(separated by spaces) on the second line. You can output the points in any order. If there are multiple
such sets of points, you can output any of them.
Constraints. 1 ≤ n ≤ 100; 0 ≤ li ≤ ri ≤ 10^9 for all i.'''

'''Sample 1.
Input:
3
1 3
2 5
3 6
Output:
1
3
Sample 2.
Input:
4
4 7
1 3
2 5
5 6
Output:
2
3 6
'''
def covering_segments(segments_arr):
	segments_arr.sort(key=lambda x: x[1])
	print((segments_arr))
	positions = []
	right_most =  segments_arr[0][1]
	for i in range(1, len(segments_arr)):
		print(i)
		if right_most in range(segments_arr[i][0], segments_arr[i][1]+1):
			if i == len(segments_arr)-1:
				positions.append(right_most)
		else:
			positions.append(right_most)
			right_most= segments_arr[i][1]
	if right_most not in range(segments_arr[-1][0], segments_arr[-1][1]+1):
		positions.append(right_most)
	return positions
if __name__ == '__main__':
	n = int(input())
	segments_arr = []
	for i in range(n):
		left, right = list(map(int,(input().split())))
		segments_arr.append((left, right))
	positions = covering_segments(segments_arr)
	print(len(positions))
	print(*positions)
