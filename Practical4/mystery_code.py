from random import randint  # Import the randint function to generate random integers.
from math import ceil  # Import the ceil function to round numbers up to the nearest integer.

progress=0  # Initialize a variable 'progress' to 0 to count iterations.
while progress>=0:  # Start an infinite loop (condition always true since progress >= 0).
	progress+=1  # Increment the 'progress' counter by 1.
	first_n = randint(1,6)  # Generate a random integer between 1 and 6 and assign it to 'first_n'.
	second_n = randint(1,6)  # Generate another random integer between 1 and 6 and assign it to 'second_n'.
	if first_n == second_n:  # Check if the two random numbers are equal.
		print(progress)  # If equal, print the current value of 'progress'.
		break  # Exit the loop.

