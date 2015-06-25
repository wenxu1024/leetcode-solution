#! /usr/bin/python

def primes(n):
  l = []
  sieve = [True] * (n+1)
  for p in range(2, n+1):
    if (sieve[p]):
      l.append(p)
      for i in range(p, n+1, p):
        sieve[i] = False
  return l

if __name__ == "__main__":
  n = 1000
  print primes(n)
