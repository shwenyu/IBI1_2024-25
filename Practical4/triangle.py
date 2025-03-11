n=int(input("the length of triangle seq:"))
sum=0
for i in range(1,n+1) :		
	for j in range(i):		#each loop calculate the sum of the certain triangle
		sum += 	j+1
	print("the sum is:",sum)
	sum=0