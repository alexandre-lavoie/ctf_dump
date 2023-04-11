from typing import List, Tuple
import math
from fractions import Fraction

class RSA:
    @classmethod
    def calculate_n(cls, primes: List[int]) -> int:
        n = 1

        for prime in primes:
            n *= prime

        return n

    @classmethod
    def totient(cls, primes: List[int]) -> int:
        n = cls.calculate_n(primes)

        unique_primes = set(primes)

        prefix = n
        for prime in unique_primes:
            prefix //= prime

        product = prefix
        for prime in unique_primes:
            product *= (prime - 1)

        return product
    
    @classmethod
    def calculate_d(cls, e: int, primes: List[int]) -> int:
        t = cls.totient(primes)
        
        return pow(e, -1, t)

    @classmethod
    def encrypt(cls, m: int, e: int, n: int) -> int:
        return pow(m, e, n)
    
    @classmethod
    def decrypt(cls, c: int, d: int, n: int) -> int:
        return pow(c, d, n)
    
def test_encrypt_decrypt():
    p = 3
    q = 11
    ps = [p, q]

    n = RSA.calculate_n(ps)
    e = 7

    m_in = 2
    c = RSA.encrypt(m_in, e, n)
    
    d = RSA.calculate_d(e, ps)
    m_out = RSA.decrypt(c, d, n)

    assert m_in == m_out

class BreakRSA:
    @classmethod
    def near_primes(cls, n: int, rng: int) -> Tuple[int, int]:
        p_approx = math.isqrt(n)

        for p in range(max(p_approx - rng, 2), p_approx + rng):
            if n % p == 0:
                return (p, n // p)

        return (None, None)

    @classmethod
    def reused_primes(cls, n1: int, n2: int) -> Tuple[int, int, int]:
        f = Fraction(n1, n2)

        q = f.numerator
        r = f.denominator

        p1 = n1 // q
        p2 = n2 // r

        assert p1 == p2, "Primes were not reused"

        return (p1, q, r)

def test_near_primes():
    p_in = 3
    q_in = 11
    ps = [p_in, q_in]

    n = RSA.calculate_n(ps)

    p_out, q_out = BreakRSA.near_primes(n, 10)

    assert p_in == p_out
    assert q_in == q_out

def test_reused_primes():
    p_in = 3
    q_in = 7
    r_in = 11
    
    n1 = RSA.calculate_n([p_in, q_in])
    n2 = RSA.calculate_n([p_in, r_in])

    p_out, q_out, r_out = BreakRSA.reused_primes(n1, n2)

    assert p_in == p_out
    assert q_in == q_out
    assert r_in == r_out

def test():
    test_encrypt_decrypt()
    test_near_primes()
    test_reused_primes()

if __name__ == "__main__":
    test()
