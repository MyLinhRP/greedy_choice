"""Car Fueling Problem
Compute the minimum number of gas tank refills to get from one city to another"""

"""Input: Integers d and m, as well as a sequence of integers stop1 <stop2 < ··· < stopn.
Output: The minimum number of refills to get from one city to another if a car can travel at most m miles on a full tank.
The distance between the cities is d miles and there are gas stations at distances stop1 , stop2 ,..., stopn along the way. 
We assume that a car starts with a full tank."""

"""Input format. The first line contains an integer d. 
The second line contains an integer m. The third line specifies an integer n. 
Finally, the last line contains integers stop1 , stop2 ,..., stopn.
Output format. The minimum number of refills needed. If it is not possible to reach the destination, output -1.
Constraints. 1 ≤ d ≤ 10^5. 1 ≤ m ≤ 400. 1 ≤ n ≤ 300. 0 < stop1 < stop2 <··· < stopn < d."""

"""Sample 1.
Input:
950
400
4
200 375 550 750
Output:
2
The distance between the cities is 950, the car can travel at most 400 miles on a full tank. 
It suffices to make two refills: at distance 375 and 750. 
This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.
"""

"""Sample 2.
Input:
10
3
4
1 2 5 9
Output:
-1
"""


def minimize_refill(running_limit_miles, num_stops_arr):
    current_stop = 0
    count = 0
    for i in range(len(num_stops_arr) - 1):
        if num_stops_arr[i] - current_stop > running_limit_miles:
            return -1
        if (
				num_stops_arr[i] - current_stop <= running_limit_miles < num_stops_arr[i + 1] - current_stop
		):
            count += 1
            current_stop = num_stops_arr[i]
    if num_stops_arr[i+1] - current_stop > running_limit_miles:
        return -1
    return count


if __name__ == "__main__":
    distances = int(input())
    running_limit_miles = int(input())
    num_stops = int(input())
    num_stops_arr = list(map(int, input().split()))
    num_stops_arr.append(distances)
    print(minimize_refill(running_limit_miles, num_stops_arr))
