import math, time
def sum_all_proper_factors(n):
    f = set([1])
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            f.add(i)
            f.add(n // i)
    return sum(f)
    

def pe_095_Amicable_chains():
    LIMIT = 1000000
    
    cycles = dict()
    
    for n in range(1, LIMIT + 1):
        if n % 10000 == 0:
            print(n)
        
        cyc = [n]
        
        s = sum_all_proper_factors(n)
        
        while True:

            if s == n:
                for c in cyc:
                    cycles[c] = cyc
                break

            if s > LIMIT:
                break

            if s in cyc:
                # n didn't cycle!
                break
            
            cyc.append(s)
            s = sum_all_proper_factors(s)

        
    longest = 0
    for n, c in cycles.items():
        if len(c) >= longest:
            longest = len(c)
            print("New longest chain for n:", n, "len:", len(c), "chain:", c)
        
    # ... 28 chain: [629072, 589786, 294896, 358336, 418904, 366556, 274924, 275444, 243760, 376736, 381028, 285778, 152990, 122410, 97946, 48976, 45946, 22976, 22744, 19916, 17716, 14316, 19116, 31704, 47616, 83328, 177792, 295488]
    # Done in 455.9520790576935 seconds.

global start_time
start_time = time.time()
pe_095_Amicable_chains()
print("Done in %s seconds." % (time.time() - start_time))