
# arr[] to store all the distinct elements 
# index - next location in array 
# num - given number 
# reducedNum - reduced number 
def findCombinationsUtil(arr, index, n, red_num): 
	
	# Set to store all the 
	# distinct elements 
	s = set() 
	sum = 0

	# Base condition 
	if (red_num < 0): 
		return

	if (red_num == 0): 
		
		# Iterate over all the elements 
		# and store it into the set 
		for i in range(index): 
			s.add(arr[i]) 

		# Calculate the sum of all 
		# the elements of the set 
		for itr in s: 
			sum = sum + (itr) 

		# Compare whether the sum is equal to n or not, 
		# if it is equal to n print the numbers 
		if (sum == n and len(s) == 4): 
			for i in s: 
				print(i, end = " ") 
			print("\n", end = "") 
			return

	# Find previous number stored in the array 
	if (index == 0): 
		prev = 1
	else: 
		prev = arr[index - 1] 

	for k in range(prev, n + 1, 1): 
		
		# Store all the numbers recursively 
		# into the arr[] 
		arr[index] = k 
		findCombinationsUtil(arr, index + 1, 
							n, red_num - k) 

# Function to find all the 
# distinct combinations of n 
def findCombinations(n): 
	a = [0 for i in range(n + 1)] 
	findCombinationsUtil(a, 0, n, n) 

# Driver code 
if __name__ == '__main__': 
	n = 41
	findCombinations(n) 

# This code is contributed by Surendra_Gangwar 
