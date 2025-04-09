n=int(input("the length of triangle seq:"))  # Prompt the user to input the length of the triangle sequence and convert it to an integer
sum=0  # Initialize the variable 'sum' to 0
for i in range(1,n+1) :  # Loop through numbers from 1 to n (inclusive) to calculate sums for each triangle
	for j in range(i):  # Loop through numbers from 0 to i-1 to calculate the sum of the current triangle
		sum += 	j+1  # Add (j+1) to the sum for the current triangle
	print("the sum is:",sum)  # Print the sum of the current triangle
	sum=0  # Reset the sum to 0 for the next triangle
