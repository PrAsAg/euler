
import math
from time import time
start = time()
primeList=[]
def IsPrime(test):
    if test == 2:  
        primeList.append(2)  
        return True  
    elif test < 2:  
        return False  
    else:  
        for i in primeList:  
            if i > math.sqrt(test):
                break
            elif test % i == 0:
                return False
        primeList.append(test)
        return True

# def IsPrime(n):
# 	count=0
# 	for x in range(1,(n//2)+1):
# 		if n%x==0:
# 			count=count+1
# 	if count==1:
# 		return True
# 	else:
# 		return False

# while True:
# 	x=int(input("Enter number:"))
# 	print(IsPrime(x))
			
def RotateCheck(n):
	x= int(math.log10(n))
	for i in range(0,x+1):
		rot=10**x*(n%10)+n//10
		if(IsPrime(rot)):
			n=rot
			if i==x:
				print(f"\t{n}")
				return True
		else:
			return False


def Count():
	cc=0
	for i in range(1000000):
		if IsPrime(i):
			if RotateCheck(i):
				print(f"{cc}:Yess")
				cc+=1
	print(cc)



Count()

print (f"process time :: {time()-start}")


# import math  
# num = 0  
# primeList = []

# def isprime(test):
#     if test == 2:  
#         primeList.append(2)  
#         return True  
#     elif test < 2:  
#         return False  
#     else:  
#         for i in primeList:  
#             if i > math.sqrt(test):
#                 break
#             elif test % i == 0:
#                 return False
#         primeList.append(test)
#         return True

# def rotations(n):
#     answer = []
#     rotation = n
#     while not rotation in answer:
#         answer.append(rotation)
#         rotation = int(str(rotation)[1:] + str(rotation)[0])
#     return answer

# for i in range(2,1000000):
#     numList = rotations(i)
#     valid = True
#     for j in numList:
#         if not isprime(j):
#             valid = False
#     if valid:
#         num += 1

#     print(num)




