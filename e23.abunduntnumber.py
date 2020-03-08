# from time import process_time
# def FactorSum(n):
# 	sum=0
# 	for i in range(1,(n//2)+1):
# 		if n%i==0:
# 			sum=sum+i;
# 	return sum

# # inp=int(input("Enter number:"))
# # print(FactorSum(inp))
# adun=[]
# for i in range(1,28123):
# 	if FactorSum(i)>i:
# 		adun.append(i);

# print(len(adun))
# print(f"Time required:	{process_time()}")


#time module for calculating execution time
import time

#square root from math module
from math import sqrt

#time at the start of execution
start = time.time()

#Function used from problem 21
def divisors(n):
	"""This function will generate 
	divisors of given number
	Example: divisors(28) will give
	[1,2,4,7,14]"""
	divs = [1]
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			divs.extend([i,n/i])
	return list(set(divs))

#list to store the values of abundant numbers
ab = []

#For loop to generate the abundant numbers
for i in range(12,28123):
	if sum(divisors(i))>i:
		ab.append(i)

#first let us assume all the numbers are 
#not sum of abundant numbers
non_ab_sum = [x for x in range(28123)]

#for loop to generate sum of two 
#abundant numbers
for i in range(len(ab)):
	for j in range(i,28123):
		if ab[i]+ab[j] < 28123:
			#negating the value of the abundant sum
			non_ab_sum[ab[i]+ab[j]] = 0
		else:
			break

#printing the value of the sum of non abundant sum
print (sum(non_ab_sum))
        
#printing the total execution time
print (time.time() -start)