def compute_S(n, mod):
    # Compute f[i] = number of x in [1, n] with v₂(x) = i.
    # v₂(x)=0 means x is odd.
    f = []
    i = 0
    # While 2^i <= n:
    while (1 << i) <= n:
        if i == 0:
            count = (n + 1) // 2 
        else:
            count = (n // (1 << i)) - (n // (1 << (i + 1)))
        f.append(count)
        i += 1
    m = len(f)  

    losing = 0
    for i_val in range(m):
        for j_val in range(m):
            k_val = i_val ^ j_val
            if k_val < m:
                losing = (losing + (f[i_val] * f[j_val] * f[k_val]) % mod) % mod

    T = pow(n, 3, mod)
    winning = (T - losing) % mod
    return winning

def main():
    mod = 1234567890

    n = 123456787654321
    ans = compute_S(n, mod)
    print("S(123456787654321) mod 1234567890 =", ans)

if __name__ == '__main__':
    main()
