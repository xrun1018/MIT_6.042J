# @XuRUn: 04/2021

def gcd(a, b):
  assert a >= 0 and b >= 0 and a + b > 0

  if b == 0:
    d, x, y = a, 1, 0 
  else:
    d, p, q = gcd(b, a % b)
    x = q
    y = p - q * (a // b)
  return (d, x, y)

def diophantine(a, b, c):
  assert c % gcd(a, b)[0] == 0
  d, x, y = gcd(a, b)
  coef = c / d
  return (x * coef, y * coef)

def divide(a, b, n):
  assert n > 1 and a > 0 and gcd(a, n)[0] == 1
  s, t = diophantine(n, a, 1)
  # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
  return (b * s) % n
