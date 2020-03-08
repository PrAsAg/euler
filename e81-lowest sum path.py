matrix = [list(map(int, row.split(','))) for row in open("p081_matrix.txt").readlines()]
print(len(matrix))
for i in range(len(matrix)):
        for j in range(len(matrix)):

            if i*j>0:
                matrix[i][j] += min(matrix[i - 1][j], matrix[i][j - 1])
            else:
                #check i==0 or not
                if i:
                    matrix[i][j] += matrix[i - 1][j]
                else:
                    #check i==0 or not
                    if j:
                        matrix[i][j] += matrix[i][j - 1]
                    else:
                        matrix[i][j] += 0

print ("Result: ", matrix[-1][-1])
 
