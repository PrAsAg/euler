def result():
    m = [[int(n) for n in l.split(',')]
         for l in open('p082_matrix.txt', 'r')]
    ln = len(m)
    t = [m[r][0] for r in range(ln)]
    for c in range(1, ln):
        t = [m[r][c] + t[r] for r in range(ln)]
        # Comb the column looking for improvements, down then up.
        for r in range(1, ln):
            t[r] = min(t[r - 1] + m[r][c], t[r])
        for r in range(ln - 2, -1, -1):
            t[r] = min(t[r + 1] + m[r][c], t[r])

    return min(t)

print(result())