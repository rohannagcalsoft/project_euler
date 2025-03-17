#!/usr/bin/env python3
"""
Modified Nim – Three-Pile Game with Proper Divisor Removal

Rules summary:
  • Three piles with sizes (a, b, c), with 1 ≤ a,b,c ≤ n.
  • On a turn a player chooses one pile and removes d stones,
    where d is a proper divisor of the number in that pile.
  • A proper divisor of n is any positive divisor d < n.
  • A pile of size 1 has no move.
  • The game is impartial and (via the Sprague–Grundy theorem)
    a position is losing if and only if the nim–sum is 0.

Key observation:
  One may prove that the Grundy value of a single pile is:
      G(n) = v₂(n)
  where v₂(n) is the exponent of 2 in n.
  (For example, G(1)=0; for a prime p>2, G(p)=0; G(2)=1; G(4)=2; G(8)=3; etc.)

Thus the overall nim–sum for a triple is:
      v₂(a) ⊕ v₂(b) ⊕ v₂(c)
and the first player wins exactly when this xor is nonzero.

Let f(i) be the count of numbers in [1, n] with v₂(x) = i.
Then the total number of positions is T = n³ and the number of losing positions is:
      L = Σ₍i,j₎ f(i) * f(j) * f(i ⊕ j)
so that the number of winning positions is:
      S(n) = n³ − L.
We finally output S(n) modulo 1234567890.

The sample cases given are:
  S(10) = 692 and S(100) = 735494.
  
Below is the complete code.
"""

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
