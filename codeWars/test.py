# Build a pile of Cubes

def find_nb(m):
    # your code
    n = 0
    while m > 0:
        m -= n**3
        n += 1
    if m == 0:
        return n-1
    else:
        return -1
