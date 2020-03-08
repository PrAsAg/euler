from fractions import Fraction as frac

l = []

for i in range(1,100):
    for j in range(i+1,100):
        temp = frac(i,j)
        numera = frac(i,j).numerator
        det = frac(i,j).denominator
        if temp not in l and numera<det:
            l.append(frac(i,j))



print(l)
print("\n")
print(len(l))