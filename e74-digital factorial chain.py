from math import factorial as fact
from time import time as tm
start= tm()

count = 0

def EveryDigitFactorialSum(n):
    sumoffactorial=0
    while n:
        last= n%10
        sumoffactorial=sumoffactorial+ fact(last)
        n=n//10
    return sumoffactorial

def ListLenCheck(n):
    templist=[]
    templist.append(n)
    while True:
        Every = EveryDigitFactorialSum(n)
        n= Every
        # if(len(templist)>=61):
        #     break
        if Every  not  in templist:
            templist.append(Every)

        else:
            break

    return (len(templist))


for i in range(1000000):
    if(ListLenCheck(i)==60):
        #print(f"{i}")
        count=count+1

print(f"There are {count} chains of length 60\nSolution took {tm()-start} seconds")
#print(f"\ncompilation time::{tm()-start}") 

# number= 98000021

# s= fact(map(int, str(number)))

# # sum(map(int, str(number)))


# print(s)

