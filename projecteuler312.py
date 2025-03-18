def C(n, mod = None): 
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return 8
    return 8*pow(12, (pow(3, (n-2)) - 3)//2, mod) % mod

if __name__ == "__main__":
    print(C(C(C(10000 % (6*13**2), (6*13**4)), (6*13**6)), (13**8)))