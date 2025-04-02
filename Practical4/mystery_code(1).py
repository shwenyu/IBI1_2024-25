from random import randint  # Import the randint function to generate random integers

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil  # Import the ceil function to round numbers up to the nearest integer

progress=0  # Initialize a counter variable to track the number of iterations
while progress>=0:  # Start an infinite loop (condition always true)
	progress+=1  # Increment the counter by 1
	first_n = randint(1,6)  # Generate a random integer between 1 and 6 for the first number
	second_n = randint(1,6)  # Generate a random integer between 1 and 6 for the second number
	if first_n == second_n:  # Check if the two random numbers are equal
		print(progress)  # Print the number of iterations it took to find a match
		break  # Exit the loop once a match is found

