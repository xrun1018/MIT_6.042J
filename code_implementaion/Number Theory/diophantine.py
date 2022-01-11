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
  coef = c / gcd(a, b)[0]
  # return (x, y) such that a * x + b * y = c
  d, x, y = gcd(a, b)
  return (x * coef, y * coef)
