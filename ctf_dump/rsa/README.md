# RSA

## Definition

RSA is an asymmetric encryption (aka one key for encryption and one for decryption). It uses prime numbers and modular arithmetic to encrypt/decrypt messages.

## Values

### Prime Numbers (p, q, ...)

The standard algorithm generates 2 **unique + large** prime numbers.

The algorithm still works with more than 2 primes, just have to modify some usage.

### Public Modulus (n)

A public modulus (`n`) is the product of all prime.

If we have 2 primes, this is `n = p * q`.

### Totient Function (phi(n))

The totient function is a "magic" number theory method that counts the positive coprimes less than a number.

All you need to care about really is that: 

```
phi(n) = n * (1 - 1/p_1) * (1 - 1/p_2) * ... * (1 - 1/p_n)
```

Where: `p_i` is a **unique** prime factor of `n`.

If you only have 2 primes for `n`, this is often simplifed to `phi(n) = (p - 1)(q - 1)`.

### Public Exponent (e)

A public exponent is coprime of `n` between `[1, phi(n)]`.

This should most likely be given by you and commonly `e = 3, 5, 17, 257, or 65537`.

### Public Key

A public key is the public modulus and public exponent combined. Extract `n` and `e` from this key.

### Private Exponent (d)

A private exponent is a value to reverse the encryption algorithm. This value satisfies:

```
d*e (mod phi(n)) == 1
```

We can calculate this with:

```
d = invmod(e, phi(n))
```

There are multiple values to satisfy this equation, but we usually take the smallest one to save on computation time.

### Private Key

A private key is the public modulus and private exponent combined. Extract `n` and `d` from this key.

### Message (m)

A message is a text to be encrypted.

### Encrypted Message (c)

An encrypted message is a text to be decrypted.

## Algorithms

### Encryption

```
c = pow(m, e) % n

or

c = pow(m, e, n)
```

### Decryption

```
m = pow(c, d) % n

or 

m = pow(c, d, n)
```

## Example

Assuming we want to encrypt:

```
m = 2
```

We take 2 primes:

```
p = 3
q = 11
```

We calculate the public modulus:

```
n = p * q 

n = 33
```

We calculate the totient function:

```
phi(n) = n * (1 - 1/p) * (1 - 1/q)
phi(n) = pq * (p - 1)/p * (q - 1)/q
phi(n) = (p - 1)(q - 1)

phi(n) = 20
```

We want to pick a public exponent that is `1 < e < phi(n)` coprime to `n`:

```
e = 7
```

We can now encrypt on message:

```
c = pow(m, e, n)
c = (2 ** 7) % 33
c = 128 % 33

c = 29
```

We can find our decryption key:

```
d * e % phi(n) = 1
d = invmod(e, phi(n))

d = 3
```

We can check that `d` satisfies our equality:

```
3 * 7 % 20 = 1
21 % 20 = 1
1 = 1 
```

We can get back the `m` from `c`:

```
m = pow(c, d, n)
m = (29 ** 3) % 33
m = 24389 % 33

m = 2
```

## Attack

### Small Primes

If the primes are small, you can find the factors of `n` http://factordb.com/.

### Near Primes

If `n = p * q` and `p` and `q` are near, we can assume that their product will be almost be a squared number (`n ~ p * p` or `n ~ q * q`). Therefore, we can assume `p ~ sqrt(n)`. So we can bruteforce values around `sqrt(n)` until we get a factor.

### Duplicate Primes

If `n = p * q` and `p == q`, then `p = q = sqrt(n)`. Note that `phi(n) = p * (p - 1)` in this case (`phi(n)` definition uses **unique** primes).

### Reused Primes

If `n1 = p * q` and `n2 = p * r`, then `n1 / n2 = q / r`. We can extract the numerator and denominator to get `q` and `r`. Then `p = n1 / q` or `p = n2 / r`.
