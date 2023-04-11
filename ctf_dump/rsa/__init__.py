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
    
class BreakRSA:
    @classmethod
    def near_primes(cls, n: int, rng: int) -> Tuple[int, int]:
        p_approx = math.isqrt(n)

        for p in range(p_approx - rng, p_approx + rng):
            if n % p == 0:
                return (p, n // p)

        return (None, None)

    @classmethod
    def reuse_prime(cls, n1: int, n2: int) -> Tuple[int, int, int]:
        f = Fraction(n1, n2)

        q = f.numerator
        r = f.denominator

        p1 = n1 // q
        p2 = n2 // r

        assert p1 == p2, "Primes were not reused"

        return (p1, q, r)
