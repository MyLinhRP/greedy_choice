def max_salary(numbers):
	# Custom comparison function defined by the sort order needed
	# We convert numbers to strings and compare them based on concatenated results
	# The key makes sure to compare them as '56' + '5' vs '5' + '56' which is '565' vs '556'
	sorted_numbers = sorted(numbers, key=lambda x: str(x) * 10, reverse=True)

	# Concatenate the sorted numbers into the largest possible number
	result = ''.join(map(str, sorted_numbers))

	return result


def main():
	# Input reading similar to C scanf
	n = int(input())
	arr = list(map(int, input().split()))

	# Compute and print the maximum salary
	print(max_salary(arr))


if __name__ == "__main__":
	main()
