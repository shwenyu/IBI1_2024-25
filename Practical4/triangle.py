n=int(input("the length of triangle seq:"))
sum=0
for i in range(1,n+1) :		
	for j in range(i):		#each loop calculate the sum of the certain triangle
		sum += 	j+1
	print("the sum is:",sum)
	sum=0
'''
Pseudocode:
BEGIN
    PROMPT user to input the length of the triangle sequence and STORE it in variable n
    INITIALIZE sum to 0

    FOR each integer i from 1 to n (inclusive)
        FOR each integer j from 0 to i-1 (inclusive)
            ADD (j + 1) to sum
        END FOR

        PRINT "the sum is:" followed by the value of sum
        RESET sum to 0
    END FOR
END

'''